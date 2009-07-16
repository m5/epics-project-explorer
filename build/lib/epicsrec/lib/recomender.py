from __future__ import division
import cPickle

def make_dict(s):
    d = {}
    for row in s.split('\n'):
        row = row.strip()
        if ':' in row:
            pair = row.split(':')
            d[ pair[0] ] = pair[1]
    return d

def read_data(dataname):
    data_file = open(dataname,'r').read()
    data_rows = data_file.split('\n')
    dataray = []
    teams = open('teams.txt','r').read().split('\n')
    schools = open('majors.txt','r').read().split('\n\n')
    majors = []
    for school in schools:
        for major in school.split()[1:]:
            majors.append( school.split('\n')[0] + '-' + major ) 

    identifiers = []
    for identifier in majors+teams:
        identifiers.append(identifier.lower())

    for row in data_rows: 
        good_row = []
        cols = row.split()
        for col in cols:
            if col.lower() in identifiers:
                good_row.append(col.lower() )
        dataray.append( good_row )
    return dataray

def total_votes(dataray):
    totals = {}
    for row in dataray:
        for col in row:
            if col in totals.keys():
                totals[ col ] += 1
            else:
                totals[ col ]  = 1
    del totals['']
    return totals

def average_score(totals):
    sum = 0
    for key in totals.keys():
       sum += totals[key]
    return sum/len(totals.keys())

class Recomender:
    def __init__(self):
        self.pairs = {}
        self.totals = {}

    def add(self,row):
        for primary in row:

            if primary not in self.totals.keys():
                self.totals[primary] = 0
            self.totals[primary] += 1

            if primary not in self.pairs.keys():
                self.pairs[primary] = {}
            for secondary in row:
                if secondary == primary:
                    continue

                if secondary not in self.pairs[primary].keys():
                    self.pairs[primary][secondary] = 1
                else:
                    self.pairs[primary][secondary] += 1

    def suggest(self,row,number=-1):
        matches = {}
        for item in row:
            item = item.lower()
            if item not in self.pairs.keys():
                continue
            for match in self.pairs[item].keys():
                if match not in matches:
                    matches[match] = 0
                matches[match] += self.pairs[item][match]/self.totals[match] 

        match_list = matches.items()
        match_list.sort(key=lambda x:x[1])
        if number > len(match_list):
            return match_list[::-1]
        else:
            return match_list[number::-1]

    def save(self,filename):
        file = open(filename,'w')
        cPickle.dump( (self.pairs,self.totals), file )
        file.close()

    def load(self,filename):
        file = open(filename,'r')
        self.pairs, self.totals = cPickle.load(file)
        file.close()

def make_my_day():
    dataray = read_data('data.txt')
    rec = Recomender()
    for row in dataray:
        rec.add(row)
    return rec


if __name__ == '__main__':
    dataray = read_data('data.txt')
    print dataray
    totals = total_votes(dataray)
    keys = totals.keys()
    keys.sort()
    for key in keys:
        print key, totals[key] 

