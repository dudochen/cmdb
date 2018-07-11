import xadmin
from .models import AssetPermission
from django.contrib import admin
from xadmin import views


class AssetPermissionAdmin(object):
        pass
xadmin.site.register(AssetPermission, AssetPermissionAdmin)