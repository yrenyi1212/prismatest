# -*- coding: utf-8 -*-
import pytest

if __name__ == '__main__':
    # pytest.main(['-s', 'testcases/', '-m download', '--alluredir=./tmp/my_allure_results '])
    pytest.main(['-s', 'testcases/', '--alluredir=./tmp/my_allure_results '])