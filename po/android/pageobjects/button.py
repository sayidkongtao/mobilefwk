from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject


class Button(BasePageObject):
    LOCATOR = (MobileBy.XPATH, "android.widget.Button")

    def __init__(self, locator, element_name, page_name, search_context, default_time=30):
        super(Button, self).__init__(locator, element_name, page_name, search_context, default_time)
