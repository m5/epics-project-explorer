import logging
import time
import hashlib
import math
import glob
from BeautifulSoup import BeautifulSoup
import shutil

from pylons import request, response, session, tmpl_context as c
from pylons import app_globals as g
from pylons.controllers.util import abort, redirect_to
from epicsrec import model
from epicsrec.model.meta import Session
from epicsrec.model.recomender import dbRecomender
from epicsrec.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ChooseController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/choose.mako')
        # or, return a response
        print request.environ.get('REMOTE_ADDR') 
        sid = request.environ.get('REMOTE_ADDR') + str(time.time())
        c.majors = {}
        c.teams = []
        for item in Session.query(model.Category).all():
            if item.name == 'team':
                c.teams = item.members
            else:
                c.majors[item.name] = item.members
                for member in item.members:
                    print member
        print c.categories
        c.sid_hash = hashlib.md5( sid ).hexdigest()
        #soup =  BeautifulSoup(render('/rec.mak'))
        return render('/rec.mak')

    def doit(self):
        rec = dbRecomender()
        for file in glob.glob('./toimport/*.recdat'):
            rec.load_data(file,g.identifiers,4)
            shutil.move(file,'./imported/')
        return "import successful"


    def ajax(self):
        selected = request.POST.getone('selected').lower()
        deselected = request.POST.getone('deselected').lower()
        print "---!!!###!!!---"
        print selected
        print deselected
        sid_hash = request.POST.getone('sid_hash')
        recomender = dbRecomender()
        if selected:
            recomender.add_by_sid(sid_hash,selected)
        if deselected:
            print "$$$$$$$$$$$\ndeselecting%s\n$$$$$$$$$$$$$$$" % deselected
            recomender.remove_by_sid(sid_hash,deselected)
        recomendations = recomender.recomend_by_sid(sid_hash)
        c.recs = map(lambda x: x[0], recomendations)
        c.avail = []
        for selection in Session.query(model.Interaction).filter_by(sid_hash=sid_hash).first().choices:
            for avail in selection.available_choices:
                if avail.choice.id not in c.recs:
                    c.avail.append(avail.choice.id)
        c.recs = filter(lambda x: x in c.avail, c.recs)
        c.recs = c.recs[:3]
        response.content_type = 'text/xml'
        r = render('/xml_recs.mak')
        print r
        return r

    def info(self, id):
        team = Session.query(model.Suggestable).filter_by(id=id).first()
        if team:
            return team.html
        else:
            return ''

    def dict_ajax(self):
        selected = request.POST.getone('selected')
        deselected = request.POST.getone('deselected')
        sid_hash = request.POST.getone('sid_hash')
        if selected:
            like = model.Like(sid_hash,selected)
            Session.save(like)
            Session.commit()
        if deselected:
            unliked = Session.query(model.Like).filter_by(sid_hash=sid_hash,item=deselected).first()
            print unliked
            Session.delete(unliked)
            Session.commit()
        all_likes = []
        for row in Session.query(model.Like.item).filter_by(sid_hash=sid_hash):
           all_likes.append(row[0]); 
        print all_likes
        suggestions = []
        c.recs = []
        if (len(all_likes) > 0):
            for suggestion in g.rec.suggest(all_likes):
                if suggestion[0] in g.teams:
                    suggestions.append(suggestion[0])
            c.recs = suggestions[:3]
        return render('/xml_recs.mak')

