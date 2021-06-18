from core.client import Client
import os
import allure
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, 'config', 'setting.ini')


class Tenant(Client):
    def __init__(self, host, **kwargs):
        super(Tenant, self).__init__(host, **kwargs)

    @allure.step
    def get_key(self, key, secret, clientcode, apitype=0):
        data = {
            'key': key,
            'secret': secret,
            'clientcode': clientcode,
            'apitype': apitype
        }
        return self.post('/Api/External/GetKey', jsondata=data)

    @allure.step('setp in tenant.py::Tenant')
    def get_project_info_list(self, apikey):
        data = {
            'apikey': apikey
        }
        return self.post('/Api/External/GetProjectInfoList', jsondata=data)

    @allure.step
    def get_send_project_list(self, apikey, projectid, pageindex, pagesize):
        data = {
            'apikey': apikey,
            'projectid': projectid,
            'pageindex': pageindex,
            'pagesize': pagesize
        }

        return self.post('/Api/External/GetSendToPersonList', jsondata=data)

    @allure.step
    def get_send_project_status_list(self, apikey, projectid, pageindex, pagesize):
        data = {
            'apikey': apikey,
            'projectid': projectid,
            'pageindex': pageindex,
            'pagesize': pagesize
        }
        return self.post('/Api/External/GetSendToPersonStatusList', jsondata=data)

    @allure.step
    def get_analysis_list(self, apikey, projectid, demographicname, reporttype):
        data = {
            'apikey': apikey,
            'projectid': projectid,
            'demographicname': demographicname,
            'reporttype': reporttype
        }
        return self.post('/Api/External/GetAnalysisList', jsondata=data)

    @allure.step
    def download_analysis_by_id(self, apikey, id):
        data = {
            'apikey': apikey,
            'id': id
        }

        return self.post_file('/Api/External/DownLoadAnalysisByID', jsondata=data)
        # with open(r'cc', 'wb+') as f:
        #     f.write(r.content)
        # return r

# tenant = Tenant(data.load_ini(data_file_path)['host']['baseurl'])
