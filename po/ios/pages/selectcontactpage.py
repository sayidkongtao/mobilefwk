# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.ios.pageobjects.button import Button
from po.ios.pageobjects.input import Input
from po.ios.pageobjects.text import Text
from utils.utils import Utils


class SelectContactPage(BasePage):
    def __init__(self, appium_driver):
        super(SelectContactPage, self).__init__(appium_driver)

    @property
    def search_input(self):
        return Utils.find(
            Input,
            (MobileBy.XPATH,
             '//XCUIElementTypeImage[@name="nav_btn_search_focused"]//parent::XCUIElementTypeOther//XCUIElementTypeSearchField'),
            "search_input",
            "SelectContactPage",
            self.driver
        )

    @property
    def confirm_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, "确定"),
            "确定",
            "SelectContactPage",
            self.driver
        )

    # contact group
    @property
    def contact_group(self):
        return Utils.find(
            Button,
            (MobileBy.ID, '联系人分组'),
            "联系人分组",
            "SelectContactPage",
            self.driver
        )

    def contact_group_by_name(self, group_name):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, group_name),
            group_name,
            "SelectContactPage",
            self.driver
        )

    def first_person_under_search(self, name):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//XCUIElementTypeStaticText[contains(@name,"{}")]'.format(name)),
            "First Person",
            "SelectContactPage",
            self.driver
        )

    def first_person_under_selected_group(self, group_name):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '(//XCUIElementTypeStaticText[@name="{}"]//parent::XCUIElementTypeCell/following-sibling::XCUIElementTypeCell//XCUIElementTypeStaticText)[2]'.format(
                 group_name)),
            "First Person",
            "SelectContactPage",
            self.driver
        )


# page Logic

    def select_first_contact(self, value):
        self.search_input.click()
        self.accept_right()
        self.search_input.send_keys(value)
        self.first_person_under_search(value).click()
        self.confirm_button.click()
        return value

    def search_then_select(self, value):
        return self.select_first_contact(value)

    def select_under_group(self, group_name, value):
        self.contact_group.click()
        self.contact_group_by_name(group_name).click()
        self.first_person_under_selected_group(group_name).click()
        self.confirm_button.click()
        return value
