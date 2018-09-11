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
        return Utils.find_wait_for_visible("refresh_quee_view_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/refresh_quee_view"))

    @property
    def is_refresh_quee_view_button_visible(self):
        return Utils.is_visible(
            "refresh_quee_view_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/refresh_quee_view")
        )

    @property
    def write_email_button(self):
        return Utils.find_wait_for_visible(
            "write_email_button", Button, self.driver, (MobileBy.XPATH, '(//android.widget.ImageView[@content-desc="image"])[3]')
        )

    @property
    def is_write_email_button_visible(self):
        return Utils.is_visible("write_email_button", Button, self.driver, (MobileBy.XPATH, '(//android.widget.ImageView[@content-desc="image"])[3]'))

    @property
    def close_button(self):
        return Utils.find_wait_for_visible(
            "close_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/close")
        )

    @property
    def is_close_button_visible(self):
        return Utils.is_visible(
            "close_button", Button, self.driver, (MobileBy.ID, "cn.cj.pe:id/close")
        )


# page logic
    def check_update(self):
        self.logger.info("check whether has version update")
        if self.is_close_button_visible:
            self.logger.info("close version update")
            self.close_button.click()
        else:
            self.logger.info("no version update")

    def goto_write_email_page(self):
        self.write_email_button.click()

    def wait_for_page_fresh(self):
        if self.is_refresh_quee_view_button_visible:
            Utils.wait_for_disappear("refresh_quee_view_button", self.driver, self.refresh_quee_view_button)
