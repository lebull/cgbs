import os

from cgbsfixture import CGBSFixture, TeamObject, GameObject

from reader import CSVReader

from datetime import datetime, date, time

os.path.dirname(os.path.abspath(__file__))


source_file = os.getcwd() + '/season.csv'
dest_file = '/home/ubuntu/workspace/fixtures/ncaa_fb_2015.json'

myReader = CSVReader(source_file, season=1)
myReader.process()
myReader.save(dest_file)