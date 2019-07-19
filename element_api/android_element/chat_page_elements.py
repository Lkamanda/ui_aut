# 聊天相关
from appium.webdriver.common.touch_action import TouchAction

from log.logger import mylogger
from comm.element_error import element_error, element_error_main_chat
import os

def message_back_element(self):
    """消息页面返回home_page按钮"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("imageview_search").click()
    except Exception as e:
        element_error(self=self, e=e)


# 聊天title
def chatTitle_element(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/textview_tab_chat").click()
    except Exception as e:
        element_error(self=self, e=e)


#  联系人 title
def contacts_element(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_text("联系人").click()
    except Exception as e:
        element_error(self=self, e=e)


# 通知 title
def notice_element(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_text("通知")
    except Exception as e:
        element_error(self=self, e=e)


# 聊天下第一个窗口
def first_chat_element(self):
    try:
        self.driver.implicitly_wait(5)
        #driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.ListView/android.widget.RelativeLayout[1]").click()
        self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.ListView"
                                          "/android.widget.RelativeLayout[1]").click()
    except Exception as e:
        element_error(self=self, e=e)


# img_more  加号button
def chat_img_more_element(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/img_more").click()
    except Exception as e:
        element_error(self, e)


# 表情
def chat_expression_element(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/img_exp").click()
    except Exception as e:
        element_error(self=self, e=e)


def chat_send_keys_element(self, chat_str):
    """
    聊天输入框 输入
    :param self:
    :param self: self
    :param chat_str: 输入的字符
    :return:
    """
    # adb1 = 'adb shell ime set com.sohu.inputmethod.sogou.xiaomi/.SogouIME'
    adb3 = 'adb shell ime set io.appium.android.ime/.UnicodeIME'
    os.system(adb3)
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("et_msg").send_keys(chat_str)

    except Exception as e:
        element_error(self=self, e=e)
    # os.system(adb3)

# 发送消息button 点击
def chat_send_all_element(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btnSend").click()
    except Exception as e:
        element_error(self, e)


# 调用相册
def chat_add_photo_album(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "//android.support.v4.view.ViewPager/android.widget.GridView/android.widget.LinearLayout[1]"
            "/android.widget.ImageView").click()
    except Exception as e:
        element_error(self, e)


# 任选相册位置
def chat_add_photo_album_n(self, n):
    """
    :param self:
    :param n: 第几张图片
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
            "FrameLayout/android.widget.RelativeLayout/android.widget.GridView/android.widget."
            "RelativeLayout[%s]/android.widget.RelativeLayout/android.widget.Button" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_add_photo_send(self):
    """相册发送按钮"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/ok_button").click()
    except Exception as e:
        element_error(self, e)


def chat_add_photo_preview(self):
    """相册预览按钮"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("preview").click()
    except Exception as e:
        element_error(self, e)


def chat_add_photo_preview_send(self):
    """相册预览后的发送按钮"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_send").click()
    except Exception as e:
        element_error(self, e)


def chat_add_all(self, n):
    """
    对加号下的各个接口调用
    :param self:
    :param n:
    n = 1 :相册
    n = 2 : 拍摄
    n = 3 : 语音聊天
    n = 4 : 视频聊天
    n = 5 : 位置分享
    n = 6 : 联系人
    n = 7 : 地点
    n = 8 : 分享软件
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "//android.support.v4.view.ViewPager/android.widget.GridView/android.widget.LinearLayout[%s]"
            "/android.widget.ImageView" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_add_sendfile(self):
    """发送文件按钮触发"""
    # 进入加号下调用左滑
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "//android.support.v4.view.ViewPager/android.widget.GridView/android.widget.LinearLayout"
            "/android.widget.ImageView").click()
    except Exception as e:
        element_error(self, e)


# def chat_take_picture_getback(driver):
#     """拍照下返回"""
#     #driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.ImageView").click()
#     driver.find_element_by_id("com.erlinyou.worldlist:id/focusImageView").click()

# driver.find_element_by_id("com.erlinyou.worldlist:id/btnBack").click()


