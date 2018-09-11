from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject


class Input(BasePageObject):
    LOCATOR = (MobileBy.XPATH, "//android.widget.EditText")

    def __init__(self, web_element, element_name="base"):
        super(Input, self).__init__(web_element, element_name)
