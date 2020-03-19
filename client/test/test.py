
import subprocess
import requests
import json
########################### 1. agent 方案 #############
# res = subprocess.getoutput('ifconfig')
#
# # print(res)
#
# ip = res[20:30]
# print(ip)
#
# ### content-type: applciation/json
# ret = requests.post('http://127.0.0.1:8000/api/', data=json.dumps(ip))
#
# print(ret.text)



###############  2. ssh类方案 #########
#### pip3 install paramiko

import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.79.131', port=22, username='root', password='root')

# 执行命令
stdin, stdout, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result = stdout.read()
print(result)

# 关闭连接
ssh.close()


ip = result[20:30]
print(ip)

### content-type: applciation/json
ret = requests.post('http://127.0.0.1:8000/api/', data=json.dumps(ip))

print(ret.text)









