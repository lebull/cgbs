'''
Created on Jul 28, 2015

@author: TDARSEY
'''

from string import lower

from cgbsfixture import TeamObject, GameObject, CGBSFixture
from fixture import Fixture, ValidationError

from datetime import datetime


class FormatError(Exception):
    pass


class CSVReader(object):

    '''Read and process a CSV file provided by Zach.

    The file should have a header line naming which variables the data rows
    correspond with.
    '''

    def __init__(self, src_filepath, season):
        self.src_filepath = src_filepath
        self.season = season
        
        self.header = []
        self.fixture = CGBSFixture()

    def process(self):
        '''Create a fixture from file contents'''
        with open(self.src_filepath) as myfile:
            file_contents = myfile.read()

        csv_lines = file_contents.split('\n')

        # Set header values by the first line
        self.getHeaderValues(csv_lines[0])

        # Loop through each line.
        # If line is valid, Take values and add it to the fixture
        for line in csv_lines[1:]:
            self.processCSVLine(line)
            # TODO: else, warn of an invalid line.

    def validateLine(self, split_line):
        '''Is the line valid?

        Returns true if the list of values match up with what the header
        said was coming.
        '''
        # Must be same size as header
        if len(split_line) != len(self.header):
            return False

        # If header[column] = None, then content[column] must equal None

        for column_num in range(len(self.header)):
            if self.header[column_num] is None\
                    and split_line[column_num] is None:
                return False

        return True

    def processCSVLine(self, line):
        '''Save a single line into the local fixture
        '''

        line_values = line.split(',')

        # Ignore if the line isn't valid
        if not self.validateLine(line_values):
            # TODO: Warn of Invalid Line
            return

        # Arguments used to add a game to the fixture
        line_kwargs = {}

        # Pull the information from the line
        for column_num in range(len(self.header)):
            header = self.header[column_num]
            value = line_values[column_num]

            # TODO: if header is None and value is not None: #If we are mising
            #    a value
            #    raise FormatError("Error in {}".format(column_num))

            line_kwargs[header] = value

            # Make sure all required values are present
            if header in GameObject.required_fields and \
                    (value == None or value == ''):
                return

        # Convert game's teams to pks and add teams to fixture if not present.
        for which_team, team_name in {
            'away_team': line_kwargs['away_team'],
            'home_team': line_kwargs['home_team']
        }.iteritems():
            
            if not self.fixture.teamExists(team_name):
                
                try:
                    self.fixture.addObject(TeamObject(name=team_name))

                except ValidationError:
                    return

            line_kwargs[which_team] = self.fixture.getTeam(team_name).pk

        
        if line_kwargs['date'] not in [None, '']:
            
            # Convert the date and time to our datetime field.
            kickoff_date = datetime.strptime(
                str(line_kwargs['date']), '%m/%d/%Y'
            )
            
            line_kwargs['kickoff_time'] = str(
                datetime.strftime(kickoff_date, '%Y-%m-%d %H:%M:%S')
            )
            
        else:
            line_kwargs['kickoff_time'] = ''

        
        
        
        vestige_keys = []  # Values to be removed
        for key, value in line_kwargs.iteritems():
            
            # Remove anything not defined in the fixture
            if key not in GameObject.field_names:
                vestige_keys.append(key)
                
            # Remove any value that is none or empty string 
            elif value in [None, '']:
                vestige_keys.append(key)
            
        # Only because deleting from dicts in a loop is derp   
        for key in vestige_keys: 
            del line_kwargs[key]
            

        #And finally, add in our season argument
        line_kwargs['season'] = self.season
            
        #Try your thing and hope for the best
        try:
            self.fixture.addObject(GameObject(**line_kwargs))
        except ValidationError:
            print ("Invalid Line Skipped: {}".format(line))

    def getHeaderValues(self, line):
        ''' Set the order which the values will come in.
        '''
        
        line_values = line.split(',')
        
        #
        for value in line_values:
            if value == '':
                self.header.append(None)
            else:
                self.header.append(lower(value).replace(' ', '_'))

    def save(self, dest_filepath):
        '''Save the fixture.
        '''
        #TODO: Get the filename away from the fucking constructor.
        out_string = str(self.fixture.jsonEncode())
        out_string = out_string.replace("'", "\"")
        
        with open(dest_filepath, 'w+') as myFile:
            myFile.write(out_string)
