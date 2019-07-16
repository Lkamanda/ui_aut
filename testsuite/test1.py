import unittest
from comm.webdriver import *
from comm.comm_api import *
from public.assertion import check_share_location_stop
import public.public_module
import sys

from element_api.android_element.home_page_elements import *
from element_api.android_element.chat_page_elements import *
from config.myconfig import myconfig


class Test1(WebDriver, unittest.TestCase):

    # def test1(self):
    #     # 对于新安装的app进行获取权限
    #     get_agree(self)
    #     obtain_permission(self=self)
    #
    #     # 获取登录状态
    #     login_state = get_login_state(self)
    #
    #     # 微信登录，前提是手机当前已有微信运行
    #     public.public_module.login(self=self, mode=2, login_state=login_state)
    #
    #     # 返回首页
    #     public.public_module.return_home(self)
    #
    # def test2(self):
    #     """与聊天page下第一个联系人发起回话"""
    #     test_name = self._testMethodName
    #     mylogger.debug(test_name)
    #
    #     self.driver.implicitly_wait(5)
    #     mainChat_element(self)
    #     self.driver.implicitly_wait(5)
    #     first_chat_element(self)
    #     mylogger.info("进入与第一个联系人交互界面")
    #
    #     self.driver.implicitly_wait(5)
    #
    #     chat_send_keys_element(self=self, chat_str=myconfig.get_chat_str(n=1))
    #     time.sleep(3)
    #     chat_send_all_element(self)
    #     mylogger.info("消息已发送")
    #     time.sleep(3)
    #     screenShot(self, test_name)
    #
    #     # 返回首页操作
    #     public.public_module.return_home(self)
    #
    # def test3(self):
    #     """第一个联系人发送照片和视频，预览"""
    #     test_name = self._testMethodName
    #     mylogger.debug(test_name)
    #
    #     self.driver.implicitly_wait(5)
    #     mainChat_element(self)
    #     self.driver.implicitly_wait(5)
    #     first_chat_element(self)
    #     mylogger.info("进入与第一个联系人交互界面")
    #
    #     self.driver.implicitly_wait(5)
    #
    #     chat_img_more_element(self)
    #     mylogger.info("点击+号")
    #
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album(self)
    #     mylogger.info("点击进入相册界面")
    #
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album_n(self, n=2)
    #
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album_n(self, n=7)
    #
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album_n(self, n=12)
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_preview(self)
    #     mylogger.info("进入发送预览")
    #     swipeLeft(self, 1000)
    #     self.driver.implicitly_wait(5)
    #     swipeLeft(self, 1000)
    #
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_preview_send(self)
    #     self.driver.implicitly_wait(30)
    #     mylogger.info("照片上传成功")
    #
    #     # 返回首页操作
    #     public.public_module.return_home(self)

    # def test4(self):
    #     """直接发送照片"""
    #     test_name = self._testMethodName
    #     mylogger.debug(test_name)
    #
    #     self.driver.implicitly_wait(5)
    #     mainChat_element(self)
    #     self.driver.implicitly_wait(5)
    #     first_chat_element(self)
    #     mylogger.info("进入与第一个联系人交互界面")
    #
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element_by_id("et_msg").click()  # com.erlinyou.worldlist:id/
    #     chat_img_more_element(self)
    #     mylogger.info("点击+号")
    #
    #     self.driver.implicitly_wait(15)
    #     chat_add_photo_album(self)
    #     mylogger.info("点击进入相册界面")
    #     self.driver.implicitly_wait(10)
    #     chat_add_photo_album_n(self, n=2)
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album_n(self, n=7)
    #     mylogger.info("选择照片/视频成功")
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_album_n(self, n=12)
    #     mylogger.info("选择照片/视频成功")
    #
    #     self.driver.implicitly_wait(5)
    #     chat_add_photo_send(self)
    #
    #     screenShot(self, test_name)
    #    public.public_module.return_home(self)

    def test5(self):
        """拍照后勾选所拍照片发送"""
        test_name = sys._getframe().f_code.co_name
        test_name = "{}拍照后勾选所拍照片发送".format(test_name)
        mylogger.debug(test_name)

        self.driver.implicitly_wait(5)
        mainChat_element(self)
        self.driver.implicitly_wait(5)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")

        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/et_msg").click()
        time.sleep(2)
        mylogger.info("触发聊天成功")
        self.driver.implicitly_wait(5)
        chat_img_more_element(self.driver)
        self.driver.implicitly_wait(5)
        chat_add_all(self, n=2)
        mylogger.info("进入拍摄page")
        time.sleep(2)
        self.driver.implicitly_wait(10)
        chat_take_picture_start(self)
        mylogger.info("触发拍摄按钮")
        self.driver.implicitly_wait(5)
        chat_take_picture_sure(self, n=2)
        self.driver.implicitly_wait(20)

        self.driver.press_keycode(4)
        time.sleep(3)
        screenShot(self=self, test_name=test_name)
        public.public_module.return_home(self)
    # def test_take_picture_2(self):
    #     """拍照后发送"""
    # def test_take_picture_3(self):
    #     """拍摄视频后发送"""
    # def test_take_picture_4(self):
    #     """拍摄照片后再拍摄视频发送"""

    def test6_1(self):
        """共享位置直接停止"""
        test_name = "共享位置直接停止"
        mylogger.debug(test_name)

        self.driver.implicitly_wait(5)
        mainChat_element(self)
        self.driver.implicitly_wait(5)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")

        self.driver.implicitly_wait(10)
        chat_img_more_element(self)
        chat_add_all(self, n=5)
        self.driver.implicitly_wait(10)
        chat_location_share_stop(self)
        self.assertEqual(True, check_share_location_stop(self=self, test_name=test_name))

        public.public_module.return_home(self)

    def test6_2(self):
        """共享位置返回聊天停止"""
        test_name = "共享位置返回聊天停止"
        mylogger.debug(test_name)

        self.driver.implicitly_wait(5)
        mainChat_element(self)
        self.driver.implicitly_wait(5)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")

        chat_img_more_element(self)
        chat_add_all(self, n=5)
        self.driver.implicitly_wait(5)
        chat_location_share_get_back(self)
        # self.driver.find_element_by_id("et_msg").click()
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("et_msg").send_keys("123")
        # mylogger.info("输入成功")
        self.driver.implicitly_wait(5)
        chat_send_all_element(self)
        self.driver.implicitly_wait(5)
        chat_location_share_stop(self)
        mylogger.info("位置共享结束,聊天终止")

        public.public_module.mainChat_element(self)

    def test7_contacts_share_1(self):
        """分享联系人"""
        test_name = "分享联系人"
        mylogger.debug(test_name)

        self.driver.implicitly_wait(5)
        mainChat_element(self)
        self.driver.implicitly_wait(5)
        first_chat_element(self)
        mylogger.info("进入与第一个联系人交互界面")

        chat_img_more_element(self)
        mylogger.info("add")
        self.driver.implicitly_wait(5)
        chat_add_all(self, n=6)
        mylogger.info("进入contacts page")
        time.sleep(1)
        chat_contacts_share(self, n=1)
        mylogger.info("选择第一张contacts发送")
        self.driver.implicitly_wait(10)
        chat_img_more_element(self)
        mylogger.info("add")
        self.driver.implicitly_wait(5)
        chat_add_all(self, n=6)
        mylogger.info("进入contacts page")
        time.sleep(1)
        chat_contacts_share(self, n=2)
        mylogger.info("选择第一张contacts发送")
        time.sleep(3)
        screenShot(self, test_name=test_name)
        public.public_module.return_home(self)

    def test7_contacts_share_2(self):
        """查询到指定联系人并分享查询的第一个"""
        test_name = "查询到指定联系人并分享查询的第一个"
        mylogger.debug(test_name)
        chat_img_more_element(self)
        mylogger.info("add")
        self.driver.implicitly_wait(5)
        chat_add_all(self, n=6)
        mylogger.info("进入contacts page")
        self.driver.implicitly_wait(5)
        chat_location_contact_share_search(self, n=u"zhoujialin")
        time.sleep(3)
        chat_contacts_share(self, n=1)
        mylogger.info("选择查询到的第一张contacts发送")
        screenShot(self=self, test_name=test_name)

        # 返回首页
        public.public_module.mainChat_element(self)

    def test9(self):
        # 退出登录
        login_state = get_login_state(self)

        public.public_module.logout(self, login_state)


if __name__ == '__main__':
    unittest.main(verbosity=2)
