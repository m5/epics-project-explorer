from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1255554272.8866861
_template_filename='/home/mfivecoa/src/pylons/epicsrec/epicsrec/templates/rec.mak'
_template_uri='/rec.mak'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['css_links', 'js_links', 'css', 'js']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        set = context.get('set', UNDEFINED)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n"http://www.w3.org/TR/html14/loose.tdt">\n<html>\n')
        # SOURCE LINE 5
        self.seen_css = set() 
        
        __M_writer(u'\n')
        # SOURCE LINE 6
        self.seen_js = set() 
        
        __M_writer(u'\n    <head>\n\t')
        # SOURCE LINE 8
        __M_writer(escape(self.css()))
        __M_writer(u'\n\t')
        # SOURCE LINE 9
        __M_writer(escape(self.js()))
        __M_writer(u'\n\t</head>\n\n\t')
        # SOURCE LINE 17
        __M_writer(u'\n\t')
        # SOURCE LINE 23
        __M_writer(u'\n\n\t')
        # SOURCE LINE 27
        __M_writer(u'\n\t')
        # SOURCE LINE 32
        __M_writer(u'\n\n\n    <body>\n\t\t<div id="container">\n\t\t<div id="majors_container">\n\t\t\t<dl id="schools" class="accordian">\n')
        # SOURCE LINE 39
        for school, majors in c.majors.items():
            # SOURCE LINE 40
            __M_writer(u"\t\t\t\t<a href='#'><dt>")
            __M_writer(escape(school.replace('_',' ')))
            __M_writer(u'</dt></a>\n\t\t\t\t<dd style="height: ')
            # SOURCE LINE 41
            __M_writer(escape(3+50*((4+len(majors)) // 5)))
            __M_writer(u'px;">\t\t\t\n')
            # SOURCE LINE 42
            for suggestable in majors:
                # SOURCE LINE 43
                __M_writer(u'\t\t\t\t\t\t<span name="')
                __M_writer(escape(suggestable.id))
                __M_writer(u'" class="button major ')
                __M_writer(escape(school))
                __M_writer(u'">\n\t\t\t\t\t\t\t<span class="button_label">')
                # SOURCE LINE 44
                __M_writer(escape(suggestable.name))
                __M_writer(u'</span>\n\t\t\t\t\t\t\t<span class="information">')
                # SOURCE LINE 45
                __M_writer(escape(school))
                __M_writer(u'</span>\n\t\t\t\t\t\t</span>\n')
            # SOURCE LINE 48
            __M_writer(u'\t\t\t\t</dd>\n')
        # SOURCE LINE 50
        __M_writer(u'\t\t\t</ul>\n\t\t</div>\n\t\t<div id="information">\n\t\t\t<h1>Epics Project Explorer</h1>\n\t\t</div>\n\t\t<div id="teams_container">\n')
        # SOURCE LINE 56
        for suggestable in c.teams:
            # SOURCE LINE 57
            __M_writer(u'           \t<span name="')
            __M_writer(escape(suggestable.id))
            __M_writer(u'" class="button team">\n\t\t\t\t<span class="button_label"name="')
            # SOURCE LINE 58
            __M_writer(escape(c.abbr))
            __M_writer(u'">\n\t\t\t\t\t')
            # SOURCE LINE 59
            __M_writer(escape(suggestable.name))
            __M_writer(u'\n\t\t\t\t</span>\n\t\t\t\t<span class="information" name="title">\n\t\t\t\t\t')
            # SOURCE LINE 62
            __M_writer(escape(suggestable.long_name))
            __M_writer(u'\n\t\t\t\t</span>\n\t\t\t\t<span class="information" name="description">\n\t\t\t\t\t')
            # SOURCE LINE 65
            __M_writer(escape(suggestable.description))
            __M_writer(u'\n\t\t\t\t</span>\n\t\t\t\t<a class="information" href="')
            # SOURCE LINE 67
            __M_writer(escape(suggestable.link))
            __M_writer(u'"></a>\n\t\t</span>\n')
        # SOURCE LINE 70
        __M_writer(u'\t\t</div>\n\t\t<span id="description" class="popup"></span>\n\t\t<div id="tutorial">Choose your school...</div>\n\t\t</div>\n\t<input type="hidden" id="sid_hash" value="')
        # SOURCE LINE 74
        __M_writer(escape(c.sid_hash))
        __M_writer(u'">\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_links(context,path,media=''):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'\n')
        # SOURCE LINE 13
        if path not in self.seen_css:
            # SOURCE LINE 14
            __M_writer(u'\t\t\t<link rel="stylesheet" type="text/css" href="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" media="')
            __M_writer(escape(media))
            __M_writer(u'" >\n')
        # SOURCE LINE 16
        __M_writer(u'\t\t')
        self.seen_css.add(path) 
        
        __M_writer(u'\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_links(context,path):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(u'\n')
        # SOURCE LINE 19
        if path not in self.seen_js:
            # SOURCE LINE 20
            __M_writer(u'\t\t\t<script type="text/javascript" src="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" ></script>\n')
        # SOURCE LINE 22
        __M_writer(u'\t\t')
        self.seen_js.add(path) 
        
        __M_writer(u'\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css(context):
    context.caller_stack._push_frame()
    try:
        def css_links(path,media=''):
            return render_css_links(context,path,media)
        __M_writer = context.writer()
        # SOURCE LINE 25
        __M_writer(u'\n\t\t')
        # SOURCE LINE 26
        __M_writer(escape(css_links('/css/rec.css', 'screen')))
        __M_writer(u'\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        def js_links(path):
            return render_js_links(context,path)
        __M_writer = context.writer()
        # SOURCE LINE 28
        __M_writer(u'\n\t\t')
        # SOURCE LINE 29
        __M_writer(escape(js_links('/js/jquery-1.2.6.pack.js')))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 30
        __M_writer(escape(js_links('/js/jquery.color.js')))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 31
        __M_writer(escape(js_links('/js/buttons.js')))
        __M_writer(u'\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


