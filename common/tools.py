import allure
from functools import wraps
from testcases.conftest import tenant


def set_header(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tenant.session.headers.pop('HTTP_X_FORWARDED_FOR', None)
        reqip = kwargs.get('reqip')
        title = kwargs.get('title')
        apikey = kwargs.get('apikey')
        if title:
            allure.dynamic.title(title)
        if reqip:
            tenant.session.headers.update({"HTTP_X_FORWARDED_FOR": reqip})
        if apikey == 0:
            apikey = kwargs.get('getkey_fixtrue')
            kwargs.update({'apikey': apikey})
        return func(*args, **kwargs)

    return wrapper
