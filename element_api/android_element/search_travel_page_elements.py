from comm.element_error import element_error
from config.myconfig import MyConfig


def search_travel_element(self):
    """旅行"""
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/rl_myTrip").click()
    except Exception as e:
        element_error(self, e)


def search_travel_strategy(self):
    """旅游攻略"""
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("旅游攻略")').click()
    except Exception as e:
        element_error(self, e)


def search_travel_route(self):
    """旅游路线"""
    try:

        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("旅游路线")').click()
    except Exception as e:
        element_error(self, e)


def search_travel_mine_trip(self):
    """我的行程"""
    try:
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("我的行程")').click()
    except Exception as e:
        element_error(self.driver, e)


def mine_trip_add(self):
    """新建我的行程"""
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/create_trip").click()
    except Exception as e:
        element_error(self, e)


def mine_trip_new_input(self, n):
    """新建行程输入框"""
    try:
        myconfig = MyConfig()
        text = myconfig.get_new_trip_input_text(n)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/trip_edit_name").send_keys(text)
    except Exception as e:
        element_error(self, e)


def mine_trip_new_finish(self):
    """新建行程完成"""
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/send_btn").click()
    except Exception as e:
        element_error(self, e)


def mine_trip_new_add_place(self):
    """新建行程添加地点  文字栏"""
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/add_trip_place_btn").click()
    except Exception as e:
        element_error(self, e)


def mine_trip_send_place(self, n):
    """
    添加行程地点输入框
    :param driver:
    :param n:
    :return:
    """
    myconfig = MyConfig()
    place = myconfig.get_new_trip_add_place(n)
    self.driver.find_element_by_id("com.erlinyou.worldlist:id/search_edit").send_keys(place)


def mine_trip_add_place(self):
    """为行程添加详细地点"""
    try:
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/add_trip_point").click()
    except Exception as e:
        element_error(self, e)
