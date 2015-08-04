'''
Created on Jul 31, 2015

@author: TDARSEY
'''


class ValidationError(Exception):

    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(ValidationError, self).__init__(message)


class Fixture(object):

    def __init__(self, *args, **kwargs):
        self.objects = {}  # Dict of lists

    def _getNextValidPK(self, object_name):
        i = 1
        
        self.makeSureObjectTypeExists(object_name)
        
        for obj in self.objects[object_name]:
            if obj.pk != i:
                break
            i += 1
        return i
        
    def addObject(self, fixtureObject):
        '''Add a game to the fixture's list of games.

        :param str away_team: NAME of the away team.
        '''

        # If both the away team and home team are already in the fixture
        object_name = fixtureObject.getObjectName()

        #Get this new object's pk
        fixtureObject.pk = self._getNextValidPK(object_name)

        if fixtureObject.validate():
            
            #If the object type isn't in self.objects, add it.
            if object_name not in self.objects.keys():
                self.objects[object_name] = []
            
            #Add it
            self.objects[object_name].append(fixtureObject)
        else:
            raise ValidationError(fixtureObject)
            
    def makeSureObjectTypeExists(self, name):
        if name not in self.objects.keys():
            self.objects[name] = []
            
        

    def jsonEncode(self):

        json_object = []
        for object_type in self.objects.keys():
            json_object += [obj.getFixtureData()
                            for obj in self.objects[object_type]]

        return json_object


class FixtureObject(dict):

    model = 'object'
    field_names = []
    required_fields = []

    def __init__(self, pk=0, **kwargs):
        self.__initialised = False
        self.pk = pk

        super(FixtureObject, self).__init__(**kwargs)

    def validate(self):

        # Make sure all required keys are pesent
        for key in self.required_fields:
            if key not in self.keys():
                raise ValidationError("Missing Key {}".format(key))
            if key in self.required_fields and self[key] == "":
                raise ValidationError("Missing Required Value {}".format(key))
        return True

    def getFixtureData(self):

        self.validate()

        return_dict = {}
        return_dict['model'] = self.model
        return_dict['pk'] = self.pk
        return_dict['fields'] = self

        return return_dict
    
    def getObjectName(self):
        return self.__class__.__name__.replace('Object', '')
        

