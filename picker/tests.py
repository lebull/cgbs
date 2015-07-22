from django.test import TestCase

from picker.models import Season, JoinRequest, Game, Pick, Team
from django.contrib.auth.models import AnonymousUser, User

from django.core.exceptions import ValidationError



class PickTestCase(TestCase):
    def setUp(self):
        self.season = Season.objects.create(name='TestSeason')
        
        self.user1 = User.objects.create_user(username='user1')
        self.user2 = User.objects.create_user(username='user2')
        
        self.team1 = Team.objects.create(name = "TestTeam1")
        self.team2 = Team.objects.create(name = "TestTeam2")
        self.team3 = Team.objects.create(name = "TestTeam3")
        
        self.game1 = Game.objects.create(season = self.season, away_team = self.team1, home_team = self.team2, week=1)
        self.game2 = Game.objects.create(season = self.season, away_team = self.team2, home_team = self.team3, week=2)
        self.game3 = Game.objects.create(season = self.season, away_team = self.team3, home_team = self.team1, week=3)
        
    def test_pick(self):
        
        game = Game.objects.get(id=self.game1.id)
        pick = game.pick(author=self.user1, winner=self.team1)
        
        #Correct winner was picked
        self.assertEqual(pick.winner.id, self.team1.id)
        
        #Latest pick is what the user picked last
        self.assertEqual(game.get_pick_by_author(author=self.user1), pick)
        

    def test_repick(self):
        
        game = Game.objects.get(id=self.game1.id)
        irrelevent_game = Game.objects.get(id=self.game2.id)
        pick = game.pick(author=self.user1, winner=self.team2)
        irrelevent_game.pick(author=self.user1, winner=self.team3)

        #Latest pick is what the user picked last
        self.assertEqual(game.get_pick_by_author(author=self.user1), pick)
        
    # def test_pick_bad_team(self):
    #     game = Game.objects.get(id=self.game1.id)
    #     pick = game.pick(author=self.user1, winner=self.team3)
    #     print pick.winner
    #     with self.assertRaises(ValidationError):
    #         pick = game.pick(author=self.user1, winner=self.team3)
            
    
            
class SeasonTestCase(TestCase):
    def setUp(self):
        
        self.season = Season.objects.create(name='TestSeason')
        
        self.user1 = User.objects.create_user(username='user1')
        self.user2 = User.objects.create_user(username='user2')
        
    def test_request_season(self):
        self.season.request_user_to_join(self.user1)
        
        
    
        
            

# Create your tests here.
