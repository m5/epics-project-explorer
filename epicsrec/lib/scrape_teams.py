import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import os
import cPickle


class Team():
    abbr = ''
    link = ''
    name = ''
    info = ''
    html = ''
    soup = ''
    def __init__(self):
        pass
    def __repr__(self):
        return self.abbr
    def __str__(self):
        return self.abbr

def load_teams():
    cache = 'team_cache.pkl'
    if os.path.exists(cache):
        return cPickle.load( open(cache,'r') )
    else:
        teams = scrape_teams()
        cPickle.dump( teams, open(cache,'w') )
        return teams
    
def good_abbr(abbr):
    r = {'voss@pace':'voss'}
    abbr = abbr.lower().strip()
    print abbr
    if abbr in r.keys():
        return r[abbr]
    else:
        return abbr

def scrape_teams():
    base_url = "http://engineering.purdue.edu/EPICS/Projects/Teams/"
    page = urllib2.urlopen(base_url)
    soup = BeautifulSoup(page)
    team_bits = soup.find(id="teams").findAll(re.compile('dt|dd'))
    team_list = [ [team_bits[i],team_bits[i+1]] for i in range(0,len(team_bits),2)]
    teams = []
    paren_match = re.compile(r".*\((.*)\)")
    for team in team_list:
        t = Team()
        abbr = paren_match.match(team[0].a.string).group(1)
        if abbr:
            t.abbr = good_abbr( abbr )
        link = team[0].a['href']
        if link:
            t.link = base_url + link
        t.name = team[0].a.string
        t.info = team[1].string
        if t.abbr:
            teams.append(t)
        print t.link
        try:html = urllib2.urlopen(t.link) 
        except (URLError,HTTPError) as e:
            print e
            continue
        t.soup = BeautifulSoup( html )
        img_src = '/cache/' + t.abbr + '.jpg'
        img = t.soup.find('ul','team_info').find('img')
        if img:
            img_path = 'epicsrec/public'+img_src
            if not os.path.exists(img_path):
                urllib.urlretrieve(img['src'], img_path)
                img['src'] = img_src
    return teams


    
