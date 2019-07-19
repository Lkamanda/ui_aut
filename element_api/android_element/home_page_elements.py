# 主页相关
from comm.element_error import element_error, element_error_main_chat


def userAvatar_element(self):
    """点击首页用户头像"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('com.erlinyou.worldlist:id/user_avatar_img').click()
    except Exception as e:
        # print('ceshi')
        # print('----------------------%s-------' % mainChat_element.__name__)
        element_error(self=self, e=e)


def mainChat_element(self):
    """主页消息入口 main_chat  id"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("chat_img").click()
    except Exception as e:
        element_error_main_chat(self, e)


def homepage_roam_element(self):
    """点击主页漫游页面"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/iv_starthelicopter").click()
    except Exception as e:
        element_error(self, e)


def homepage_input_box(self):
    """主页面输入框"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("searchtextview").click()
    except Exception as e:
        element_error(self, e)


def homepage_location_element(self):
    """首页定位自身，和旋转"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/recenter_img").click()
    except Exception as e:
        element_error(self, e)


def homepage_amplification_element(self):
    """首页放大"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/iv_zoom_in").click()
    except Exception as e:
        element_error(self, e)


def homepage_narrow_element(self):
    """首页缩小"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/iv_zoom_in").click()
    except Exception as e:
        element_error(self, e)


def homepage_2d_3d(self):
    """2d 3d"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/ll_2d3dSwitch").click()
    except Exception as e:
        element_error(self, e)


def dynamic(self):
    """ 首页 动态"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/iv_moments_icon").click()
    except Exception as e:
        element_error(self, e)
