import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from epicsrec import model, forms
from epicsrec.model import meta
from epicsrec.lib.scrape_teams import scrape_teams
from epicsrec.model.recomender import dbRecomender

from epicsrec.lib.base import BaseController, render
from formalchemy.ext.pylons.admin import FormAlchemyAdminController
from collections import defaultdict

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn

log = logging.getLogger(__name__)

class AdminController(BaseController):

    def index(self):
       return self.view_controlls()

    @authorize(ValidAuthKitUser())
    def view_controlls(self):
        c.default_scrape_url = "http://engineering.purdue.edu/EPICS/Projects/Teams/"
        c.formatted_majors = ""
        for school in meta.Session.query(model.Category).filter(model.Category.name != 'team'):
            c.formatted_majors += school.name + '\n'
            c.formatted_majors += '\n'.join(m.name for m in school.members)
            c.formatted_majors += '\n'

        return render('update_teams.mak')

    @authorize(ValidAuthKitUser())
    def scrape_teams(self):
        team_category = meta.Session.query(model.Category).filter_by(name='team').first()
        new_teams = scrape_teams()
        if team_category:
            old_teams = team_category.members
        else:
            team_category = model.Category()
            team_category.name = 'team'
            meta.Session.add(team_category)
            old_teams = []
        team_aliases = {}
        for team in old_teams:
            team_aliases[team.name] = team
            for alias in team.aliases:
                team_aliases[alias] = team
        for team in new_teams:
            if team.abbr in team_aliases:
                new_team = team_aliases[team.abbr]
            else:
                new_team = model.Suggestable()
                new_team.name = team.abbr
                new_team.category = team_category

            new_team.long_name = team.name
            new_team.link = team.link
            new_team.html = unicode(team.html)
            new_team.picture_path = team.picture
            new_team.description = team.info
            meta.Session.add(new_team)
        meta.Session.commit()
        return "Teams updated successfully."

    @authorize(ValidAuthKitUser())
    def parse_majors(self):
        print request.POST
        majors_text = request.POST.getone('majors')
        print repr(majors_text)
        majors_text = majors_text.replace('\r','')
        for school in majors_text.split('\n\n'):
            school_bits = school.split('\n')
            school_name = school_bits[0]
            majors = school_bits[1:]

            school_category = meta.Session.query(model.Category).filter_by(name=school_name).first()
            if not school_category:
                school_category = model.Category()
                school_category.name = school_name
                meta.Session.add(school_category)
            old_majors = [ m.name for m in school_category.members]

            for major in majors:
                if major not in old_majors:
                    major_suggestable = model.Suggestable()
                    major_suggestable.name = major
                    major_suggestable.category = school_category
                    meta.Session.add(major_suggestable)
            meta.Session.commit()
        return "Majors updated successfully"

    @authorize(ValidAuthKitUser())
    def recompute_top_choices(self):
        rec = dbRecomender()
        rec.recompute_top_choices()
        return "Successfully recomputed top choices"

    @authorize(ValidAuthKitUser())
    def parse_choices(self):
        known_names = {}
        if 'unknown_aliases' in session:
            for unknown_alias in session['unknown_aliases']:
                if unknown_alias in request.POST: 
                    if request.POST.getone(unknown_alias) == '':
                        known_names[unknown_alias] = None
                        continue
                    new_alias = model.Alias()
                    new_alias.name = unknown_alias
                    new_alias.refers_to_id = request.POST[unknown_alias]
                    print "uk: %s; id: %s " % (unknown_alias, request.POST[unknown_alias])
                    meta.Session.add(new_alias)
            meta.Session.commit()

        if 'choices' in request.POST:        
            choices_lines = request.POST.getone('choices').replace('\r','')
            choices_lines = choices_lines.split('\n')
        elif 'lines_to_parse' in session:
            choices_lines = session['lines_to_parse']
        else:
            return "Nothing to parse."

        rec = dbRecomender()
        known_names = {}
        c.categories = defaultdict(list)
        for category in meta.Session.query(model.Category):
            for item in category.members:
                known_names[item.name] = item.id
                c.categories[category].append(item)

        for item in meta.Session.query(model.Alias):
            known_names[item.name] = item.refers_to.id

        c.unknown_aliases = set()
        unknown_lines = []
        for line in choices_lines:
            line_choices = []
            unknown_line_aliases = set()
            for item in line.split():
                if item in known_names:
                    if known_names[item] == None:
                        continue
                    line_choices.append(known_names[item])
                else:
                    unknown_line_aliases.add(item)
            if unknown_line_aliases:
                c.unknown_aliases = c.unknown_aliases.union( unknown_line_aliases )
                unknown_lines.append(line)
            else:
                rec.add_row(line_choices)
        if c.unknown_aliases:
            session['lines_to_parse'] = unknown_lines
            session['unknown_aliases'] = c.unknown_aliases
            session.save()
            return( render('add_aliases.mak') )
        else:
            return( "Choices Updated." )

    def update_available(self):
        if 'selected' in request.POST:
            selected = request.POST.getone('selected')
            availables = defaultdict(list)
            for selection in (s for s in selected.split(';') if s):
                major,team = map(int,selection.split(','))
                availables[major].append(team)
            schools = meta.Session.query(model.Category).filter(model.Category.name != 'team')
            for major, choices in availables.iteritems():
                suggestable = meta.Session.query(model.Suggestable).filter_by(id=major).first()
                suggestable.available_choices = [ model.AvailableChoice(team) for team in choices ]
                meta.Session.add(suggestable)
                print '\n\n################################'
                print suggestable
                print suggestable.available_choices
            meta.Session.commit()
            return "Update Successful"
        else:
         
            c.teams = meta.Session.query(model.Category).filter(model.Category.name == 'team').first().members
            c.teams.sort(key=lambda s:s.name)
            c.schools =  meta.Session.query(model.Category).filter(model.Category.name != 'team')
            return render('update_available.mak')
