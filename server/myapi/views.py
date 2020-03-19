from django.shortcuts import render,HttpResponse

# Create your views here.
import json
from respositoy import models

def asset(request):

    if request.method == 'POST':
        res = json.loads(request.body)
        print(res)

        #### 1.获取post过来的主机名，判断主机是否合法
        status = res['basic']['status']
        if status != 10000:
            return HttpResponse('采集出错')

        hostname = res['basic']['data']['hostname']

        server_obj = models.Server.objects.filter(hostname=hostname).first()

        if not server_obj:
            return HttpResponse('资产未录入！')

        ##### 2.判断一下硬盘数据采集是否成功
        code = res['disk']['status']
        if code != 10000:
            models.ErrorLog.objects.create(asset_obj=server_obj, content=res['disk']['data'], title='采集硬盘数据出错')


        ##### 3.保存磁盘的数据入库

        new_disk_data = res['disk']['data']

        ### 新的slot集合
        new_slot = list(new_disk_data.keys())

        ### 老的slot集合
        old_disk_data = models.Disk.objects.filter(server_obj=server_obj).all()
        old_slot = []
        for obj in old_disk_data:
            old_slot.append(obj.slot)

        add_slot = set(new_slot).difference(set(old_slot))  #### [0,1,2,3,4,5]

        if add_slot:
            for slot in add_slot:
                #### {'slot': '0', 'pd_type': 'SAS', 'capacity': '279.396', 'model': 'SEAGATE ST300MM0006     LS08S0K2B5NV'},
                disk_info = res['disk']['data'][slot]
                disk_info['server_obj'] = server_obj

                models.Disk.objects.create(**disk_info)




        return HttpResponse('okokok')
    else:

        #### 从数据库中获取服务器的主机名

        #### 最终将数据库中存的主机名以列表的格式返回
        return HttpResponse(['c1.com', 'c2.com'])

