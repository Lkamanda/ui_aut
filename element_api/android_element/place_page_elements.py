"""
message 下chat 位置页面 element api
"""

from comm.element_error import element_error

from config.myconfig import MyConfig


def chat_place_search_place(self, n):
    """
    place page search
    :param driver:
    :param n: where you want to go  类型 0,1,2,3,4
    """
    myconfig = MyConfig()
    place = myconfig.get_place_share_search(n)
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/search_edit").send_keys(place)
    except Exception as e:
        element_error(self, e)

def chat_place_get_back(self):
    """place get back button """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btnBack").click()
    except Exception as e:
        element_error(self, e)


def chat_place_sleep(self):
    """ place page Sleep button """
    # com.erlinyou.worldlist:id/tv_house
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("tv_house").click()
    except Exception as e:
        element_error(self, e)

def chat_place_eat(self):
    """place page Eat button"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_food").click()
    except Exception as e:
        element_error(self, e)

def chat_place_visit(self):
    """place page visit button """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_play").click()
    except Exception as e:
        element_error(self, e)

def chat_place_move(self):
    """place page move button"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_out").click()
    except Exception as e:
        element_error(self, e)


def chat_place_service(self):
    """place page service button"""
    try:
        self.driver.implicitly_wait(5)
        # driver.implicitly_wait(5)
        self.driver.find_element_by_id("tv_service").click()
        print("t")
    except Exception as e:
        print("f")
        element_error(self, e)


def chat_place_nearby(self):
    """place page nearby button """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/tv_more").click()
    except Exception as e:
        element_error(self, e)


def chat_place_favorite(self):
    """ place page favorite button 收藏"""
    # Interactions are not available for this element
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/rl_favorite").click()
    except Exception as e:
        element_error(self, e)


def chat_place_on_map(self):
    """place page on map choice """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/rl_select").click()
    except Exception as e:
        element_error(self.driver, e)


def chat_place_on_map_sure(self):
    """place page on map 确定"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("detail_set_tv").click()
    except Exception as e:
        element_error(self, e)


def chat_place_on_map_GPS(self):
    """place page GPS"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("rl_current").click()
    except Exception as e:
        element_error(self, e)


def  chat_place_type(self, n):
    """
    搜素框下地点类型
    :param driver: self.driver
    :param n:
    n = 1 :  综合
    n = 2 ： 城市
    n = 3 :  地址
    n = 4 :  地点
    n = 5 :  酒店
    n = 6 :  美食
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]"
                                     "/android.widget.TextView" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_place_choice_Address(self, n):
    """
    搜索框下 地点 第n个位置信息
    :param driver: self.driver
    :param n: 第几个查询寻结果
    :return:
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView"
                                     "/android.widget.LinearLayout[%s]" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_place_choice_All(self, n):
    """搜索框下 全部 第n个位置信息"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.RelativeLayout/"
                                     "android.support.v7.widget.RecyclerView/android.widget.LinearLayout[%s]" % n)\
            .click()
    except Exception as e:
        element_error(self, e)


def chat_place_choice_City(self, n):
    """
    搜索框下 城市下 第n个数据
    :param driver:
    :param n:
    :return:
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.LinearLayout[%s]" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_place_surrounding_share(self, n):
    """
    对 place type 周边兴趣点列表数据获取
    :param self:
    :param n: 周边兴趣点列表分享 1 or 2
    :return:
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]" % n)\
            .click()
    except Exception as e:
        element_error(self, e)


def chat_send_file_element(self):
    """message send file element"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("img_icon").click()
    except Exception as e:
        element_error(self, e)


def chat_place_collection_rename(self):
    """收藏详情 重命名"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("重命名")').click()
    except Exception as e:
        element_error(self, e)


def chat_place_collection_delete(self):
    """收藏详情 删除"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("删除")').click()
    except Exception as e:
        element_error(self, e)


def chat_place_collection_delete_all(self):
    """收藏详情 删除所有"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("删除全部")').click()
    except Exception as e:
        element_error(self, e)


def chat_place_collection_cancel(self):
    """收藏详情 取消"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_android_uiautomator('ew UiSelector().textContains("取消")').click()
    except Exception as e:
        element_error(self, e)


def chat_place_collection_rename_finish(self):
    """收藏详情 重命名 完成"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/dialog_ok").click()
    except Exception as e:
        element_error(self.driver, e)
