from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1247729137.1459179
_template_filename='/home/mfivecoa/purdue/epics/EpicsRec/epicsrec/templates/xml_recs.mak'
_template_uri='/xml_recs.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<response>\n')
        # SOURCE LINE 2
        for rec in c.recs:
            # SOURCE LINE 3
            __M_writer(u'\t<rec name="')
            __M_writer(escape(rec))
            __M_writer(u'">')
            __M_writer(escape(rec))
            __M_writer(u'</rec>\n')
        # SOURCE LINE 5
        __M_writer(u'</response>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


