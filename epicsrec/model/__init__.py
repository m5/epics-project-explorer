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

interactions_table = sa.Table("likes",meta.metadata,
        sa.Column("id",       sa.types.Integer,     primary_key=True),
        sa.Column("sid_hash", sa.types.String(100), nullable=False),
        sa.Column("timestamp",sa.types.Integer,     nullable=False)
        )

suggestions_table = sa.Table("suggestions",meta.metadata,
        sa.Column("id",       sa.types.Integer,     primary_key=True),
        sa.Column("chosen",   sa.types.Integer,     sa.ForeignKey('suggestables.id')),
        sa.Column("suggested",sa.types.Integer,     sa.ForeignKey('suggestables.id')),
        sa.Column("weight",   sa.types.Integer,     nullable=False),
        sa.Column("timestamp",sa.types.Integer,     nullable=False)
        )

suggestables_table = sa.Table("suggestables",meta.metadata,
        sa.Column("id",       sa.types.Integer,     primary_key=True),
        sa.Column("name",     sa.types.String(100), nullable=False),
        sa.Column("categoty", sa.types.String(100), nullable=False),
        sa.Column("weight",   sa.types.Integer,     nullable=False),
        sa.Column("timestamp",sa.types.Integer,     nullable=False)
        )

suggestables_sessions_table = sa.Table("suggestable_session",meta.metadata,
        sa.Column("suggestable_id", sa.types.Integer, sa.ForeignKey('suggestables.id')),
        sa.Column("suggestion_id", sa.types.Integer, sa.ForeignKey('suggestions.id'))
        )

class Suggestable(object):
    def __init__(self,item):
        self.item = item
        self.weight = 1
        self.timestamp = int(time.time())

class Suggestion(object):
    def __init__(self,item,rec):
        self.item = item
        self.rec = rec
        self.timestamp = int(time.time())
        self.weight = 1

class Interaction(object):
    def __init__(self,sid_hash):
        self.sid_hash = sid_hash
        self.timestamp = int(time.time())
        
orm.mapper(Interaction, interactions_table, properties={
    'choices': sa.relation(Suggestable, secondary=suggestables_sessions_table, backref='chosen_by')
    })
orm.mapper(Suggestable, suggestables_table)
orm.mapper(Suggestion, suggestions_table)



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
