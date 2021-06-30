# -*- coding: utf-8 -*-
import pytest
import os
from api.tenant import Tenant
import allure
import json
import logging
from testcases import *


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
    """
    预获取apikey
    :param tenant:
    :return:
    """

    tenant.session.headers.update({IP_HEADER: IP_HEADER_ADDR})
    res = tenant.post(url=init_uri['GetKey'], json=base_data['init_vivo_user'])
    yield res['data']['apikey']


@pytest.fixture(autouse=True)
def predata_fixture(tenant, getkey_fixtrue, request):
    """
    对header进行统一处理，对apikey进行预处理
    :param tenant:
    :param getkey_fixtrue:
    :param request:
    :return:
    """
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
        tenant.session.headers.pop(IP_HEADER, None)

    title = param.get('title', None)
    if title:
        allure.title(title)
    return param['payload']


def pytest_generate_tests(metafunc):
    """
    参数化,生成测试用例，请保证测试数据文件名与测试方法名一致，不然无法自动生成用例
    :param metafunc: 
    :return: 
    """
    if "param" in metafunc.fixturenames:
        filename = metafunc.function.__name__ + ".json"
        _f = os.path.join(BASE_PATH, 'data', filename)
        if os.path.exists(_f):
            dat = json.load(open(_f, encoding='UTF-8'))
            ids = [i["title"] for i in dat['payloads']]
            metafunc.parametrize("param", dat['payloads'], ids=ids)
        else:
            metafunc.definition.add_marker('skip')
            metafunc.parametrize("param", {})
    else:
        pass
