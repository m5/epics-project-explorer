from __future__ import division
from epicsrec import model
from epicsrec.model.meta import Session
from sqlalchemy import and_, or_
import os
from collections import defaultdict
from operator import itemgetter

def debug_print(item):
    print "##########################"
    print item
    print "##########################"

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
        debug_print("Adding %s to %s" % (", ".join(map(str,relations)),item))
        result = Session.query(model.Suggestable).filter_by(id=item)
        if (result.count() > 0):
            item_suggestable = result.first()
        else:
            return

        item_suggestable.weight += weight
        Session.add(item_suggestable)

        for relation in relations:
            if (relation == item):
                continue

            result = Session.query(model.Suggestable).filter_by(id=relation)
            relation_suggestable = result.first()
            if not relation_suggestable: continue

            results = Session.query(model.Suggestion).filter(
                    or_(
                        and_( model.Suggestion.high_choice_id == relation_suggestable.id,
                              model.Suggestion.low_choice_id == item_suggestable.id
                              ),
                        and_( model.Suggestion.high_choice_id == item_suggestable.id,
                              model.Suggestion.low_choice_id == relation_suggestable.id
                              )
                        )
                    )
            if (results.count() > 0):
                suggestion = results.first()
                suggestion.weight += weight
                if suggestion.weight <= 0:
                    Session.delete(suggestion)
                else:
                    Session.add(suggestion)
            else:
                suggestion = model.Suggestion(item_suggestable,relation_suggestable)
                Session.add(suggestion)
            Session.commit()

    def remove(self,item,relations,weight=1):
        self.add(item,relations,-weight)

    def add_row(self,items):
        while items:
            self.add(items.pop(),items)

    def remove_row(self,items):
        for i in range(len(items)):
            self.remove(items[i],items)

    def modify_by_sid(self, sid_hash, item, weight):
        results = Session.query(model.Interaction).filter_by(sid_hash=sid_hash)
        if (results.count() != 0):
            interaction = results.first()
        else:
            interaction = model.Interaction(sid_hash)
        choices = map(lambda x: x.id, interaction.choices)
        if interaction.choices:
            self.add(item,choices,weight)
        item_suggestable = Session.query(model.Suggestable).filter_by(id=item).first()
        if item_suggestable and weight > 0:
            interaction.choices.append(item_suggestable)
        elif weight < 0:
            interaction.choices.remove(item_suggestable)

        Session.add(interaction)
        Session.commit()

    def add_by_sid(self,sid_hash, item):
        self.modify_by_sid(sid_hash, item, 1)

    def remove_by_sid(self,sid_hash, item):
        self.modify_by_sid(sid_hash, item, -1)

    def recomend_by_sid(self,sid_hash):
        interaction = Session.query(model.Interaction).filter_by(sid_hash=sid_hash).first()
        if interaction:
            choices = map(lambda x: x.id, interaction.choices)
        if ( len(choices) > 0 ):
            return self.recomend(choices)
        else:
            return []

    def recomend(self,items):
        recomendations = defaultdict(lambda:0)
        for item in items:
            suggestable = Session.query(model.Suggestable).filter_by(id=item).first()
            debug_print(suggestable)
            if not suggestable: continue
            for top_choice in suggestable.top_choices:
                recomendations[top_choice.choice_id] += top_choice.weight
        rec_list = sorted(recomendations.iteritems(), key=itemgetter(1), reverse=True)
        debug_print(rec_list)
        return [ rec for rec in rec_list if rec[0] not in items ][:3]
                

    def deep_recomend(self,items):
        recomendations = {}
        for item in items:
            if not item: continue
            suggestions = Session.query(model.Suggestion).filter(
                    or_(
                        model.Suggestion.high_choice_id==item, 
                        model.Suggestion.low_choice_id==item
                        )
                    )
            for suggestion in suggestions.all():
                high = suggestion.high_choice
                low = suggestion.low_choice
                rec = high if high.id != item else low
                if rec.category.name != 'team':
                    continue

                results = Session.query(model.Suggestable).filter_by(id=rec)

                weight = rec.weight or 1

                if rec.id in recomendations.keys():
                    recomendations[rec.id] += suggestion.weight/weight
                else:
                    recomendations[rec.id] = suggestion.weight/weight

        rec_list = [ (x,y/len(items)) for x,y in recomendations.items()]
        rec_list.sort(key=lambda x:-x[1])
        return filter(lambda x: x[0] not in items, rec_list)

    def recompute_top_choices(self):
        for suggestable in Session.query(model.Suggestable):
            debug_print( suggestable )
            suggestable.top_choices = []
            Session.add(suggestable) 

            suggestions = Session.query(model.Suggestion).filter(
                    or_(
                        model.Suggestion.high_choice_id==suggestable.id, 
                        model.Suggestion.low_choice_id==suggestable.id
                        )
                    )
            recomendations = defaultdict(lambda:0)
            for suggestion in suggestions:
                high = suggestion.high_choice
                low = suggestion.low_choice
                rec = high if high.id != suggestable.id else low
                if rec.category.name != 'team':
                    continue

                weight = rec.weight or 1
                recomendations[rec.id] += suggestion.weight/weight

            rec_list = [ (x,y) for x,y in recomendations.items()]
            rec_list.sort(key=lambda x:-x[1])
            for rec in rec_list[:5]:
                top_choice = model.TopChoice()
                top_choice.chooser = suggestable
                top_choice.choice_id = rec[0]
                top_choice.weight = rec[1]
                Session.add(top_choice)
        Session.commit()
