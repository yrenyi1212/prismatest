# -*- coding: utf-8 -*-
import allure
from functools import wraps
from common.tools import check_dict


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
        result = check_dict(expect, res)
        assert result, "预期与响应不符,预期{0}，响应{1}".format(expect, res)
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
