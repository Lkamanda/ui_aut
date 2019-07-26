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

def check_setting_go_home(self, home_address):
    """
    校验回家, 回公司
    :param self:
    :param home_address:
    :return:
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("*[@text= %s ]") % home_address
        return True
    except Exception as e:
        return False
