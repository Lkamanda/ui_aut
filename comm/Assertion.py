from log.logger import mylogger
from comm.common import screenShot
from comm.comm_api import get_login_state


def check_login(self, login_state,  test_name):
    """
    通过login_state 来判断是否登录成功
    :param driver:
    :param login_state:
    :param test_name:
    :return:
    """
    if login_state == 2:
        return True
    else:
        screenShot(self, test_name)
        return False

