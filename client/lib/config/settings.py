
from . import global_settings
from conf import config

class Settings():

    def __init__(self):

        #### 集成高级配置
        for k in dir(global_settings):
            if k.isupper():
                v = getattr(global_settings, k)
                setattr(self, k, v)

        #### 集成用户自定制配置
        for k in dir(config):
            if k.isupper():
                v = getattr(config, k)
                setattr(self, k, v)




settings = Settings()



