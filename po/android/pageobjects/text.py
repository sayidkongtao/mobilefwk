from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject


class Text(BasePageObject):
    LOCATOR = (MobileBy.XPATH, "//android.widget.TextView")

    def __init__(self, web_element, element_name="base"):
        super(Text, self).__init__(web_element, element_name)
