import os
from common import ReadFileData

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

base_data = ReadFileData.load_yaml(os.path.join(BASE_PATH, 'data', 'base_data.yml'))
init_conf = ReadFileData.load_ini(os.path.join(BASE_PATH, 'config', 'setting.ini'))

init_uri = init_conf['URL']
init_host = init_conf['HOST']

HOST = init_host['BASEURL']
IP_HEADER = init_host['IP_HEADER']
IP_HEADER_ADDR = init_host['IP_HEADER_ADDR']

__all__ = ['BASE_PATH', 'base_data', 'init_conf', 'HOST', 'IP_HEADER', 'IP_HEADER_ADDR', 'init_uri']
