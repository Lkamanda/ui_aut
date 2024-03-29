#  """移动地图，旋转地图，2D、3D切换， 回家，回公司，搜索街道，地点，门牌号"""
import unittest
from public.assertion import *
from comm.webdriver import *
# from comm.config import MyConfig
from comm.comm_api import *
from public.public_module import *
from element_api.android_element.elements import *
from comm.Assertion import *


class Test3(WebDriver, unittest.TestCase):
    # def test1_a(self):
    #     """zh 登录"""
    #     test_name = "%s登录" % self._testMethodName
    #     # 获取登录状态
    #     login_state = get_login_state(self)
    #     print('1=========')
    #     # 微信登录，前提是手机当前已有微信运行
    #     login(self=self, mode=1, login_state=login_state)
    #
    #     # 返回首页
    #     return_home(self, test_name)

    def test2_a_0(self):
        """回家"""

        test_name = "%s回家" % self._testMethodName
        mylogger.info("%s" % test_name)

        # 设置当前所在城市
        config_number = myconfig.config_number

        through_config_setting(self=self, config_number=config_number)

        self.driver.implicitly_wait(10)
        homepage_input_box(self)
        print("输入")
        go_home_number = 0
        self.driver.implicitly_wait(5)
        try:
            homepage_details_go_home_add(self)
            go_home_number = go_home_number
        except:
            homepage_details_go_home_cancel_element(self)
            go_home_number = go_home_number + 1
            print(2)

        if go_home_number == 0:
            mylogger.info("进入添加家的测试用例")
            # go_home_number.click()
            chat_place_search_place(self, n=3)
            mylogger.info('触发输入家的地址成功')

            chat_place_type(self=self, n=4)

            # 选择查询到的第一个搜索结果
            self.driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.ListView/"
                                              "android.widget.LinearLayout[0]/android.widget.LinearLayout").click()
            mylogger.info("选择搜索结果成功")
            homepage_details_go_home_element(self)
            mylogger.info("进入导航页")
        elif go_home_number == 1:
            homepage_details_go_home_element(self)
            mylogger.info("进入导航页，已经设置家")
            check_direct_go_home(self=self, test_name=test_name)

        # 校验回家添加家地址是否成功
        go_home_check = check_setting_go_home(self=self, home_address=myconfig.get_place_share_search(n=3))

        # 如果是研发版本需要添加当前前位置
        if config_number == 1:
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id().send_keys("巴黎圣母院")


        navigation_details_goto_element(self)
        screenShot(self=self, test_name="%s+ '路线规划图'" % test_name)
        mylogger.info("开始规划路线")

        navigation_details_trip_mode(self=self, mode=2)
        navigation_details_navigation_element(self)
        mylogger.info("开始导航")
        screenShot(self=self, test_name="%s+ '导航开始'" % test_name)
        
        return_home(self=self, test_name=test_name)

        self.assertEqual(True, go_home_check)

    # def test2_a_1(self):
    #     """取消回家并对家重新设置"""
    #     test_name = "%s取消回家操作"% self._testMethodName
    #     mylogger.info("%s" % test_name)
    #     self.driver.implicitly_wait(5)
    #     homepage_input_box(self)
    #     go_home_number = 0
    #     self.driver.implicitly_wait(5)
    #     try:
    #         homepage_details_go_home_add(self)
    #         go_home_number = go_home_number
    #         print(1)
    #     except Exception as e:
    #         print(e)
    #         mylogger.info("当前用户已经设置了回家")
    #         homepage_details_go_home_cancel_element(self)
    #         go_home_number = go_home_number + 1
    #         print(2)
    #
    #     if go_home_number == 0:
    #         mylogger.info("进入添加家的测试用例")
    #         # go_home_number.click()
    #         chat_place_search_place(self=self, n=3)
    #         mylogger.info('触发输入家的地址成功')
    #         # 选择查询到的第一个搜索结果
    #         self.driver.find_element_by_xpath(
    #             "//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.view.View").click()
    #         mylogger.info("选择搜索结果成功")
    #         homepage_details_go_home_element(self)
    #         mylogger.info("进入导航页")
    #         self.driver.implicitly_wait(5)
    #         navigation_details_goto_element(self)
    #         screenShot(self=self, test_name="%s+ '路线规划图'" % test_name)
    #         mylogger.info("开始规划路线")
    #         self.driver.implicitly_wait(10)
    #         navigation_details_trip_mode(self=self, mode=2)
    #         navigation_details_navigation_element(self)
    #         mylogger.info("开始导航")
    #         screenShot(self=self, test_name="%s+ '导航开始'" % test_name)
    #     elif go_home_number == 1:
    #         homepage_details_go_home_cancel_element_1(self)
    #         mylogger.info("取消回家设置")
    #         homepage_details_go_home_add(self)
    #         self.assertTrue(check_cancel_go_home(self=self, test_name=test_name))
    #     self.driver.press_keycode(4)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #
    # def test2_a_2(self):
    #     """回公司"""
    #     test_name = "%s回公司" % self._testMethodName
    #     mylogger.info("%s" % test_name)
    #     self.driver.implicitly_wait(10)
    #     homepage_input_box(self)
    #     print("输入")
    #     go_company_number = 0
    #     self.driver.implicitly_wait(5)
    #     try:
    #         homepage_details_go_company_add_element(self)
    #         go_company_number = go_company_number
    #     except:
    #         homepage_details_go_company_cancel_element(self)
    #         go_company_number = go_company_number + 1
    #         print(2)
    #     if go_company_number == 0:
    #         mylogger.info("进入添加公司的测试用例")
    #         chat_place_search_place(self=self, n=7)
    #         mylogger.info("触发输入公司的地址成功")
    #         self.driver.find_element_by_xpath("//android.support.v4.view.ViewPager/android.widget.RelativeLayout"
    #                                           "/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]")\
    #             .click()
    #         mylogger.info("选择搜索结果成功")
    #         self.driver.implicitly_wait(5)
    #         homepage_details_go_company_element(self)
    #         mylogger.info("进入导航页")
    #     elif go_company_number == 1:
    #         homepage_details_go_company_element(self)
    #         mylogger.info("进入导航页，已经设置回公司")
    #         check_direct_go_home(self=self, test_name=test_name)
    #     self.driver.implicitly_wait(5)
    #     navigation_details_goto_element(self)
    #     screenShot(self=self, test_name="%s+ '路线规划图'" % test_name)
    #     mylogger.info("开始规划路线")
    #     self.driver.implicitly_wait(10)
    #     navigation_details_trip_mode(self=self, mode=2)
    #     print('ceshi')
    #     self.driver.implicitly_wait(5)
    #     navigation_details_navigation_element(self)
    #     mylogger.info("开始导航")
    #     screenShot(self=self, test_name="%s+ '导航开始'" % test_name)
    #     self.driver.press_keycode(4)
    #     # navigation_details_quit(self)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回主页面")
    #
    # def test3_a(self):
    #     # 未完成
    #     """旋转地图"""
    #     test_name = "旋转地图"
    #     mylogger.info("%s" % test_name)
    #     time.sleep(3)
    #     homepage_location_element(self)
    #     mylogger.info("触发旋转")
    #     screenShot(self, test_name)
    #     homepage_location_element(self)
    #     screenShot(self, test_name)
    #
    # def test3_a_1(self):
    #     """2D和3D之间的切换"""
    #     test_name = "2D和3D之间的切换"
    #     mylogger.info("%s" % test_name)
    #     time.sleep(2)
    #     homepage_amplification_element(self)
    #     time.sleep(2)
    #     homepage_amplification_element(self)
    #     time.sleep(2)
    #     homepage_amplification_element(self)
    #     homepage_2d_3d(self)
    #     mylogger.info("切换成了3d")
    #     time.sleep(4)
    #     screenShot(self=self, test_name="%s+'3d截图'" % test_name)
    #     homepage_2d_3d(self)
    #     screenShot(self=self, test_name="%s+'2d截图'" % test_name)
    #
    # def test4_a_1(self):
    #     """进入漫游模式"""
    #     test_name = "进入漫游模式"
    #     mylogger.info("%s" % test_name)
    #     self.driver.implicitly_wait(5)
    #     homepage_roam_element(self)
    #     roam_page_look_more_element(self)
    #     self.driver.implicitly_wait(5)
    #     roam_page_choice_ldmark(self=self, n=6)
    #     screenShot(self=self, test_name="漫游截图")
    #     time.sleep(2)
    #     roam_page_goto_element(self)
    #     navigation_details_navigation_element(self)
    #     self.driver.implicitly_wait(5)
    #     navigation_details_quit(self)
    #     self.driver.press_keycode(4)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回主页面")
    #
    # def test5_a_1(self):
    #     """搜索街道，计算路径，导航回家"""
    #     test_name = "搜索街道，计算路径，导航回家"
    #     mylogger.debug("%s" % test_name)
    #     self.driver.implicitly_wait(10)
    #     homepage_input_box(self)
    #     chat_place_search_place(self=self, n=1)
    #     chat_place_choice_All(self=self, n=1)
    #     navigation_details_goto_element(self)
    #     mylogger.info("进入路线规划")
    #     time.sleep(2)
    #     screenShot(self=self, test_name="%s+'路线导航'" % test_name)
    #     navigation_details_navigation_element(self)
    #     time.sleep(4)
    #     self.driver.press_keycode(4)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回主页面")
    #
    # def test5_a_2(self):
    #     """搜索地点，计算路径，导航回家"""
    #     test_name = "搜索地点，计算路径，导航回家"
    #     mylogger.debug("%s" % test_name)
    #     self.driver.implicitly_wait(10)
    #     homepage_input_box(self)
    #     chat_place_search_place(self=self, n=0)
    #     chat_place_choice_All(self=self, n=1)
    #     navigation_details_goto_element(self)
    #     mylogger.info("进入路线规划")
    #     time.sleep(2)
    #     screenShot(self=self, test_name="%s+'路线导航'" % test_name)
    #     navigation_details_trip_mode(self=self, mode=2)
    #     navigation_details_navigation_element(self)
    #     time.sleep(4)
    #     self.driver.press_keycode(4)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回主页面")
    #
    # def test5_a_3(self):
    #     """搜索门牌号，计算路径，导航回家"""
    #     test_name = "搜索街道，计算路径，导航回家"
    #     mylogger.debug("%s" % test_name)
    #     self.driver.implicitly_wait(10)
    #     homepage_input_box(self)
    #     chat_place_search_place(self=self, n=4)
    #     chat_place_choice_All(self=self, n=1)
    #     navigation_details_goto_element(self)
    #     mylogger.info("进入路线规划")
    #     time.sleep(2)
    #     screenShot(self=self, test_name="%s+'路线导航'" % test_name)
    #     navigation_details_navigation_element(self)
    #     time.sleep(4)
    #     self.driver.press_keycode(4)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回主页面")
    #
    # def test6_a_1(self):
    #     """汽车、步行、自行车导航模式"""
    #     mode_list = [2, 3, 4, 5, 6]
    #     for i in mode_list:
    #         test_name_list = ["0", "1", "汽车", "公交", "地铁", "步行", "自行车"]
    #         test_name = test_name_list[i]
    #         mylogger.debug("%s" % test_name)
    #         self.driver.implicitly_wait(10)
    #         homepage_input_box(self)
    #         self.driver.implicitly_wait(10)
    #         chat_place_search_place(self=self, n=5)
    #         self.driver.implicitly_wait(10)
    #         chat_place_choice_All(self=self, n=1)
    #         self.driver.implicitly_wait(10)
    #         navigation_details_goto_element(self)
    #         mylogger.info("进入路线规划")
    #         screenShot(self=self, test_name="%s+'路线规划'" % test_name)
    #         self.driver.implicitly_wait(10)
    #         navigation_details_trip_mode(self=self, mode=i)
    #         if i == 2 or i == 5 or i == 6:
    #             self.driver.implicitly_wait(10)
    #             navigation_details_navigation_element(self)
    #             time.sleep(2)
    #         elif i == 3:
    #             time.sleep(2)
    #             screenShot(self=self, test_name="公交路线图")
    #         elif i == 4:
    #             mylogger.info("进入地铁路线图")
    #             time.sleep(2)
    #             screenShot(self=self, test_name="地铁路线图")
    #             # 地铁mode下导航
    #             self.driver.implicitly_wait(5)
    #             self.driver.find_element_by_id("com.erlinyou.worldlist:id/detail_iconbutton_container").click()
    #             mylogger.info("进入地铁导航详情")
    #             self.driver.find_element_by_id("com.erlinyou.worldlist:id/exit_img").click()
    #         self.driver.press_keycode(4)
    #         time.sleep(1)
    #         self.driver.press_keycode(4)
    #         mylogger.info("返回主页面")
    #
    # def test7_a_1(self):
    #     """添加历史记录，并对历史记录校验"""
    #     test_name = "添加历史记录，并对历史记录校验"
    #     mylogger.debug("%s" % test_name)
    #     self.driver.implicitly_wait(10)
    #     homepage_input_box(self)
    #     self.driver.implicitly_wait(10)
    #     chat_place_search_place(self=self, n=6)
    #     self.driver.implicitly_wait(5)
    #     chat_place_choice_All(self=self, n=2)
    #     self.driver.implicitly_wait(10)
    #     self.driver.press_keycode(4)
    #     self.driver.press_keycode(4)
    #     self.driver.implicitly_wait(5)
    #     homepage_input_box(self)
    #     self.assertEqual(True, check_history_search(self=self))
    #     self.driver.press_keycode(4)
    #
    # def test8_a_0(self):
    #     """添加收藏, 重命名， 删除收藏"""
    #     rename_text = myconfig.get_rename_text()
    #     test_name = "添加收藏, 重命名， 删除收藏"
    #     mylogger.info("%s" % test_name)
    #     self.driver.implicitly_wait(10)
    #     homepage_input_box(self)
    #     chat_place_search_place(self=self, n=7)
    #     self.driver.implicitly_wait(5)
    #     chat_place_choice_All(self=self, n=1)
    #     self.driver.implicitly_wait(5)
    #     navigation_details_collection(self)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #     time.sleep(1)
    #     self.driver.press_keycode(4)
    #     mylogger.info("返回主页面")
    #     self.driver.implicitly_wait(2)
    #     homepage_input_box(self)
    #     self.driver.implicitly_wait(5)
    #     chat_place_favorite(self)
    #     self.driver.implicitly_wait(5)
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("望京SOHO")').click()
    #     mylogger.info("-----添加收藏成功-------")
    #     self.driver.press_keycode(4)
    #     # 长按被收藏地点
    #     place_ele = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("望京SOHO")')
    #     action = TouchAction(self)
    #     action.long_press(el=place_ele, duration=3000).wait(10000).perform()
    #     self.driver.implicitly_wait(5)
    #     chat_place_collection_rename(self)
    #     if check_collection(self=self) == "False":
    #         mylogger.error("测试用例执行失败")
    #         self.driver.implicitly_wait(5)
    #         chat_place_collection_cancel(self)
    #         self.driver.press_keycode(4)
    #         time.sleep(1)
    #         self.driver.press_keycode(4)
    #         mylogger.info("退出环境")
    #         self.assertEqual(True, check_collection(self))
    #     elif check_collection(self=self) == "True":
    #         mylogger.info("开始执行重命名操作")
    #         input_box = self.driver.find_element_by_id("com.erlinyou.worldlist:id/et")
    #         length = len(input_box.text)
    #         print(length)
    #         clean_text(self=self, length=length)
    #         clean_text_length = len(input_box.text)
    #         self.assertTrue(True, check_clean_text(length=clean_text_length))
    #         mylogger.info("清空输入框成功")
    #         input_box.send_keys(rename_text)
    #         self.driver.implicitly_wait(5)
    #         print(1)
    #         chat_place_collection_rename_finish(self)
    #         print(2)
    #         self.driver.implicitly_wait(5)
    #         place_ele = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("重命名收藏地点")')
    #         # place_ele = self.driver.find_element_by_android_uiautomator("new UiSelector().textContains(%s)")
    #         action = TouchAction(self)
    #         action.long_press(el=place_ele, duration=3000).wait(10000).perform()
    #         mylogger.info("----重命名成功———")
    #         chat_place_collection_delete(self)
    #         self.assertEqual(True, check_collection_delete(self))
    #         mylogger.info("---删除收藏成功---")
    #         self.driver.press_keycode(4)
    #         time.sleep(1)
    #         self.driver.press_keycode(4)
    #
    # def test9_a_0(self):
    #     """添加我的行程"""
    #     test_name = "添加一个行程"
    #     mylogger.debug("%s" % test_name)
    #     self.driver.implicitly_wait(5)
    #     homepage_input_box(self)
    #     search_travel_element(self)
    #     mylogger.info("进入旅行界面")
    #     self.driver.implicitly_wait(5)
    #     search_travel_mine_trip(self)
    #     mine_trip_add(self)
    #     mylogger.info("进入新建行程界面")
    #     self.driver.implicitly_wait(5)
    #     mine_trip_new_input(self=self, n=0)
    #     self.driver.implicitly_wait(5)
    #     mine_trip_new_finish(self)
    #     time.sleep(2)
    #     self.driver.press_keycode(4)
    #     self.driver.implicitly_wait(5)
    #     self.assertEqual(True, check_add_trip(self))
    #     mylogger.info("新建行程成功")
    #     self.driver.implicitly_wait(5)
    #     for i in range(0, 4):
    #         if i == 0:
    #             mine_trip_new_add_place(self)
    #         else:
    #             mine_trip_add_place(self)
    #         self.driver.implicitly_wait(5)
    #         mine_trip_send_place(self=self, n=i)
    #         self.driver.implicitly_wait(5)
    #         # chat_place_choice_Address(self=self, n=1)
    #         chat_place_choice_All(self=self, n=1)
    #     self.driver.press_keycode(4)
    #     time.sleep(2)
    #     self.driver.press_keycode(4)
    #
    # def test9_a_1(self):
    #     """当前用户退出"""
    #     login_state = get_login_state(self)
    #     logout(self, login_state)























