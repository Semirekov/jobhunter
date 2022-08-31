import collections
import os

from dotenv import load_dotenv


Env = collections.namedtuple('Env', ['superjob_token'])

def get_settins():    
    load_dotenv()
    return Env(
        os.getenv('SUPERJOB_TOKEN', '')
    )