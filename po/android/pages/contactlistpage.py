# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from po.android.pageobjects.input import Input
from po.android.pageobjects.text import Text
from utils.utils import Utils


class ContactListPage(BasePage):
    def __init__(self, appium_driver):
        super(ContactListPage, self).__init__(appium_driver)

    @property
    def title(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/actionbar_sub_title'),
            "联系人",
            "ContactListPage",
            self.driver
        )

    @property
    def search_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, '//android.widget.ImageView'),
            "Search Button",
            "ContactListPage",
            self.driver
        )

    @property
    def search_input(self):
        return Utils.find(
            Input,
            (MobileBy.ID, "cn.cj.pe:id/search"),
            "联系人搜索框",
            "ContactListPage",
            self.driver
        )

    @property
    def first_contact(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/name'),
            "第一个联系人",
            "ContactListPage",
            self.driver
        )

    #  page logic
    def search_then_select_to_(self, value):
        Utils.wait_time(2)
        self.search_button.click()
        Utils.wait_time(3)
        self.search_input.send_keys(value)
        text = self.first_contact.text()
        self.first_contact.click()
        return text
