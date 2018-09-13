# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'


from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject
from po.android.pageobjects.contactitem import ContactItem
from utils.utils import Utils


class ContactList(BasePageObject):
    LOCATOR = (MobileBy.ID, "cn.cj.pe:id/contact_list")

    def __init__(self, locator, element_name, page_name, search_context, default_time=30):
        super(ContactList, self).__init__(locator, element_name, page_name, search_context, default_time)

# page object
    @property
    def first_contact(self):
        return Utils.find(
            ContactItem,
            (MobileBy.XPATH, './/android.widget.LinearLayout[@resource-id="cn.cj.pe:id/item"]'),
            "first_contact",
            "ContactList",
            self.root
        )

# page logic
