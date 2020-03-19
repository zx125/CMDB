from lib.config.settings import settings
from src.client import Agent,SSHSalt

def run():

    if settings.MODE == 'agent':
        Agent().collect()
    else:
        SSHSalt().collect()

