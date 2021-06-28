# -*- coding: utf-8 -*-
import allure
from functools import wraps
from common.tools import check_dict
from testcases import init_uri


def check_result(func):
    """
    通用验证方法,对测试接口响应进行验证,预期key与响应key需完全一致，如需要逻辑判断，请不要使用此方法进行断言验证
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        expect = kwargs["param"]["expect"]
        check_dict(expect, res)

    return wrapper


@allure.feature("vivo")
class TestPrisma:

    @allure.story('获取凭证')
    @check_result
    def test_get_key(self, param, tenant):
        res = tenant.post(url=init_uri['GetKey'], json=param['payload'])
        return res

    @allure.story('获取租户的项目列表')
    @check_result
    def test_get_project_list(self, param, tenant):
        res = tenant.post(url=init_uri['GetProjectInfoList'], json=param['payload'])
        return res

    @allure.story('获得租户项目填答地址')
    @check_result
    def test_get_send_project_list(self, param, tenant):
        res = tenant.post(url=init_uri['GetSendToPersonList'], json=param['payload'])
        return res

    @allure.story('获得人员填答状态')
    @check_result
    def test_get_send_project_status_list(self, param, tenant):
        res = tenant.post(url=init_uri['GetSendToPersonStatusList'], json=param['payload'])
        return res

    @allure.story('获取报告')
    @check_result
    def test_get_analysis_list(self, param, tenant):
        res = tenant.post(url=init_uri['GetAnalysisList'], json=param['payload'])
        return res

    @allure.story('下载报告')
    @check_result
    def test_download_analysis_by_id(self, param, tenant):
        res = tenant.post(url=init_uri['DownLoadAnalysisByID'], json=param['payload'])
        return res
