import xadmin
from .models import Monitor
from django.contrib import admin
from xadmin import views

class MointorAdmin(object):
        list_display = ['hostname', 'ip', 'mem_usage']
        search_fields = ['hostname']
        list_filter = ['hostname', 'ip']
        #refresh_times=[3,5]
xadmin.site.register(Monitor, MointorAdmin)