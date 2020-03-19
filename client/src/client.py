from src.plugins import Plugins_Dict
from lib.config.settings import settings

import requests

class Agent():

    def collect(self):
        #### 采集资产信心
        res = Plugins_Dict().execute()

        for k, v in res.items():
            print(k, v)

        #### 将采集到的信息数据发送给API端
        # requests.post(settings.API_URL, data=json.dumps(res))
        requests.post(settings.API_URL, json=res)

class SSHSalt():

    def getHostname(self):
        hostnames = requests.get(settings.API_URL)

        ### hostnames 就是获取的主机名列表
        # return ['c1.com', 'c2.com']
        return hostnames ### ['c1.com', 'c2.com']

    def task(self, hostname):
        res = Plugins_Dict(hostname=hostname).execute()

        requests.post(settings.API, json=res)

    def collect(self):
        hostnames = self.getHostname()

        from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
        p = ThreadPoolExecutor(10)

        for hostname in hostnames:

            p.submit(self.task, hostname)
