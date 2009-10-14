from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1255549344.218482
_template_filename='/home/mfivecoa/src/pylons/epicsrec/epicsrec/templates/update_teams.mak'
_template_uri='update_teams.mak'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n"http://www.w3.org/TR/html14/loose.tdt">\n<html>\n')
        # SOURCE LINE 4
        self.seen_css = set() 
        
        __M_writer(u'\n')
        # SOURCE LINE 5
        self.seen_js = set() 
        
        __M_writer(u'\n    <head>\n\t')
        # SOURCE LINE 7
        __M_writer(escape(self.css()))
        __M_writer(u'\n\t')
        # SOURCE LINE 8
        __M_writer(escape(self.js()))
        __M_writer(u'\n\t</head>\n\n\t')
        # SOURCE LINE 16
        __M_writer(u'\n\t')
        # SOURCE LINE 22
        __M_writer(u'\n\n\t')
        # SOURCE LINE 26
        __M_writer(u'\n\t')
        # SOURCE LINE 31
        __M_writer(u'\n\n\n    <body>\n\t\t<div id="container">\n\t\t\t<table>\n\t\t\t<form action=\'scrape_teams\' method=post>\n\t\t\t<fieldset class="admin">\n\t\t\t\t<legend>Scrape Team Information</legend>\n\t\t\t\t<ul>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<label for="from">From:</label>\n\t\t\t\t\t\t<input width="80em" type="text" id="from" name="from" value=')
        # SOURCE LINE 43
        __M_writer(escape(c.default_scrape_url))
        __M_writer(u' />\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<input type="submit" value="submit" />\n\t\t\t\t\t</li> \n\t\t\t\t</ul>\n\t\t\t</fieldset>\n\t\t\t</form>\n\t\t\t\t\n\t\t\t<form action=\'parse_majors\' method=post>\n\t\t\t<fieldset class="admin">\n\t\t\t\t<legend>Parse Majors</legend>\n\t\t\t\t<ul>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<label for="majors">Formatted majors list:</label>\n\t\t\t\t\t\t<textarea rows=10 id="majors" name="majors">')
        # SOURCE LINE 58
        __M_writer(escape(c.formatted_majors))
        __M_writer(u'</textarea>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<input type="submit" value="submit" />\n\t\t\t\t\t</li> \n\t\t\t\t</ul>\n\t\t\t</fieldset>\n\t\t\t</form>\n\n\t\t\t<form action=\'parse_choices\' method=post>\n\t\t\t<fieldset class="admin">\n\t\t\t\t<legend>Parse Choices</legend>\n\t\t\t\t<ul>\n\t\t\t\t\t<li>\n\t\t\t\t\t<label for="majors">Space delimited choice data: </label>\n\t\t\t\t\t\t<textarea rows=20 cols=80 id="choices" name="choices"></textarea>\n\t\t\t\t\t</li>\n\t\t\t\t\t<li>\n\t\t\t\t\t\t<input type="submit" value="submit" />\n\t\t\t\t\t</li> \n\t\t\t\t</ul>\n\t\t\t</fieldset>\n\t\t\t</form>\n\n\t\t</div>\n\t<input type="hidden" id="sid_hash" value="')
        # SOURCE LINE 83
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
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        if path not in self.seen_css:
            # SOURCE LINE 13
            __M_writer(u'\t\t\t<link rel="stylesheet" type="text/css" href="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" media="')
            __M_writer(escape(media))
            __M_writer(u'" >\n')
        # SOURCE LINE 15
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
        # SOURCE LINE 17
        __M_writer(u'\n')
        # SOURCE LINE 18
        if path not in self.seen_js:
            # SOURCE LINE 19
            __M_writer(u'\t\t\t<script type="text/javascript" src="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" ></script>\n')
        # SOURCE LINE 21
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
        # SOURCE LINE 24
        __M_writer(u'\n\t\t')
        # SOURCE LINE 25
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
        # SOURCE LINE 27
        __M_writer(u'\n\t\t')
        # SOURCE LINE 28
        __M_writer(escape(js_links('/js/jquery-1.2.6.pack.js')))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 29
        __M_writer(escape(js_links('/js/jquery.color.js')))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 30
        __M_writer(escape(js_links('/js/buttons.js')))
        __M_writer(u'\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


