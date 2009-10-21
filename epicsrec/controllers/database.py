import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from epicsrec import model, forms
from epicsrec.model import meta

from epicsrec.lib.base import BaseController, render
from formalchemy.ext.pylons.admin import FormAlchemyAdminController

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn

log = logging.getLogger(__name__)

class DatabaseControllerBase(BaseController):
    model = model
    forms = forms

    @authorize(ValidAuthKitUser())
    def __before__(self): pass
    
    def Session(self):
        return meta.Session


DatabaseController = FormAlchemyAdminController(DatabaseControllerBase)
