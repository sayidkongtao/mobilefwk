# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from po.android.pageobjects.contactist import ContactList
from po.android.pageobjects.input import Input
from po.android.pageobjects.text import Text
from utils.utils import Utils


class SelectContactPage(BasePage):
    def __init__(self, appium_driver):
        super(SelectContactPage, self).__init__(appium_driver)

    @property
    def search_input(self):
        return Utils.find(
            Input,
            (MobileBy.ID, "cn.cj.pe:id/search"),
            "search_input",
            "SelectContactPage",
            self.driver
        )

    @property
    def confirm_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/headicon_text"),
            "确定",
            "SelectContactPage",
            self.driver
        )

    @property
    def contact_list(self):
        return Utils.find(
            ContactList,
            (MobileBy.ID, "cn.cj.pe:id/contact_list"),
            "contact_list",
            "SelectContactPage",
            self.driver
        )

    # contact group
    @property
    def contact_group(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/tv_contact_group'),
            "联系人分组",
            "SelectContactPage",
            self.driver
        )

    @property
    def read_group(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//android.widget.TextView[@text="读信联系人"]'),
            "读信联系人",
            "SelectContactPage",
            self.driver
        )

    @property
    def first_person_under_selected_group(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//android.widget.TextView[@resource-id="cn.cj.pe:id/name"]'),
            "First Person",
            "SelectContactPage",
            self.driver
        )


# page Logic

    def select_first_contact(self):
        contact = self.contact_list.first_contact
        contact.click()
        context = {
            "name": contact.contact_name.text(),
            "email": contact.email_text.text()
        }
        self.confirm_button.click()
        return context

    def search_then_select(self, value):
        self.search_input.send_keys(value)
        return self.select_first_contact()

    def select_under_group(self):
        self.contact_group.click()
        self.read_group.click()
        self.first_person_under_selected_group.click()
        text = self.first_person_under_selected_group.text()
        self.confirm_button.click()
        return text
