
def check_dict(expect, res):
    """
    递归比较两个字典的key:value是否一致
    :param expect:
    :param res:
    :return:
    """
    if isinstance(expect, dict):
        for k in expect.keys():
            temp_value1 = expect[k]
            temp_value2 = res.get(k, None)
            check_dict(temp_value1, temp_value2)
    else:
        assert expect == res, "响应错误,预期{0}，响应{1}".format(expect, res)