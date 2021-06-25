# -*- coding: utf-8 -*-
import allure
from functools import wraps
import logging


def check_result(func):
    """
    对测试接口响应码进行验证，所有接口定义的响应码key均为code,如果需要其他验证，请在具体测试用例进行判断
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        code = kwargs["param"]["expect"].get("code", None)
        assert res["code"] == code, "请求响应code值{0}与预期值不符{1}".format(res["code"], code)

    return wrapper


@allure.feature("vivo")
class TestPrisma:

    @allure.story('获取凭证')
    @check_result
    def test_get_key(self, param, tenant):
        res = tenant.post(url='/Api/External/GetKey', json=param['payload'])
        return res

    @allure.story('获取租户的项目列表')
    @check_result
    def test_get_project_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetProjectInfoList', json=param['payload'])
        return res

    @allure.story('获得租户项目填答地址')
    @check_result
    def test_get_send_project_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetSendToPersonList', json=param['payload'])
        return res

    @allure.story('获得人员填答状态')
    @check_result
    def test_get_send_project_status_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetSendToPersonStatusList', json=param['payload'])
        return res

    @allure.story('获取报告')
    @check_result
    def test_get_analysis_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetAnalysisList', json=param['payload'])
        return res

    @allure.story('下载报告')
    @check_result
    def test_download_analysis_by_id(self, param, tenant):
        res = tenant.post(url='/Api/External/DownLoadAnalysisByID', json=param['payload'])
        return res
