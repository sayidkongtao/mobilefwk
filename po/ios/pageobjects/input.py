# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'


from appium.webdriver.common.mobileby import MobileBy

from common.basepageobject import BasePageObject


class Input(BasePageObject):
    LOCATOR = (MobileBy.XPATH, "//ios.widget.EditText")

    def __init__(self, locator, element_name, page_name, search_context, default_time=30):
        super(Input, self).__init__(locator, element_name, page_name, search_context, default_time)
