import xadmin
from .models import Domain
from django.contrib import admin
from xadmin import views

class GlobalSetting(object):
    """
    配置抬头和尾部，以及列表显示
    """
    site_title = '泡面管理管理系统'
    site_footer = '泡面管理系统开源'
    menu_style = 'accordion'
class DomainAdmin(object):
        pass
xadmin.site.register(Domain, DomainAdmin)