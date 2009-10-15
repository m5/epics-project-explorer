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

class DatabaseController(BaseController):
    model = model
    forms = forms
    def Session(self):
        return meta.Session

    @authorize(ValidAuthKitUser())
    def edit(self, *args, **kwargs):
        return super(AdminControllerBase, self).edit(*args, **kwargs)


DatabaseController = FormAlchemyAdminController(DatabaseController)
