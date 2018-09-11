# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy
from common.basepage import BasePage
from po.android.pageobjects.button import Button
from utils.utils import Utils
import time

class NavigationPage(BasePage):
    def __init__(self, appium_driver):
        super(NavigationPage, self).__init__(appium_driver)

# page object
    @property
    def start_button(self):
        return Utils.find_wait_for_visible("start_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/bt_start"))

# page logic
    def goto_accountdomainselect(self):
        self.logger.info("goto_accountdomainselect")
        time.sleep(3)
        self.swipe_left()
        self.swipe_left()
        self.start_button.click()
