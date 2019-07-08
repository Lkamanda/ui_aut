# home page 输入框详情页
from comm.element_error import element_error
from config.myconfig import *


def homepage_details_go_home_element(driver):
    """详情页回家"""
    try:
        driver.find_element_by_id("rl_home").click()
    except Exception as e:
        element_error(driver, e)


def homepage_details_go_home_cancel_element(driver):
    """详情页取消回家按钮"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/iv_home_delete")
    except Exception as e:
        element_error(driver, e)


def homepage_details_go_home_cancel_element_1(driver):
    """详情页取消回家按钮"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/iv_home_delete").click()
    except Exception as e:
        element_error(driver, e)


def homepage_details_go_home_add(driver):
    """详情页未添加回家"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/tv_home_set").click()
    except Exception as e:
        element_error(driver, e)


def homepage_details_go_home_add_1(driver):
    """详情页未添加回家"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/tv_home_set")
    except Exception as e:
        element_error(driver, e)


def homepage_details_go_company_element(driver):
    """详情页回公司"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/rl_company").click()
    except Exception as e:
        element_error(driver, e)


def homepage_details_go_company_add_element(driver):
    """添加公司"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/tv_company_set").click()
    except Exception as e:
        element_error(driver, e)


def homepage_details_go_company_cancel_element(driver):
    """取消公司"""
    try:
        driver.find_element_by_id("com.erlinyou.worldlist:id/iv_company_delete")
    except Exception as e:
        element_error(driver, e)