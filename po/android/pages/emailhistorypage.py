# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.text import Text
from utils.utils import Utils


class EmailHistoryPage(BasePage):
    def __init__(self, appium_driver):
        super(EmailHistoryPage, self).__init__(appium_driver)

    @property
    def first_email_sender(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/sender'),
            "first_email_sender",
            "EmailHistory",
            self.driver
        )

    # page logic
    def goto_email_content(self):
        self.logger.info("goto_email_content")
        text = self.first_email_sender.text()
        self.first_email_sender.click()
        return text
