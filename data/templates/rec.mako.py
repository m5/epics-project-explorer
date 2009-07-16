from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1247421408.860672
_template_filename='/home/mfivecoa/purdue/epics/EpicsRec/epicsrec/templates/rec.mako'
_template_uri='/rec.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n')
        # SOURCE LINE 2
        self.seen_css = set() 
        
        __M_writer(u'\n')
        # SOURCE LINE 3
        self.seen_js = set() 
        
        __M_writer(u'\n    <head>\n\t')
        # SOURCE LINE 5
        __M_writer(escape(self.css()))
        __M_writer(u'\n\t')
        # SOURCE LINE 6
        __M_writer(escape(self.js()))
        __M_writer(u'\n\t</head>\n\n\t')
        # SOURCE LINE 14
        __M_writer(u'\n\t')
        # SOURCE LINE 20
        __M_writer(u'\n\n\t')
        # SOURCE LINE 24
        __M_writer(u'\n\t')
        # SOURCE LINE 28
        __M_writer(u'\n\n\n    <body>\n        <fieldset><legend>Eng.</legend>\n            <span class="button unlit">AAE</span>\n            <span class="button unlit">A&amp;BE</span>\n            <span class="button unlit">BME</span>\n            <span class="button unlit">CE</span>\n            <span class="button unlit">CEM</span>\n            <span class="button unlit">CHE</span>\n            <span class="button unlit">CMPE</span>\n            <span class="button unlit">EE</span>\n            <span class="button unlit">Environ</span>\n            <span class="button unlit">IDE</span>\n            <span class="button unlit">IE</span>\n            <span class="button unlit">ME</span>\n            <span class="button unlit">MSE</span>\n            <span class="button unlit">NUCL</span>\n        </fieldset>\n        <fieldset><legend>Science</legend>\n            <span class="button unlit">Edu</span>\n            <span class="button unlit">Other</span>\n        </fieldset>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_css_links(context,path,media=''):
    context.caller_stack._push_frame()
    try:
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n')
        # SOURCE LINE 10
        if path not in self.seen_css:
            # SOURCE LINE 11
            __M_writer(u'\t\t\t<link rel="stylesheet" type="text/css" href="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" media="')
            __M_writer(escape(media))
            __M_writer(u'"></link>\n')
        # SOURCE LINE 13
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
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 16
        if path not in self.seen_js:
            # SOURCE LINE 17
            __M_writer(u'\t\t\t<script type="text/javascript" src="')
            __M_writer(filters.html_escape(escape(path)))
            __M_writer(u'" ></script>\n')
        # SOURCE LINE 19
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
        # SOURCE LINE 22
        __M_writer(u'\n\t\t')
        # SOURCE LINE 23
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
        # SOURCE LINE 25
        __M_writer(u'\n\t\t')
        # SOURCE LINE 26
        __M_writer(escape(js_links('/js/jquery-1.2.6.pack.js')))
        __M_writer(u'\n\t\t')
        # SOURCE LINE 27
        __M_writer(escape(js_links('/js/buttons.js')))
        __M_writer(u'\n\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


