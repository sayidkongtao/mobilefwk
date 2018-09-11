from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject
from utils.utils import Utils
from po.android.pageobjects.input import Input
from po.android.pageobjects.text import Text


class ContactItem(BasePageObject):
    LOCATOR = (MobileBy.XPATH, '//android.widget.LinearLayout[@resource-id="cn.cj.pe:id/item"]')

    def __init__(self, web_element, element_name="base"):
        super(ContactItem, self).__init__(web_element, element_name)

# page object
    @property
    def select_checkbox(self):
        return Utils.find_wait_for_visible(
            "select_checkbox", Input, self.root, (MobileBy.XPATH, ".//android.widget.CheckBox")
        )

    @property
    def contact_name(self):
        return Utils.find_wait_for_visible(
            "contact_name", Text, self.root, (MobileBy.XPATH, './/android.widget.TextView[@resource-id="cn.cj.pe:id/name"]')
        )

    @property
    def email_text(self):
        return Utils.find_wait_for_visible(
            "email_text", Text, self.root, (MobileBy.XPATH, './/android.widget.TextView[@resource-id="cn.cj.pe:id/email"]')
        )

