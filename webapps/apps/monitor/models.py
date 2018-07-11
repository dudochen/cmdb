from __future__ import unicode_literals
from django.db import models

class Monitor(models.Model):
    hostname = models.CharField(u"名称",max_length=50)
    ip = models.CharField(u"ip地址",max_length=100)
    cpu_num = models.CharField(u"cpu数量",max_length=50)
    mem_size = models.CharField(u"内存大小",max_length=100)
    cpu_idle = models.CharField(u"cpu空闲率",max_length=100)
    mem_usage = models.CharField(u"mem使用率",max_length=100)


    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "监控"
        verbose_name_plural = verbose_name
        db_table = 'monitor'

        permissions = (
            ("can_add_monitor", "添加监控点"),
            ("can_change_monitor", "修改监控点"),
            ("can_delete_monitor", "删除监控点"),
            ("can_view_monitor", "查看监控点"),
        )