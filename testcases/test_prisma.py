# -*- coding: utf-8 -*-
import pytest
from testcases.conftest import api_data
from .conftest import tenant, set_header
import allure


class TestPrisma:

    @allure.feature("vivo")
    @allure.story('获取凭证')
    @set_header
    @pytest.mark.getkey
    @pytest.mark.parametrize('key,secret,clientCode,actiontype,code,reqip,title', api_data['test_get_key'])
    def test_get_key(self, key, secret, clientCode, actiontype, code, reqip, title):
        res = tenant.get_key(key=key, secret=secret, clientcode=clientCode, apitype=actiontype)
        assert res['code'] == code

    @allure.feature("vivo")
    @allure.story('获取租户的项目列表')
    @set_header
    @pytest.mark.getprojectlist
    @pytest.mark.parametrize('apikey,code,reqip, title', api_data['test_get_project_list'])
    def test_get_project_list(self, apikey, code, title, reqip, getkey_fixtrue):
        res = tenant.get_project_info_list(apikey=apikey)
        assert res['code'] == code

    @allure.feature("vivo")
    @allure.story('获得租户项目填答地址')
    @set_header
    @pytest.mark.sendprojectlist
    @pytest.mark.parametrize('apikey, projectid, pageindex, pagesize,code,reqip,title',
                             api_data['test_get_send_project_list'])
    def test_get_send_project_list(self, apikey, projectid, pageindex, pagesize, code, reqip, title, getkey_fixtrue):
        res = tenant.get_send_project_list(apikey, projectid, pageindex, pagesize)
        assert code == res['code']

    @allure.feature("vivo")
    @allure.story('获得人员填答状态')
    @set_header
    @pytest.mark.sendprojectstatuslist
    @pytest.mark.parametrize('apikey, projectid, pageindex, pagesize,code,reqip,title',
                             api_data['test_get_send_project_status_list'])
    def test_get_send_project_status_list(self, apikey, projectid, pageindex, pagesize, code, reqip, title,
                                          getkey_fixtrue):
        res = tenant.get_send_project_status_list(apikey, projectid, pageindex, pagesize)
        assert res['code'] == code

    @allure.feature("vivo")
    @allure.story('获取报告')
    @set_header
    @pytest.mark.analysislist
    @pytest.mark.parametrize('apikey, projectid, demographicname, reporttype,code,total,reqip,title',
                             api_data['test_get_analysis_list'])
    def test_get_analysis_list(self, apikey, projectid, demographicname, reporttype, code, total, reqip, title,
                               getkey_fixtrue):
        res = tenant.get_analysis_list(apikey=apikey, projectid=projectid, demographicname=demographicname,
                                       reporttype=reporttype)
        assert res['code'] == code
        if not code:
            totalsize = True if res['total'] > 0 else False
            assert total == totalsize

    @allure.feature("vivo")
    @allure.story('下载报告')
    @set_header
    @pytest.mark.download
    @pytest.mark.parametrize('apikey, id, code, reqip, title', api_data['test_download_analysis_by_id'])
    def test_download_analysis_by_id(self, apikey, id, code, reqip, title, getkey_fixtrue):
        res = tenant.download_analysis_by_id(apikey=apikey, id=id)
        assert res['code'] == code
