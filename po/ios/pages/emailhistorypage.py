# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.ios.pageobjects.text import Text
from utils.utils import Utils


class EmailHistoryPage(BasePage):
    def __init__(self, appium_driver):
        super(EmailHistoryPage, self).__init__(appium_driver)

    @property
    def first_email_sender(self, value):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="{}"])[1]'.format(value)),
            "first_email_sender",
            "EmailHistory",
            self.driver
        )

    # page logic
    def goto_email_content(self, name):
        self.logger.info("goto_email_content")
        text = self.first_email_sender(name).text()
        self.first_email_sender(name).click()
        return text
