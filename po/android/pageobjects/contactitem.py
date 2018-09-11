from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject
from utils.utils import Utils
from po.android.pageobjects.input import Input
from po.android.pageobjects.text import Text


class ContactItem(BasePageObject):
    LOCATOR = (MobileBy.XPATH, '//android.widget.LinearLayout[@resource-id="cn.cj.pe:id/item"]')

    def __init__(self, locator, element_name, page_name, search_context, default_time=30):
        super(ContactItem, self).__init__(locator, element_name, page_name, search_context, default_time)

# page object
    @property
    def select_checkbox(self):
        return Utils.find_visible(
            Input,
            (MobileBy.XPATH, ".//android.widget.CheckBox"),
            "select_checkbox",
            "ContactItem",
            self.root
        )

    @property
    def contact_name(self):
        return Utils.find_visible(
            Text,
            (MobileBy.XPATH, './/android.widget.TextView[@resource-id="cn.cj.pe:id/name"]'),
            "contact_name",
            "ContactItem",
            self.root
        )

    @property
    def email_text(self):
        return Utils.find_visible(
            Text,
            (MobileBy.XPATH, './/android.widget.TextView[@resource-id="cn.cj.pe:id/email"]'),
            "email_text",
            "ContactItem",
            self.root
        )

