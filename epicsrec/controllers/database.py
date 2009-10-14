import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from epicsrec import model, forms
from epicsrec.model import meta

from epicsrec.lib.base import BaseController, render
from formalchemy.ext.pylons.admin import FormAlchemyAdminController


log = logging.getLogger(__name__)

class DatabaseController(BaseController):
    model = model
    forms = forms
    def Session(self):
        return meta.Session

DatabaseController = FormAlchemyAdminController(DatabaseController)
