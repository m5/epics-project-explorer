"""The application's Globals object"""
import recomender
import major_map
import re
import glob
from epicsrec.model.recomender import dbRecomender
import shutil

class Globals(object):

    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable
        """
        #self.teams = open('teams.txt','r').read().split()
        schools = open('majors.txt','r').read().split('\n\n')
        self.majors = {}
        self.major_names = []
        for school in schools:
            self.majors[ school.split()[0] ] = school.split()[1:]
            for major in school.split()[1:]:
                name = school.split()[0]+'-'+major
                self.major_names.append(name.lower())
        #self.rec = recomender.Recomender()
        #self.rec.load('oldrecs.dump')
        p = re.compile(r".*\((.*)\)")
