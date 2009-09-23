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
            print "weight: ", item.item,
            print item.weight
            assert item.weight == 1

        items = []
        recs = []
        for item in Session.query(model.Rec).all():
            print "recs: ", item.item,
            print item.rec
            items.append(item.item)
            recs.append(item.rec)

        items.sort()
        recs.sort()
        print items
        print recs
        assert items == recs
