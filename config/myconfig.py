import os
from config.choice_config import choiceConfig


def read_config_text():
    # path = get_path()
    # f = open(path, encoding='utf-8')
    f = open(r"C:\Users\zhoujialin\PycharmProjects\ui_aut\config\send_config.txt", encoding='utf-8')
    # f = open(r"send_config.txt", encoding='utf-8')
    chat_str3 = f.read()
    f.close()
    return chat_str3


class MyConfig:
    def __init__(self):
        # 通过设置config_number来控制不同版本的配置和校验方式
        self.config_number = 1
        self.chat_str_0 = "d发斯蒂芬斯蒂芬德生科技付款了的房价快速的减肥肯定是放假快乐的实际付款时代峻峰"
        self.chat_str_1 = "华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯华为备胎芯"
        self.chat_str_2 = "%s" % read_config_text()
        self.mobile_number = "13231533164"
        self.mobile_password = str(u"5211314")
        if self.config_number == 0:
            print("进入研发版")
            self.place_input = [u"北京西站", u"上地五街", u"beijing", u"龙泽苑西区南门", u" 北京市昌平区回龙关西大街111号", u"搜狗", u"奥林匹克公园", u"望京soho"]
            self.home_page_details_input = [u"龙泽苑西区"]
            self.rename_text = u"重命名收藏地点"
            self.new_trip_input_text = [u"北京一日游"]
            self.new_trip_add_place = [u"望京SOHO", u"天安门", u"天坛", u"搜狗"]
            self.setting_city = u"北京市"
        elif self.config_number == 1:
            print("进入发布版")
            self.place_input = [u"北京西站", u"上地五街", u"beijing", u"埃菲尔铁塔", u" 北京市昌平区回龙关西大街111号", u"搜狗", u"奥林匹克公园",
                                u"巴黎圣母"]
            self.home_page_details_input = [u"龙泽苑西区"]
            self.rename_text = u"重命名收藏地点"
            self.new_trip_input_text = [u"北京一日游"]
            self.new_trip_add_place = [u"望京SOHO", u"天安门", u"天坛", u"搜狗"]
            self.setting_city = "巴黎"

    def get_mobile_number(self):
        return self.mobile_number

    def get_mobile_password(self):
        return self.mobile_password

    def get_place_share_search(self, n):
        """
        对place 页面返回搜索值
        :param
        n = 0 ： 地点
        n = 1 :  街道
        n = 2 :  城市
        n = 3 :  家
        n = 4 :  门牌号
        n = 5 :  搜狗
        n = 6 :  奥林匹克公园
        n = 7 :  公司
        :return: place
        """
        return self.place_input[n]

    def get_chat_str(self, n):
        if n == 0:
            return self.chat_str_0
        elif n == 1:
            return self.chat_str_1
        elif n == 2:
            return self.chat_str_2

    def get_rename_text(self):
        """收藏 地点重命名"""
        return self.rename_text

    def get_new_trip_input_text(self, n):
        """新建行程 输入内容"""
        return self.new_trip_input_text[n]

    def get_new_trip_add_place(self, n):
        """ 添加行程地点 输入输入内容"""
        return self.new_trip_add_place[n]

    def get_setting_city(self):
        """返回当前城市设置text"""
        return self.setting_city

myconfig = MyConfig()



