"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from epicsrec.model import meta

import time

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine

interactions_table = sa.Table("interactions",meta.metadata,
        sa.Column("id",       sa.types.Integer,     primary_key=True),
        sa.Column("sid_hash", sa.types.String(100), nullable=False),
        sa.Column("timestamp",sa.types.Integer,     nullable=False)
        )

suggestions_table = sa.Table("suggestions",meta.metadata,
        sa.Column("id",       sa.types.Integer,     primary_key=True),
        sa.Column("low_choice_id",     sa.types.Integer,     sa.ForeignKey('suggestables.id')),
        sa.Column("high_choice_id",    sa.types.Integer,     sa.ForeignKey('suggestables.id')),
        sa.Column("weight",   sa.types.Integer,     nullable=False),
        sa.Column("timestamp",sa.types.Integer,     nullable=False)
        )

suggestables_table = sa.Table("suggestables",meta.metadata,
        sa.Column("id",       sa.types.Integer,     primary_key=True),
        sa.Column("name",     sa.types.String(100), nullable=True),
        sa.Column("categoty_id", sa.types.String(100), sa.ForeignKey('categories.id')),
        sa.Column("weight",   sa.types.Integer,     nullable=False),
        sa.Column("timestamp",sa.types.Integer,     nullable=False)
        )

aliases_table = sa.Table("aliases",meta.metadata,
        sa.Column("name",     sa.types.String(100), nullable=True),
        sa.Column("refers_to_id",     sa.types.Integer,     sa.ForeignKey('suggestables.id')),
        )

categories_table = sa.Table("categories",meta.metadata,
        sa.Column("id",       sa.types.Integer,     primary_key=True),
        sa.Column("name",     sa.types.String(100), nullable=True),
        sa.Column("is_recomendable",     sa.types.Boolean),
        )

suggestables_sessions_table = sa.Table("suggestable_session",meta.metadata,
        sa.Column("suggestable_id", sa.types.Integer, sa.ForeignKey('suggestables.id')),
        sa.Column("suggestion_id", sa.types.Integer, sa.ForeignKey('interactions.id'))
        )


class Category(object): pass

class Alias(object): pass

class Suggestable(object):
    def __init__(self,name):
        self.name = name
        self.weight = 0
        self.timestamp = int(time.time())
    def __repr__(self):
        return "<suggestable id=%s, name=%s, weight=%s>"%(self.id,self.name,self.weight)

class Suggestion(object):
    def __init__(self,item1,item2):
        if item1.id > item2.id:
            high, low = item1, item2
        else:
            high, low = item2, item1
        self.low_choice = low
        self.high_choice = high
        self.timestamp = int(time.time())
        self.weight = 1
    def __repr__(self):
        return "<suggestion high=%s low=%s weight=%s>" % (self.high_choice.name, self.low_choice.name, self.weight)

class Interaction(object):
    def __init__(self,sid_hash):
        self.sid_hash = sid_hash
        self.timestamp = int(time.time())


orm.mapper(Category, categories_table)
orm.mapper(Alias, aliases_table, properties={
    'refers_to': sa.orm.relation(Suggestable)
    })
orm.mapper(Suggestable, suggestables_table, properties={
    'category': sa.orm.relation(Category, backref='members')
    })
orm.mapper(Interaction, interactions_table, properties={
    'choices': sa.orm.relation(Suggestable, secondary=suggestables_sessions_table, backref='chosen_by')
    })
orm.mapper(Suggestion, suggestions_table, properties={
    'low_choice': sa.orm.relation(
        Suggestable, 
        primaryjoin=suggestions_table.c.low_choice_id==suggestables_table.c.id
        ),
    'high_choice': sa.orm.relation(
        Suggestable, 
        primaryjoin=suggestions_table.c.high_choice_id==suggestables_table.c.id
        )
    })



## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
