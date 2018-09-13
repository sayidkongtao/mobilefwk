# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.text import Text
from utils.utils import Utils


class ContactDetails(BasePage):
    def __init__(self, appium_driver):
        super(ContactDetails, self).__init__(appium_driver)

    @property
    def name(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/name'),
            "姓名",
            "ContactDetails",
            self.driver
        )

    @property
    def email(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//android.widget.LinearLayout[@resource-id="cn.cj.pe:id/hjl_email_container"]//\
            android.widget.TextView'),
            "邮箱地址",
            "ContactDetails",
            self.driver
        )

    @property
    def email_history(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//android.widget.TextView[@text="往来邮件"]'),
            "往来邮件",
            "ContactDetails",
            self.driver
        )

    # page logic
    def goto_email_history(self):
        self.email_history.click()
