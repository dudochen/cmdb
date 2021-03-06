# Generated by Django 2.0.6 on 2018-06-19 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=50, verbose_name='名称')),
                ('ip', models.CharField(max_length=100, verbose_name='ip地址')),
                ('cpu_num', models.CharField(max_length=50, verbose_name='cpu数量')),
                ('mem_size', models.CharField(max_length=100, verbose_name='内存大小')),
                ('cpu_idle', models.CharField(max_length=100, verbose_name='cpu空闲率')),
                ('mem_usage', models.CharField(max_length=100, verbose_name='mem使用率')),
            ],
            options={
                'verbose_name': '监控',
                'verbose_name_plural': '监控',
                'db_table': 'monitor',
                'permissions': (('can_add_monitor', '添加监控点'), ('can_change_monitor', '修改监控点'), ('can_delete_monitor', '删除监控点'), ('can_view_monitor', '查看监控点')),
            },
        ),
    ]
