# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.ios.pageobjects.text import Text
from utils.utils import Utils


class ContactDetails(BasePage):
    def __init__(self, appium_driver):
        super(ContactDetails, self).__init__(appium_driver)

    @property
    def title(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//XCUIElementTypeStaticText[@name="联系人详情"]'),
            "联系人详情"
            "ContactDetails",
            self.driver
        )

    @property
    def name(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '(//XCUIElementTypeNavigationBar[@name="联系人详情"]//following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[1]'),
            "姓名",
            "ContactDetails",
            self.driver
        )

    @property
    def email(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '//XCUIElementTypeImage[@name="contacts_ic_email_normal"]//following-sibling::XCUIElementTypeStaticText'),
            "邮箱地址",
            "ContactDetails",
            self.driver
        )

    @property
    def email_history(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '往来邮件'),
            "往来邮件",
            "ContactDetails",
            self.driver
        )

    # page logic
    def at(self):
        Utils.wait_until_condition(lambda: self.title.is_visible())

    def goto_email_history(self):
        self.email_history.click()
