'''
Created on Jul 31, 2015

@author: TDARSEY
'''

from fixture import Fixture, FixtureObject, ValidationError

from datetime import datetime


class GameObject(FixtureObject):
    model = 'picker.game'
    required_fields = ["away_team", "home_team", "week", "season"]
    field_names = required_fields + ["kickoff_time", "location"]


class TeamObject(FixtureObject):
    model = 'picker.team'
    required_fields = ["name"]
    field_names = required_fields + []


class CGBSFixture(Fixture):
    
    def teamExists(self, name):
        
        self.makeSureObjectTypeExists('Team')
        
        for team in self.objects['Team']:
            if team['name'] == name:
                return True
        return False

    def getTeam(self, name):
        # if the team exists, return that team object
        # Otherwise, raise error
        for team in self.objects['Team']:
            if team['name'] == name:
                return team

        return ValueError(name)
        


