from epicsrec.tests import *
from epicsrec.model.recomender import dbRecomender
from epicsrec import model
from epicsrec.model.meta import Session

class TestModels(TestController):
    def test_add_one(self):
        rec = dbRecomender()
        rec.add(1,[])
        one = Session.query(model.Suggestable).filter_by(id=1).first()
        print one.weight
        assert one.weight == 1
        

    def test_add_several(self):
        rec = dbRecomender()
        rec.add_row([4,5,6])
        for item in Session.query(model.Suggestable).all():
            print "weight: ", item.name,
            print item.weight
            assert item.weight == 1

        high = []
        low = []
        for item in Session.query(model.Suggestion).all():
            print item
            print "high: ", item.high_choice_id,
            print "low:  ", item.low_choice_id
            high.append(item.high_choice)
            low.append(item.low_choice)
            assert not item.high_choice.id < item.low_choice.id

        high =  map(lambda x: int(x.id), high)
        low =  map(lambda x: int(x.id), low)
        high.sort()
        low.sort()
        print high
        print low
        assert high == [2,3,3]
        assert low == [1,1,2]

    def test_recomend(self):
        rec = dbRecomender()
        rec.add_row(['z','a','b','c','d'])
        rec.add_row(['z','a','b','d'])
        rec.add_row(['z','a'])

        s = {}
        for item in Session.query(model.Suggestable).all():
            print item
            s[item.name] = item.id

        for sug in Session.query(model.Suggestion).all():
            print sug
            
        recomendations = rec.recomend([s['z'],s['b']])
        print recomendations
        assert recomendations == [(1, 1.0), (5, 1.0), (3, 0.83333333333333326)] 
