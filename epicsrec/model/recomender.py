from __future__ import division
from epicsrec import model
from epicsrec.model.meta import Session
from sqlalchemy import and_, or_
import os

class dbRecomender:
    def __init__(self):
        pass
    
    def load_data(self,dataname,identifiers,weight=1):
        if os.path.exists(dataname):
            data_file = open(dataname,'r').read()
        else:
            return

        data_rows = data_file.split('\n')
        for row in data_rows: 
            good_row = []
            cols = row.split()
            for col in cols:
                if col.lower() in identifiers:
                    self.add(col.lower(),good_row,weight)
                    good_row.append(col.lower() )


    def add(self,item,relations,weight=1):
        result = Session.query(model.Suggestable).filter_by(item=item)
        if (result.count() > 0):
            suggestable = result.first()
            suggestable.weight += weight
            if suggestable.weight <= 0:
                Session.delete(suggestable)
            else:
                Session.add(suggestable)
        else:
            suggestable = model.Suggestable(item)
            Session.add(suggestable)

        for relation in relations:
            if (relation == item):
                continue

            results = Session.query(model.Rec).filter(
                    or_(
                        and_( model.Rec.item == relation,
                              model.Rec.rec  == item    ),
                        and_( model.Rec.item == item,
                              model.Rec.rec  == relation)
                        )
                    )
            if (results.count() > 0):
                rec = results.first()
                rec.weight += weight
                if rec.weight <= 0:
                    Session.delete(rec)
                else:
                    Session.add(rec)
            else:
                rec = model.Rec(item,relation)
                Session.add(rec)
        Session.commit()

    def remove(self,item,relations,weight=1):
        self.add(item,relations,-weight)

    def add_row(self,items):
        for i in range(len(items)):
            self.add(items[i],items)

    def add_row(self,items):
        for i in range(len(items)):
            self.remove(items[i],items)

    def add_by_sid(self,sid_hash, item):
        results = Session.query(model.Like).filter_by(sid_hash=sid_hash)
        relations = []
        if (results.count() > 0):
            for result in results:
               relations.append(result.item)
        self.add(item,relations)
        like = model.Like(sid_hash,item)
        Session.add(like)
        Session.commit()

    def remove_by_sid(self,sid_hash, item):
        results = Session.query(model.Like).filter_by(sid_hash=sid_hash)
        if (results.count() > 0):
            relations = []
            for result in results:
                relations.append(result.item)
            self.remove(item,relations)
        unliked = Session.query(model.Like).filter_by(sid_hash=sid_hash,item=item).first()
        Session.delete(unliked)
        Session.commit()

    def recomend_by_sid(self,sid_hash):
        results = Session.query(model.Like).filter_by(sid_hash=sid_hash)
        likes = []
        if (results.count() > 0):
            for result in results:
                likes.append(result.item)
        if ( len(likes) > 0 ):
            return self.recomend(likes)
        else:
            return []

    def recomend(self,items):
        recomendations = {}
        rw = {}
        for item in items:
            results = Session.query(model.Rec).filter(or_(model.Rec.item==item, model.Rec.rec==item))
            for result in results:
                if result.rec != item:
                    rec = result.rec
                else:
                    rec = result.item

                results = Session.query(model.Suggestable).filter_by(item=rec)
                if ( results.count() > 0):
                    weight = results.first().weight

                if rec in recomendations.keys():
                    recomendations[rec] += result.weight/weight
                else:
                    recomendations[rec] = result.weight/weight
                    rw[rec] = weight

        rec_list = recomendations.items()
        rec_list.sort(key=lambda x:-x[1])
        return rec_list
