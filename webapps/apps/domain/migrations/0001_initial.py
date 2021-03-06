# Generated by Django 2.0.6 on 2018-06-13 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain_name', models.URLField(verbose_name='域名名称')),
                ('ip', models.GenericIPAddressField(verbose_name='解析IP')),
                ('env', models.CharField(blank=True, max_length=50, null=True, verbose_name='使用环境')),
                ('add_area', models.CharField(blank=True, choices=[('1', 'dnspod'), ('2', 'company-dns'), ('3', 'azure-dnsmasq')], max_length=30, null=True, verbose_name='添加位置')),
                ('usage', models.CharField(max_length=50, verbose_name='用途')),
                ('applicant', models.CharField(max_length=50, verbose_name='申请人')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('expiration_time', models.DateTimeField(blank=True, max_length=200, null=True, verbose_name='过期时间')),
            ],
            options={
                'verbose_name': '域名管理',
                'verbose_name_plural': '域名管理',
                'db_table': 'domain',
                'permissions': (('can_add_domain', '添加域名'), ('can_change_domain', '修改域名'), ('can_delete_domain', '删除域名'), ('can_view_domain', '查看域名')),
            },
        ),
    ]
