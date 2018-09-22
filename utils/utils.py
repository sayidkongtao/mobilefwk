# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'


import logging
import time

from appium.webdriver.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from common import globalvariable
from common.basepageobject import BasePageObject


class Utils:

    @classmethod
    def logger(cls):
        return logging.getLogger(globalvariable.get_value("LOGGER_NAME"))

    @classmethod
    def find(cls, page_object_class, locator, element_name, page_name, search_context, default_time=30):
        obj = page_object_class(locator, element_name, page_name, search_context, default_time)
        if isinstance(obj, BasePageObject):
            return obj

    @classmethod
    def find_visible(cls, page_object_class, locator, element_name, page_name, search_context, default_time=30):
        cls.logger().info("find_wait_for_visible {} on page {}, locator: {}".format(element_name, page_name, locator))
        obj = page_object_class(locator, element_name, page_name, search_context, default_time)
        obj.find_element()
        if isinstance(obj, BasePageObject):
            return obj

    @classmethod
    def find_present(cls, page_object_class, locator, element_name, page_name, search_context, default_time=30):
        cls.logger().info("find_wait_for_visible {} on page {}, locator: {}".format(element_name, page_name, locator))
        obj = page_object_class(locator, element_name, page_name, search_context, default_time)
        obj.find_element(False)
        if isinstance(obj, BasePageObject):
            return obj

    @classmethod
    def wait_disappear(cls, element_obj, appium_driver=None, default_time=30):
        if isinstance(element_obj, BasePageObject):
            element_obj.to_disappear()

        if isinstance(element_obj, WebElement):
            cls.logger().info("wait_for_disappear {}".format(
                element_obj.text if element_obj.text != "" else element_obj.tag_name)
            )
            WebDriverWait(appium_driver, default_time).until_not(ec.visibility_of(element_obj))

    @classmethod
    def wait_until_condition(cls, method, default_time=30):
        end_time = time.time() + default_time
        while True:
            try:
                value = method()
                if value:
                    return value
            except Exception as e:
                cls.logger().warning("Can ignore this info ".format(e))
                cls.logger().info("Continue to wait")
            time.sleep(2)
            if time.time() > end_time:
                break
        raise Exception("Timeout to wait for condition")

    @classmethod
    def now(cls):
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    @classmethod
    def wait_time(cls, secs):
        time.sleep(secs)
