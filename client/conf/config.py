##### 自定制配置
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USER = 'root'


MODE = 'agent' ## ssh /salt

DEBUG = True  ### True 代表调试模式  False 代表上线正式采集

PLUGINS_DICT = {
    'basic' : 'src.plugins.basic.Basic',
    'board' : 'src.plugins.board.Board',
    'cpu'   : 'src.plugins.cpu.Cpu',
    'disk'  : 'src.plugins.disk.Disk',
    'memory': 'src.plugins.memory.Memory',
    'nic'   : 'src.plugins.nic.Nic',
}

API_URL = 'http://127.0.0.1:8001/api/'
