# -*- coding: utf-8 -*-
from core.client import Client
import allure


class Tenant(Client):
    def __init__(self, host, **kwargs):
        super(Tenant, self).__init__(host, **kwargs)

    @allure.step
    def get_key(self, key, secret, clientcode, apitype=0):
        payloads = {
            'key': key,
            'secret': secret,
            'clientcode': clientcode,
            'apitype': apitype
        }
        return self.post('/Api/External/GetKey', payloads=payloads)

    @allure.step('setp in tenant.py::Tenant')
    def get_project_info_list(self, apikey):
        payloads = {
            'apikey': apikey
        }
        return self.post('/Api/External/GetProjectInfoList', payloads=payloads)

    @allure.step
    def get_send_project_list(self, apikey, projectid, pageindex, pagesize):
        payloads = {
            'apikey': apikey,
            'projectid': projectid,
            'pageindex': pageindex,
            'pagesize': pagesize
        }

        return self.post('/Api/External/GetSendToPersonList', payloads=payloads)

    @allure.step
    def get_send_project_status_list(self, apikey, projectid, pageindex, pagesize):
        payloads = {
            'apikey': apikey,
            'projectid': projectid,
            'pageindex': pageindex,
            'pagesize': pagesize
        }
        return self.post('/Api/External/GetSendToPersonStatusList', payloads=payloads)

    @allure.step
    def get_analysis_list(self, apikey, projectid, demographicname, reporttype):
        payloads = {
            'apikey': apikey,
            'projectid': projectid,
            'demographicname': demographicname,
            'reporttype': reporttype
        }
        return self.post('/Api/External/GetAnalysisList', payloads=payloads)

    @allure.step
    def download_analysis_by_id(self, apikey, id):
        payloads = {
            'apikey': apikey,
            'id': id
        }

        return self.post('/Api/External/DownLoadAnalysisByID', payloads=payloads)
