# -*- coding: utf-8 -*-
import pytest
import os
from common.read_data import data
from api.tenant import Tenant
import allure

import json
import logging

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, 'data', yaml_file_name)
    yaml_data = data.load_yaml(data_file_path)
    return yaml_data


base_data = get_data('base_data.yml')

HOST = data.load_ini(data_file_path)['host']['BASEURL']
IP_HEADER = data.load_ini(data_file_path)['host']['IP_HEADER']
IP_HEADER_ADDR = data.load_ini(data_file_path)['host']['IP_HEADER_ADDR']


@pytest.fixture(autouse=True)
def log_level(caplog):
    caplog.set_level(logging.INFO)


@pytest.fixture()
def tenant():
    t = Tenant(host=HOST)
    yield t
    t.session.close()

@allure.step
@pytest.fixture()
def getkey_fixtrue(tenant):
    key = base_data['init_vivo_user']['key']
    secret = base_data['init_vivo_user']['secret']
    clientcode = base_data['init_vivo_user']['clientcode']
    tenant.session.headers.update({IP_HEADER: IP_HEADER_ADDR})
    res = tenant.post(url='/Api/External/GetKey',
                      json={"key": key, "secret": secret, "clientcode": clientcode, "apitype": 0})
    yield res['data']['apikey']


@pytest.fixture(autouse=True)
def info(tenant, getkey_fixtrue, request):
    param = request.getfixturevalue('param')
    if 'getkey_fixtrue' in request.fixturenames:
        apikey = param['payload'].get('apikey', None)
        if apikey == 0:
            param['payload'].update({"apikey": getkey_fixtrue})
    else:
        pass
    header = param.get('header', None)
    if header:
        tenant.session.headers.update(header)
    else:
        tenant.session.headers.pop('HTTP_X_FORWARDED_FOR', None)

    title = param.get('title', None)
    if title:
        allure.title(title)
    logging.info(param['payload'])
    return param['payload']


def pytest_generate_tests(metafunc):
    if "param" in metafunc.fixturenames:
        filename = metafunc.function.__name__ + ".json"
        dat = json.load(open(os.path.join(BASE_PATH, 'data', filename), encoding='UTF-8'))
        ids = [i["title"] for i in dat['payloads']]
        metafunc.parametrize("param", dat['payloads'], ids=ids, scope='function')
    else:
        pass
