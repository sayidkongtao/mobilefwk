# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from utils.utils import Utils
from po.android.pageobjects.text import Text


class WriteEmailPage(BasePage):
    def __init__(self, appium_driver):
        super(WriteEmailPage, self).__init__(appium_driver)

    @property
    def add_to_button(self):
        return Utils.find_wait_for_visible(
            "add_to_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/add_to")
        )

    @property
    def add_cc_button(self):
        return Utils.find_wait_for_visible(
            "add_cc_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/add_cc")
        )

    @property
    def add_bcc_button(self):
        return Utils.find_wait_for_visible(
            "add_bcc_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/add_bcc")
        )

    @property
    def first_receiver(self):
        return Utils.find_wait_for_visible(
            "first_receiver", Text, self.driver, (MobileBy.XPATH, '//android.widget.RelativeLayout[@resource-id="cn.cj.pe:id/to_layout"]//android.view.View//android.widget.TextView')
        )

    @property
    def warning_message(self):
        return Utils.find_wait_for_visible(
            "warning_message", Text, self.driver, (MobileBy.ID, 'cn.cj.pe:id/message')
        )

    @property
    def send_direct_button(self):
        return Utils.find_wait_for_visible(
            "send_direct_button", Button, self.driver, (MobileBy.ID, 'cn.cj.pe:id/right')
        )

    @property
    def send_success_img(self):
        return Utils.find_wait_for_visible(
            "send_success_img", Text, self.driver, (MobileBy.ID, 'cn.cj.pe:id/gif_success_img')
        )

    @property
    def back_to_email_button(self):
        return Utils.find_wait_for_visible(
           "back_to_email_button", Button, self.driver, (MobileBy.ID, 'cn.cj.pe:id/back_to_list')
        )

# page logic
    def at_write_email_page(self):
        return Utils.is_visible(
            "add_to_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/add_to")
        )

    def goto_select_contact_page(self):
        self.logger.info("goto_select_contact_page")
        self.add_to_button.click()
