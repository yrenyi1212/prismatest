import allure


@allure.step("check response")
def check_dict(expect, res):
    """
    递归比较两个字典的key:value是否一致
    :param expect:
    :param res:
    :return:
    """

    for k in expect.keys():
        temp_value1 = expect[k]
        temp_value2 = res.get(k, None)
        if isinstance(temp_value1, dict):
            check_dict(temp_value1, temp_value2)
        else:
            assert temp_value1 == temp_value2, "字段{2}错误,预期{0}，响应{1}".format(temp_value1, temp_value2, k)