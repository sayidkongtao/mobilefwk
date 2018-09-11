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
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/bt_start"),
            "start_button",
            "NavigationPage",
            self.driver
        )

# page logic
    def at_page(self):
        self.logger.info("Wait for page: NavigationPage")
        Utils.wait_until_condition(lambda: self.driver.current_activity == "com.mail139.about.GuiderPagerActivity")

    def goto_accountdomainselect(self):
        self.logger.info("goto_accountdomainselect")
        self.at_page()
        self.swipe_left()
        self.swipe_left()
        self.start_button.click()
