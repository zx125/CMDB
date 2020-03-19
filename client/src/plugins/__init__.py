
#### 用来管理采集的插件的
import traceback
from lib.config.settings import settings
import importlib

class Plugins_Dict():

    def __init__(self, hostname=None):
        self.mode = settings.MODE
        self.plugins_dict = settings.PLUGINS_DICT
        self.debug = settings.DEBUG
        self.hostname = hostname


    #### 从配置文件中读取插件配置，并执行相关的函数获取数据
    def execute(self):
        ### 1.从配置文件中读取插件配置
        res = {}
        for k, v in self.plugins_dict.items():
            ### k: basic
            ### v: 'src.plugins.basic.Basic'
            response = {'status':None, 'data':None}
            #### 2. 导入模块， 获取类， 并实例化
            try:
                module_path, class_name = v.rsplit('.', 1)
                ### 3. 加载模块
                m = importlib.import_module(module_path)
                #### 4. 加载类, 反射
                cls = getattr(m, class_name)
                #### 5. 执行每一个插件类下面的process方法
                ret = cls().process(self.command_func, self.debug )

                response['status'] = 10000
                response['data'] = ret

            except Exception as e:
                response['status'] = 10001
                response['data'] = traceback.format_exc()

            res[k] = response

        return res


    def command_func(self, cmd):

        if self.mode == 'agent':
            import subprocess
            res = subprocess.getoutput(cmd)
            return res

        elif self.mode == 'ssh':
            import paramiko
            # 创建SSH对象
            ssh = paramiko.SSHClient()
            # 允许连接不在know_hosts文件中的主机
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接服务器
            ssh.connect(hostname=self.hostname, port=22, username='root', password='root')

            # 执行命令
            stdin, stdout, stderr = ssh.exec_command(cmd)
            # 获取命令结果
            result = stdout.read()

            # 关闭连接
            ssh.close()
            return result

        elif self.mode == 'salt':
            import salt.client

            local = salt.client.LocalClient()
            result = local.cmd(self.hostname, 'cmd.run', [cmd])
            return result
        else:
            raise  Exception('当前模式只支持 agent/ssh/salt !!!')





