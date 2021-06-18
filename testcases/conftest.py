import pytest
import yaml
import os
from common.read_data import data
import logging
from api.tenant import Tenant
import allure
from functools import wraps

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, 'data', yaml_file_name)
    yaml_data = data.load_yaml(data_file_path)
    return yaml_data


base_data = get_data('base_data.yml')
api_data = get_data('api_test_data.yml')

HOST = data.load_ini(data_file_path)['host']['BASEURL']
HTTP_X_FORWARDED_FOR = data.load_ini(data_file_path)['host']['HTTP_X_FORWARDED_FOR']
tenant = Tenant(HOST)


@pytest.fixture(autouse=True)
def log_level(caplog):
    caplog.set_level(logging.INFO)


@allure.step
@pytest.fixture(scope='class')
def getkey_fixtrue():
    key = base_data['init_vivo_user']['key']
    secret = base_data['init_vivo_user']['secret']
    clientcode = base_data['init_vivo_user']['clientcode']
    tenant.session.headers.update({"HTTP_X_FORWARDED_FOR": HTTP_X_FORWARDED_FOR})
    res = tenant.get_key(key, secret, clientcode, apitype=0)
    yield res['data']['apikey']


def set_header(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tenant.session.headers.pop('HTTP_X_FORWARDED_FOR', None)
        reqip = kwargs.get('reqip')
        title = kwargs.get('title')
        apikey = kwargs.get('apikey')
        if title:
            allure.dynamic.title(title)
        if reqip:
            tenant.session.headers.update({"HTTP_X_FORWARDED_FOR": reqip})
        if apikey == 0:
            apikey = kwargs.get('getkey_fixtrue')
            kwargs.update({'apikey': apikey})
        return func(*args, **kwargs)

    return wrapper