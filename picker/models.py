import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse

from django.db.models import Q #For ORs in queries

from django.core.exceptions import ValidationError

#from colorful.fields import RGBColorField

class Season(models.Model):
    ''' A single season of a single sport.
    :todo: Split this into a Season(collection of games) and a 
        Board(collection of users).
    '''
    name = models.CharField(max_length=128)
    active = models.BooleanField(default=False)
    current_week = models.IntegerField(default=1)
    users = models.ManyToManyField(User, related_name='user')
        
    def get_user_record(self, user):
        '''Get the w-l record of a single user in this season.
        No pick for a game will not be considered.
        
        :param User: The user whose w-l record will be returned.
        :return tuple: (wins, losses)
        '''
        
        complete_games = self.game_set.filter(complete=True).all()
        wins = 0
        losses = 0
        
        for game in complete_games:
            
            # Consider only the active pick.
            pick = game.get_current_pick_by_author(user)
            
            # The user may have not picked this game.
            if not pick:
                continue
            
            if (pick.winner == game.winner):
                wins += 1 
            else:
                losses += 1
                
        return (wins, losses)
        

    def get_all_user_records(self):
        ''' Returns a list of users and their records
        
        :todo: Sort by wins then losses.
        
        :return list: List of tuples in the format (User, (wins, losses))
        ordered by wins.
        '''
        result = [(user, self.get_user_record(user)) for user in self.users.all()]
        result.sort(key=lambda user_record: user_record[1][1], reverse=True)
        result.sort(key=lambda user_record: user_record[1][0], reverse=True)
        #result.sort(key=lambda user_record: user_record[0])

        return result

    def __unicode__(self):
        return str(self.name)
        

class Team(models.Model):
    ''' A team that may or may not win a game. '''
    name = models.CharField(max_length=128)
    abreviation = models.CharField(max_length=4, default='????')
    #Logo image
    rank=models.IntegerField(null=True, blank=True)
    #primary_color = RGBColorField()
    
    def __unicode__(self):
        return self.name


class Game(models.Model):

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
        '''Get the winner of the game if it is complete.
        :returns: Team or None if the game is not complete'''
        if self.complete == True:
            if self.home_score > self.away_score:
                return self.home_team
            if self.away_score > self.home_score:
                return self.away_team
        return None
        
    get_winner.description = 'Winner'
    winner = property(get_winner)
    
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
    
    def get_current_pick_by_author(self, author):
        try:
            return self.pick_set.filter(author=author).latest('timestamp')
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
        
    def __unicode__(self):
        return "{} at {}".format(self.away_team, self.home_team)
        

class Pick(models.Model):
    ''' A user's prediction of who will win a game.
    '''
    author = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    winner = models.ForeignKey(Team)
    
    timestamp = models.DateTimeField(default=timezone.now())
    
    def __unicode__(self):
        return str(self.winner.name)    
