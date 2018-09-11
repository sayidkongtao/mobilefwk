from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject
from po.android.pageobjects.contactitem import ContactItem
from utils.utils import Utils


class ContactList(BasePageObject):
    LOCATOR = (MobileBy.ID, "cn.cj.pe:id/contact_list")

    def __init__(self, web_element, element_name="base"):
        super(ContactList, self).__init__(web_element, element_name)

# page object
    @property
    def first_contact(self):
        return Utils.find_wait_for_visible(
            "first_contact", ContactItem, self.root, (MobileBy.XPATH, './/android.widget.LinearLayout[@resource-id="cn.cj.pe:id/item"]')
        )

# page logic


