from comm.common import *
import unittest
from comm.webdriver import *
from element_api.android_element.place_page_elements import *
from public.public_module import *
from comm.comm_api import *
from log.logger import mylogger
from element_api.android_element.home_page_elements import mainChat_element
from element_api.android_element.chat_page_elements import *

class Test2(WebDriver, unittest.TestCase):

    def test1(self):
        # 对于新安装的app进行获取权限
        test_name = "%s登录" % self._testMethodName

        get_agree(self)
        obtain_permission(self=self)

        # 获取登录状态
        login_state = get_login_state(self)

        # 微信登录，前提是手机当前已有微信运行
        login(self=self, mode=2, login_state=login_state)

        # 返回首页
        return_home(self, test_name)

    def test2_1(self):
        """通过搜索分享地点"""
        test_name = "%s:通过搜索分享地点" % self._testMethodName
        mylogger.info("%s start" % test_name)

        mainChat_element(self)

        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")

        chat_img_more_element(self)
        time.sleep(2)

        chat_place_search_place(self, n=0)
        mylogger.info("触发：输入框输入")

        chat_place_type(self=self, n=3)
        mylogger.info("选择地点类型为地点")
        chat_place_choice_Address(self, n=1)
        mylogger.info("位置信息发送")
        self.driver.implicitly_wait(5)
        screenShot(self=self, test_name=test_name)
        self.driver.implicitly_wait(5)

        return_home(self=self, test_name=test_name)

    def test2_2(self):
        """通过搜索分享街道"""
        test_name = "%s:通过搜索分享街道" % self._testMethodName
        mylogger.info("%s start" % test_name)

        mainChat_element(self.driver)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_search_place(self, n=1)
        mylogger.info("触发：输入框输入")

        chat_place_type(self=self, n=1)
        mylogger.info("选择地点类型为全部")
        chat_place_choice_All(self=self, n=1)
        mylogger.info("位置信息发送")
        self.driver.implicitly_wait(5)
        screenShot(self=self, test_name=test_name)
        return_home(self, test_name)

    def test2_3(self):
        """通过搜索分享城市"""
        test_name = "%s:通过搜索分享城市" % self._testMethodName
        mylogger.info("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")

        chat_img_more_element(self)
        time.sleep(2)

        chat_place_search_place(self=self, n=2)
        mylogger.info("触发：输入框输入")

        chat_place_type(self=self, n=2)
        mylogger.info("选择地点类型为城市")

        chat_place_choice_City(self=self, n=1)
        mylogger.info("位置信息发送")

        screenShot(self=self, test_name=test_name)
        return_home(self, test_name)

    def test3_1_Sleep(self):
        """进入 place 住宿 并分享周边兴趣列表位置"""
        test_name = "%s:住宿下分享" % self._testMethodName

        mylogger.info("%s start" % test_name)

        mainChat_element(self)

        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")

        chat_img_more_element(self)
        time.sleep(2)

        chat_place_sleep(self)

        chat_place_surrounding_share(self, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(self=self, test_name=test_name)
        return_home(self=self, test_name=test_name)

    def test3_2_Food(self):
        """进入 place food 并分享周边兴趣列表位置"""
        test_name = "%s:美食下分享" % self._testMethodName
        mylogger.debug("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_eat(self)

        chat_place_surrounding_share(self=self, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(self=self, test_name=test_name)
        self.driver.implicitly_wait(5)
        return_home(self, test_name)

    def test3_3_Visit(self):
        """进入 place visit 并分享周边兴趣列表位置"""
        test_name = "%s:游玩出行下分享" % self._testMethodName
        mylogger.info("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_visit(self)

        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(self=self, test_name=test_name)
        return_home(self=self, test_name=test_name)

    def test3_4_Move(self):
        """进入 place move 并分享周边兴趣列表位置"""
        test_name = "%s:出行下分享" % self._testMethodName
        mylogger.info("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_move(self.driver)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(self=self, test_name=test_name)
        return_home(self=self, test_name=test_name)

    def test3_5_Service(self):
        """进入 place service 并分享周边兴趣列表位置"""
        test_name = "%s:服务下分享" % self._testMethodName

        mylogger.debug("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_service(self.driver)

        chat_place_surrounding_share(self.driver, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(self=self, test_name=test_name)
        return_home(self, test_name)

    def test3_6_Favor(self):
        """进入 place service 并分享周边兴趣列表位置"""
        test_name = "出行下分享"
        mylogger.info("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_service(self)
        self.driver.implicitly_wait(5)
        chat_place_surrounding_share(self=self, n=1)
        mylogger.info("分享位置触发")
        time.sleep(2)
        screenShot(self=self, test_name=test_name)
        self.driver.implicitly_wait(5)
        return_home(self=self,test_name=test_name)

    def test3_7_Onmap(self):
        """进入place on_map 分享默认地点"""
        test_name = "%s:地图上发送默认地点" % self._testMethodName
        mylogger.info("%s start" % test_name)

        self.driver.implicitly_wait(5)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_on_map(self.driver)
        mylogger.info("on map 触发位置共享")
        self.driver.implicitly_wait(5)
        chat_place_on_map_sure(self.driver)
        screenShot(self.driver, test_name)
        return_home(self, test_name)

    def test3_8_place_GPS(self):
        """ place GPS 分享当前GPS定位"""
        test_name = "%s:地图上发送默认地点" % self._testMethodName
        mylogger.info("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_place_on_map_GPS(self.driver)
        mylogger.info("on map 触发位置共享")
        time.sleep(3)
        screenShot(self, test_name)
        self.driver.implicitly_wait(5)
        return_home(self, test_name)



    def test4_share_software(self):
        """message share software"""
        test_name = "%s:分享软件" % self._testMethodName
        mylogger.info("%s start" % test_name)
        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_img_more_element(self)
        time.sleep(2)

        chat_add_all(self.driver, n=8)
        mylogger.info("触发分享app发送")
        screenShot(self.driver, test_name)
        return_home(self, test_name)

    def test5(self):
        """message share file"""
        test_name = "%s发送文件" % self._testMethodName
        mylogger.info("%s start" % test_name)

        mainChat_element(self.driver)
        first_chat_element(self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        for i in range(1, 5):
            if i == 1:
                self.driver.implicitly_wait(5)
                chat_img_more_element(self.driver)
                time.sleep(2)
                chat_swipeLeft(self=self, t=5000)
                mylogger.info("触发chat左滑")
            else:
                self.driver.implicitly_wait(5)
                chat_img_more_element(self)
            self.driver.implicitly_wait(5)
            chat_send_file_element(self)
            self.driver.implicitly_wait(5)
            # 从文件管理中选取管理文件
            chat_send_file_type(self=self, n=3)

            chat_send_file_choice_folder(self=self, x=4, y=4, z=i)
            mylogger.info("发送文件第%s" % i)
            screenShot(self=self, test_name="%s发送第%s" % (str_nowTime(), i))
        return_home(self, test_name)

    def test6_1(self):
        """message send voice """
        test_name = "发送语音时长为10s"
        mylogger.debug("%s start" % test_name)

        mainChat_element(self)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")
        chat_voice_element(self).click()
        self.driver.implicitly_wait(5)
        chat_send_voice_element(self=self, t=10000)
        # time.sleep(5)
        return_home(self, test_name)

    def test6_2(self):
        """message send voice """
        test_name = "发送语音时长为180s"
        mylogger.debug("%s start" % test_name)
        self.driver.implicitly_wait(10)
        mainChat_element(self.driver)
        first_chat_element(self.driver)
        mylogger.info("进入与第一个联系人交互界面")
        chat_voice_element(self.driver).click()
        self.driver.implicitly_wait(5)
        t = 60000
        chat_send_voice_element(self=self, t=t)
        mylogger.info("发送语音时长为%s" % t)
        # time.sleep(5)
        return_home(self=self, test_name=test_name)

    def test7(self):
        # 退出登录
        login_state = get_login_state(self)
        logout(self, login_state)