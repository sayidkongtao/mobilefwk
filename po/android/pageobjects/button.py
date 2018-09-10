from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject


class Button(BasePageObject):
    LOCATOR = (MobileBy.XPATH, "//button")

    def __init__(self, web_element, element_name="base"):
        super(Button, self).__init__(web_element, element_name)
