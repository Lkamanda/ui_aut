from comm.element_error import element_error


def roam_page_look_more_element(self):
    """漫游页面查看更多"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/rl_heli_look_more").click()
    except Exception as e:
        element_error(self.driver, e)


def roam_page_goto_element(self):
    """到这去"""
    try:

        self.driver.find_element_by_id("com.erlinyou.worldlist:id/ll_top_map_mode_img").click()
    except Exception as e:
        element_error(self, e)


def roam_page_choice_ldmark(self, n):
    """选择当前页的第几个landmark"""
    try:

        self.driver.find_element_by_xpath("//android.widget.RelativeLayout[%s]"
                                          "/android.widget.RelativeLayout/android.widget.ImageView" % n).click()
    except Exception as e:
        element_error(self, e)
