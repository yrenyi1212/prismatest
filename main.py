# -*- coding: utf-8 -*-
import pytest

if __name__ == '__main__':
    pytest.main(['-s', "testcases/test_prisma.py::TestPrisma", '--alluredir=./tmp/my_allure_results '])
