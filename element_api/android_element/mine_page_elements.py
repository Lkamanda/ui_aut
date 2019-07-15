# 我的页面相关
"""
我的页面
"""
from comm.element_error import element_error

# 点击个人中心 登录/注册 button
def dL_element(self):
    try:
        self.driver.find_element_by_id("user_name_tv").click()
    except Exception as e:
        element_error(self, e)


# 点击离线地图
def download_map(self):
    try:
        self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]"
                                          "/androidsupport.v7.widget.RecyclerView[1]"
                                          "/android.widget.RelativeLayout[1]").click()
    except Exception as e:
        element_error(self, e)


# 点击设置按钮
def mine_setting(self):
    try:
        self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[10]"
                                     "/android.widget.RelativeLayout").click()
    except Exception as e:
        element_error(self, e)
