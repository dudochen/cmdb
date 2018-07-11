import xadmin
from .models import AssetGroup,Assets,Idc
from django.contrib import admin
from xadmin import views

class AssetGroupAdmin(object):
        pass
class AssetsAdmin(object):
    pass

class IdcAdmin(object):
    list_display = ['name', 'address', 'tel']
    search_fields = ['name']
    list_filter = ['name', 'tel']
xadmin.site.register(AssetGroup, AssetGroupAdmin)
xadmin.site.register(Assets, AssetsAdmin)
xadmin.site.register(Idc, IdcAdmin)