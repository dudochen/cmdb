import xadmin
from .models import NAVI
from django.contrib import admin
from xadmin import views

class NaviAdmin(object):
        pass
xadmin.site.register(NAVI, NaviAdmin)