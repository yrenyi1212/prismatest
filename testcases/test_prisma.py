# -*- coding: utf-8 -*-
import allure

@allure.feature("vivo")
class TestPrisma:

    @allure.story('获取凭证')
    def test_get_key(self, param, tenant):
        res = tenant.post(url='/Api/External/GetKey', json=param['payload'])
        assert param['expect']['code'] == res['code']

    @allure.story('获取租户的项目列表')
    def test_get_project_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetProjectInfoList', json=param['payload'])
        assert param['expect']['code'] == res['code']

    @allure.story('获得租户项目填答地址')
    def test_get_send_project_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetSendToPersonList', json=param['payload'])
        assert param['expect']['code'] == res['code']

    @allure.story('获得人员填答状态')
    def test_get_send_project_status_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetSendToPersonStatusList', json=param['payload'])
        assert param['expect']['code'] == res['code']

    @allure.story('获取报告')
    def test_get_analysis_list(self, param, tenant):
        res = tenant.post(url='/Api/External/GetAnalysisList', json=param['payload'])
        assert param['expect']['code'] == res['code']

    @allure.story('下载报告')
    def test_download_analysis_by_id(self, param, tenant):
        res = tenant.post(url='/Api/External/DownLoadAnalysisByID', json=param['payload'])
        assert param['expect']['code'] == res['code']
