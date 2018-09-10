# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from utils.utils import Utils

'''
example 页面元素 - 操作方法 -> 封装
'''


class ExamplePage(BasePage):
    def __init__(self, appium_driver):
        super(ExamplePage, self).__init__(appium_driver)

    @property
    def button_1(self):
        return Utils.find_wait_for_visible("button_1", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/bt_start"))

    def click_button_1(self):
        self.button_1.click()
