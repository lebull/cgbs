import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from django.db.models import Q #For ORs in queries

from django.core.exceptions import ValidationError

from colorful.fields import RGBColorField

class Season(models.Model):
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=False)
    current_week = models.IntegerField(default=1)
    users = models.ManyToManyField(User, related_name='user')
    
    def add_user(self, user):
        self.users.add(user)
        
    def get_user_record(self, user):
        #Get all picks
        complete_games = self.game_set.filter(complete=True).all()
        
        result = (0, 0)
        
        for game in complete_games:
            
            pick = game.get_current_pick_by_author(user)
            
            if pick != None and pick.winner == game.winner:
                result = (result[0] + 1, result[1])
            else:
                result = (result[0], result[1] + 1)
                
        return result
        

    def get_all_user_records(self):
        records = {}
        result = []
        
        complete_games = self.game_set.filter(complete=True).all()
        
        for user in self.user_set:
        
            record = (0, 0)
        
            for game in complete_games:
                if game.get_current_pick_by_author(user).winner == game.winner:
                    record[user] = (record[0] + 1, record[1])
                else:
                    record[user] = (record[0], record[1] + 1)
            result.append((user, record))
        
        #TODO: Sort
        
        return result

    def __unicode__(self):
        return str(self.name)
        

class Team(models.Model):
    name = models.CharField(max_length=128)
    abreviation = models.CharField(max_length=4, default='????')
    #Logo image
    rank=models.IntegerField(null=True, blank=True)
    #Rank (null=True, blank=True)
    primary_color = RGBColorField()
    
    def get_record(self):
        
        wins = 0
        losses = 0        

        games = Game.objects.filter(Q(away_team = self) | Q(home_team = self))
        
        for game in games:
            if game.complete:
                if game.get_winner() == self:
                    wins += 1
                else:
                    losses += 1
            
        return wins, losses
    record = property(get_record)

    def __unicode__(self):
        return self.name


class Game(models.Model):
    
    #pickable = PickableGameQuerySet.as_manager()
    
    season = models.ForeignKey(Season)

    away_team = models.ForeignKey(Team, related_name='%(class)s_away_team')
    home_team = models.ForeignKey(Team, related_name='%(class)s_home_team')

    week = models.IntegerField()
    kickoff_time = models.DateTimeField(null=True, blank=True)
    
    complete = models.BooleanField(default=False)
    away_score = models.IntegerField(null=True, blank=True)
    home_score = models.IntegerField(null=True, blank=True)
    
    location = models.CharField(null=True, blank=True, max_length="50")
    
    
    def get_winner(self):
        if self.complete == True:
            if self.home_score > self.away_score:
                return self.home_team
            if self.away_score > self.home_score:
                return self.away_team
        return None
    get_winner.description = 'Winner'
    winner = property(get_winner)
    
    #TODO: Create a manager, and create a get_pickable method.
    #Keep this here, though.  Refactor to pickable
    def can_pick(self):
        if self.week == self.season.current_week:
            if self.kickoff_time == None:
                return True
    
            if self.complete == False\
                and timezone.now() <= self.kickoff_time:
                    return True
        return False
                
    can_pick.admin_order_field = 'kickoff_time'
    can_pick.boolean = True
    can_pick.description = 'Can Pick?'
    pickable = property(can_pick)
    
    def can_user_pick(self, user):
        if self.can_pick() == True and user in self.season.users.all():
            return True
        else:
            return False
    
    def pick(self, author, winner, funny_winner_name=None, funny_looser_name=None):
        
            if author not in self.season.users.all():
                raise ValidationError("User cannot pick")
        
            return Pick.objects.create(
                        author=author,
                        game=self,
                        winner=winner,
                        funny_winner_name=funny_winner_name,
                        funny_looser_name=funny_looser_name
            )
        
    def get_current_pick_by_author(self, author):
        try:
            return self.pick_set.filter(author=author).latest('id')
        except Pick.DoesNotExist:
            return None
            
        
    def get_all_picks_by_author(self, author):
        try:
            return self.pick_set.filter(author=author).all()
        except Pick.DoesNotExist:
            return []
        
    def get_all_active_picks(self):
        
        return_dict = {}
        
        for user in self.season.users.all():
            return_dict[user] = self.get_current_pick_by_author(user)
            
        return return_dict
            
            
        
    def get_away_home_picks(self):
        
        pick_by_author = {}
        
        #Get the latest pick from 
        for pick in self.pick_set.all().order_by('id'):
            pick_by_author[pick.author] = (pick)
            
        away_picks = []
        home_picks = []
        
        for pick in pick_by_author.values():
            if pick.winner == pick.game.home_team:
                home_picks.append(pick)
            if pick.winner == pick.game.away_team:
                away_picks.append(pick)

        return away_picks, home_picks
        
    def get_away_home_picks_count(self):
        away_home_picks = self.get_away_home_picks()
        return len(away_home_picks[0]), len(away_home_picks[1])
            

    def __unicode__(self):
        away_rank_string = ""
        home_rank_string = ""
        
        if self.away_team.rank != None:
            away_rank_string = "({})".format(str(self.away_team.rank))  
            
        if self.home_team.rank != None:
            home_rank_string = "({})".format(str(self.away_team.rank))  
        
        return "{} {} vs. {} {}".format(self.away_team, 
            away_rank_string, 
            self.home_team, 
            home_rank_string
        )
        
class PickableGameQuerySet(models.QuerySet):
    
    def by_author(self, author):
        #Return games where the author is accepted in the game's season
        #   and the game is pickable.
        pickable_games = self.filter(can_pick=True)
        return
    
    def by_season(self, season):
        return self.filter(season=season, can_pick=true)

class Pick(models.Model):
    
    author = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(Team)
    
    timestamp = models.DateTimeField(default=timezone.now())
    
    def __unicode__(self):
        return str(self.winner.name)    

# Create your models here.