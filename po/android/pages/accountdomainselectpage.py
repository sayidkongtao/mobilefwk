# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'


from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from utils.utils import Utils


class AccountDomainsSelectPage(BasePage):
    def __init__(self, appium_driver):
        super(AccountDomainsSelectPage, self).__init__(appium_driver)

# page object
    @property
    def email139_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, "//android.widget.ListView/android.widget.RelativeLayout[1]"),
            "email139_button",
            "AccountDomainsSelectPage",
            self.driver
        )

# page logic

    def goto_login(self):
        self.logger.info("goto_login")
        self.email139_button.click()
