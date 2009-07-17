from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1247796360.84952
_template_filename='/root/EpicsRec/epicsrec/templates/rec.mak'
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
        g = context.get('g', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"\n"http://www.w3.org/TR/html14/loose.tdt">\n<html>\n')
        # SOURCE LINE 5
        self.seen_css = set() 
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin()]))
        __M_writer(u'\n')
        # SOURCE LINE 6
        self.seen_js = set() 
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin()]))
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
        __M_writer(u'\n\n\n    <body>\n\t\t<div id="container">\n\t\t<div id="majors_container">\n')
        # SOURCE LINE 38
        for row in g.major_map:
            # SOURCE LINE 39
            for m in row:
                # SOURCE LINE 40
                __M_writer(u'\t\t\t\t')
                school = m['school'] 
                
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['school'] if __M_key in __M_locals_builtin()]))
                __M_writer(u'\n\t\t\t\t')
                # SOURCE LINE 41
                major  = m['major'] 
                
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['major'] if __M_key in __M_locals_builtin()]))
                __M_writer(u'\n\t\t\t\t')
                # SOURCE LINE 42
                css    = m['css'] 
                
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['css'] if __M_key in __M_locals_builtin()]))
                __M_writer(u'\n')
                # SOURCE LINE 43
                if major:
                    # SOURCE LINE 44
                    __M_writer(u'            \t<span name="')
                    __M_writer(escape(school+'-'+major))
                    __M_writer(u'" style="')
                    __M_writer(escape(css))
                    __M_writer(u'" class="button major ')
                    __M_writer(escape(school))
                    __M_writer(u'">\n\t\t\t\t\t<span class="button_label">\n\t\t\t\t\t')
                    # SOURCE LINE 46
                    __M_writer(escape(major.replace('_',' ')))
                    __M_writer(u'\n\t\t\t\t\t</span>\n\t\t\t\t\t<span class="information" name="school">')
                    # SOURCE LINE 48
                    __M_writer(escape(school))
                    __M_writer(u'</span>\n\t\t\t\t</span>\n')
        # SOURCE LINE 53
        __M_writer(u'\t\t\t<span id="school"></span>\n\t\t</div>\n\t\t<div id="information">\n\t\t\t<h1>Epics Project Explorer</h1>\n\t\t\t<ul>\n\t\t\t<li>\n\t\t\t<span class="button selected"></span>\n\t\t\t<span class="inftext">Select any disciplines on the left that interest you.</span>\n\t\t\t</li>\n\t\t\t<li>\n\t\t\t<span class="button recomended"></span>\n\t\t\t<span calss="inftext">Select any interesting projects below for more information.</span>\n\t\t\t</li>\n\t\t\t</ul>\n\t\t\n\t\t\n\t\t</div>\n\t\t<div id="teams_container">\n')
        # SOURCE LINE 71
        for team in g.teams:
            # SOURCE LINE 72
            __M_writer(u'           \t<span name="')
            __M_writer(escape(team))
            __M_writer(u'" class="button team">\n\t\t\t\t<span class="button_label"name="abbr">\n\t\t\t\t\t')
            # SOURCE LINE 74
            __M_writer(escape(team))
            __M_writer(u'\n\t\t\t\t</span>\n\t\t\t\t<span class="information" name="title">\n\t\t\t\t\t')
            # SOURCE LINE 77
            __M_writer(escape(team.name))
            __M_writer(u'\n\t\t\t\t</span>\n\t\t\t\t<span class="information" name="description">\n\t\t\t\t\t')
            # SOURCE LINE 80
            __M_writer(escape(team.info))
            __M_writer(u'\n\t\t\t\t</span>\n\t\t\t\t<a class="information" href="')
            # SOURCE LINE 82
            __M_writer(escape(team.link))
            __M_writer(u'"></a>\n\t\t</span>\n')
        # SOURCE LINE 85
        __M_writer(u'\t\t</div>\n\t\t<span id="description" class="popup"></span>\n\t\t</div>\n\t<input type="hidden" id="sid_hash" value="')
        # SOURCE LINE 88
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


