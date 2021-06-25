# -*- coding: utf-8 -*-
from core.client import Client
import allure


class Tenant(Client):
    def __init__(self, host, **kwargs):
        super(Tenant, self).__init__(host, **kwargs)

    @allure.step
    def post(self, **kwargs):
        return super(Tenant, self).post(url=kwargs['url'], payloads=kwargs['json'])