def chat_take_picture_start(self):
    """拍照启动"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_shutter_camera").click()
    except Exception as e:
        element_error(self, e)


def chat_take_picture_album(self):
    """从相册中选择"""
    # driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.ImageView").click()
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_thumbnail").click()
    except Exception as e:
        element_error(self, e)


def chat_take_picture_videotape(self):
    """照片切换视频按钮"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/btn_switch_mode").click()
    except Exception as e:
        element_error(self, e)


def chat_take_picture_sure(self, n):
    """
    拍照的取消和确定button
    :param self:
    :param n:
    n : 1 取消
    n : 2 确定
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "//android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ImageView[%s]" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_location_share_get_back(self):
    """位置分享 返回聊天按钮"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/chat").click()
    except Exception as e:
        element_error(self, e)


def chat_location_share_stop(self):
    """位置分享 结束"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/stop").click()
    except Exception as e:
        element_error(self, e)


def chat_location_contact_share_search(self, n):
    """联系人分享 查询button"""
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/edit_search").send_keys(n)
    except Exception as e:
        element_error(self, e)


def chat_contacts_share(self, n):
    """
    联系人分享 发送名片 button
    :param self: self
    :param n: 选择名片列表下第几个
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.widget.LinearLayout"
                                          "/android.widget.LinearLayout/android.widget.TextView" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_send_file_type(self, n):
    """
    message 发送文件选择类型
    :param self: self
    :param n:
    n = 1 :本地视频
    n = 2: 本地音乐
    n = 3 : 文件管理
    n = 4 : wps office
    n = 5 : 相册
    n = 6 : 进入录音机
    n = 7 : 音乐

    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout[%s]" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_send_file_choice_folder(self, x, y, z):
    """
    文件管理:下选择具体的文件夹 ， 仅支持首页
    :param self:
    :param x: 第1层第几个文件夹
    :param y: 第2层第几个文件夹
    :param z: 第3层第几个文件
    :return:
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout[%s]" % x).click()
        self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout[%s]" % y).click()
        self.driver.find_element_by_xpath("//android.widget.ListView/android.widget.FrameLayout[%s]" % z).click()
        # 点击确定按钮
        self.driver.find_element_by_xpath("//android.widget.LinearLayout/android.widget.Button[1]").click()
        mylogger.info("确定发送")
    except Exception as e:
        self.driver.implicitly_wait(5)
        element_error(self, e)


def chat_voice_element(self):
    """返回触发语音按钮"""
    try:
        self.driver.implicitly_wait(5)
        ele_voice = self.driver.find_element_by_id("img_voice_key")
        return ele_voice
    except Exception as e:
        element_error_main_chat(self, e)


def chat_send_voice_element(self, t):
    try:
        self.driver.implicitly_wait(5)
        send_voice_ele = self.driver.find_element_by_id("recordbutton")
        # 创建 TouchAction 实例
        action1 = TouchAction(self.driver)
        # duration 长按时间 1000 基数为 1s
        action1.long_press(el=send_voice_ele, duration=t).wait(10000).perform()
    except Exception as e:
        element_error_main_chat(self, e)


def chat_emoji_element(self):
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.erlinyou.worldlist:id/img_exp").click()
    except Exception as e:
        element_error(self.driver, e)


def chat_emoji(self, n):
    """
    :param self:
    :param n: 第几个表情
    :return:
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//android.widget.GridView/android.widget.LinearLayout[%s]" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_type_emoji(self, n):
    """
    表情类型
    :param self:
    :param n: 第几种类型表情
    :return:
    """
    try:
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath(
            "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[%s]" % n).click()
    except Exception as e:
        element_error(self, e)


def chat_moving_emoji(self, n):
    """动图选择第n"""
    try:
        self.driver.implicitly_wait(5)
        # self.driver.find_element_by_xpath(
        #     "//android.widget.GridView/android.widget.LinearLayout[1]/android.widget.ImageView").click()
        self.driver.find_element_by_xpath("//android.widget.LinearLayout[%s]/android.widget.ImageView" % n).click()
    except Exception as e:
        element_error(self, e)
