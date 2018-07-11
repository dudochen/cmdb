# encoding: utf-8
import sys
import os
#  获取当前文件的路径，以及路径的父级文件夹名
pwd = os.path.dirname(os.path.realpath(__file__))
# 将项目目录加入setting
sys.path.append(pwd + "/../")

# manage.py中 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapps.settings")
import django
django.setup()

from monitor.models import Monitor

###这里替换成采集数据的方法
def conn_server():
    temp={'192.168.5.108':{'hostname': 'bogon1', 'ip': '192.168.5.108', 'cpu_num': '16', 'mem_size': '2.0G', 'cpu_idle': '100%', 'mem_usage': '16.02%'},
         '192.168.5.109':{'hostname': 'bogon1098', 'ip': '192.168.5.109', 'cpu_num': '3', 'mem_size': '2.0G', 'cpu_idle': '100%', 'mem_usage': '17.02%'},
     }
    return temp
def do_info(ip):
    monitor = Monitor()
    #print(monitor)
    #monitor = Monitor.objects.all()
    tmp_info = conn_server()
    #if tmp_inof[ip]:
    is_has_ip = Monitor.objects.filter(ip=ip).exists()
    #print(is_has_ip)
    if (is_has_ip):
        tmp = tmp_info.get(ip)
        Monitor.objects.filter(ip=ip).update(hostname = tmp['hostname'],cpu_num=tmp['cpu_num'],mem_size=tmp['mem_size'],
        mem_usage=tmp['mem_usage'])
        print('update')
    else:
        tmp = tmp_info.get(ip)
        if tmp:
            monitor.hostname=tmp['hostname']
            monitor.ip=tmp['ip']
            monitor.cpu_num=tmp['cpu_num']
            monitor.mem_size=tmp['mem_size']
            monitor.cpu_idle=tmp['cpu_idle']
            monitor.mem_usage=tmp['mem_usage']
            monitor.save()
            print('add ok')
#Monitor.objects.filter(id=3).update(hostname ='test')
#print(monitor)
def inset():
    f=['192.168.5.105','192.168.5.108','192.168.5.109','192.168.5.110'] #替换读取到的数据ip列表（就是我们自己配置采集的服务器的ip）
    for ip in f:
        #result=conn_server()
        do_info(ip)  
inset()
    


