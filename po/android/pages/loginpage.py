# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy
from common.basepage import BasePage
from po.android.pageobjects.input import Input
from utils.utils import Utils
from po.android.pageobjects.button import Button

class LoginPage(BasePage):
    def __init__(self, appium_driver):
        super(LoginPage, self).__init__(appium_driver)

# page object
    @property
    def account_input(self):
        return Utils.find_wait_for_visible(
            "account_input", Input, self.driver, (MobileBy.XPATH, '//android.widget.LinearLayout[@resource-id="cn.cj.pe:id/register_number"]//android.widget.EditText')
        )

    @property
    def passwd_input(self):
        return Utils.find_wait_for_visible(
            "passwd_input", Input, self.driver, (MobileBy.XPATH,  '//android.widget.LinearLayout[@resource-id="cn.cj.pe:id/register_password"]//android.widget.EditText')
        )

    @property
    def login_button(self):
        return Utils.find_wait_for_visible("login_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/login"))

# page logic
    def goto_message_list(self):
        self.logger.info("goto_message_list")
        self.account_input.send_keys("15827521823")
        self.passwd_input.send_keys("kt123456")
        self.login_button.click()
