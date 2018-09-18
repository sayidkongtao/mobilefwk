# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.ios.pageobjects.button import Button
from po.ios.pageobjects.input import Input
from po.ios.pageobjects.text import Text
from utils.utils import Utils


class ContactListPage(BasePage):
    def __init__(self, appium_driver):
        super(ContactListPage, self).__init__(appium_driver)

    @property
    def title(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="PMContactVC"]/XCUIElementTypeButton[1]'),
            "联系人",
            "ContactListPage",
            self.driver
        )

    @property
    def search_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="PMContactVC"]/XCUIElementTypeButton[2]'),
            "Search Button",
            "ContactListPage",
            self.driver
        )

    @property
    def search_input(self):
        return Utils.find(
            Input,
            (MobileBy.XPATH, '//XCUIElementTypeSearchField[@name="搜索"]'),
            "联系人搜索框",
            "ContactListPage",
            self.driver
        )

    def first_contact(self, value):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '(//XCUIElementTypeStaticText[@name="{}"])[2]'.format(value)),
            "第一个联系人",
            "ContactListPage",
            self.driver
        )

    #  page logic
    def search_then_select_to_contentdetails(self, value):
        self.search_button.click()
        self.search_input.send_keys(value)
        text = self.first_contact(value).text()
        self.first_contact(value).click()
        return text
