# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy
from common.basepage import BasePage
from po.android.pageobjects.button import Button
from utils.utils import Utils


class MessageListPage(BasePage):
    def __init__(self, appium_driver):
        super(MessageListPage, self).__init__(appium_driver)

    @property
    def refresh_quee_view_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/refresh_quee_view"),
            "refresh_quee_view_button",
            "MessageListPage",
            self.driver
        )

    @property
    def write_email_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.XPATH, '(//android.widget.ImageView[@content-desc="image"])[3]'),
            "write_email_button",
            "MessageListPage",
            self.driver
        )

    @property
    def close_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/close"),
            "close_button",
            "MessageListPage",
            self.driver
        )

# page logic
    def at_message_list_page(self):
        return self.write_email_button.is_visible()

    def check_update(self):
        self.logger.info("check whether has version update")
        close_button = self.close_button

        if close_button.is_visible():
            self.logger.info("close version update")
            close_button.click()
        else:
            self.logger.info("no version update")
        return self

    def goto_write_email_page(self):
        self.logger.info("goto_write_email_page")
        self.write_email_button.click()

    def wait_for_page_fresh(self):
        refresh_quee_view_button = self.refresh_quee_view_button
        if refresh_quee_view_button.is_visible():
            Utils.wait_disappear(refresh_quee_view_button)
