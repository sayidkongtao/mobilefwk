# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject
from po.ios.pageobjects.input import Input
from po.ios.pageobjects.text import Text
from utils.utils import Utils


class ContactItem(BasePageObject):
    LOCATOR = (MobileBy.XPATH, '//ios.widget.LinearLayout[@resource-id="cn.cj.pe:id/item"]')

    def __init__(self, locator, element_name, page_name, search_context, default_time=30):
        super(ContactItem, self).__init__(locator, element_name, page_name, search_context, default_time)

# page object
    @property
    def select_checkbox(self):
        return Utils.find(
            Input,
            (MobileBy.XPATH, ".//ios.widget.CheckBox"),
            "select_checkbox",
            "ContactItem",
            self.root
        )

    @property
    def contact_name(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, './/ios.widget.TextView[@resource-id="cn.cj.pe:id/name"]'),
            "contact_name",
            "ContactItem",
            self.root
        )

    @property
    def email_text(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, './/ios.widget.TextView[@resource-id="cn.cj.pe:id/email"]'),
            "email_text",
            "ContactItem",
            self.root
        )