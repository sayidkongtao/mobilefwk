# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from utils.utils import Utils
from po.android.pageobjects.contactist import ContactList


class SelectContactPage(BasePage):
    def __init__(self, appium_driver):
        super(SelectContactPage, self).__init__(appium_driver)

    @property
    def confirm_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/headicon_text"),
            "confirm_button",
            "SelectContactPage",
            self.driver
        )

    @property
    def contact_list(self):
        return Utils.find_visible(
            ContactList,
            (MobileBy.ID, "cn.cj.pe:id/contact_list"),
            "contact_list",
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
