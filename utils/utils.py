import logging

from appium.webdriver.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from common import globalvariable
from common.basepageobject import BasePageObject


class Utils:

    @classmethod
    def logger(cls):
        return logging.getLogger(globalvariable.get_value("LOGGER_NAME"))

    @classmethod
    def find_wait_for_present(cls, element_name, page_object_class, search_context, locator=None, default_time=30):
        driver = search_context
        search_locator = locator
        cls.logger().info("find_wait_for_present {}".format(element_name))
        try:
            if not locator:
                search_locator = page_object_class.LOCATOR
            web_element = WebDriverWait(driver, default_time).until(
                ec.presence_of_element_located(search_locator))
            return page_object_class(web_element, element_name)
        except Exception as e:
            raise e

    @classmethod
    def find_wait_for_visible(cls, element_name, page_object_class, search_context, locator=None, default_time=30):
        driver = search_context
        search_locator = locator
        cls.logger().info("find_wait_for_visible {}".format(element_name))
        try:
            if not locator:
                search_locator = page_object_class.LOCATOR
            web_element = WebDriverWait(driver, default_time).until(
                ec.visibility_of_element_located(search_locator))
            return page_object_class(web_element, element_name)
        except Exception as e:
            cls.logger().error("failed to locate {}".format(element_name))
            raise e

    @classmethod
    def wait_for_disappear(cls, element_name, appium_driver, element_obj, default_time=30):
        element = None
        if isinstance(element_obj, BasePageObject):
            element = element_obj.root

        if isinstance(element_obj, WebElement):
            element = element_obj
        cls.logger().info("wait_for_disappear {}".format(element_name))
        return WebDriverWait(appium_driver, default_time).until_not(ec.visibility_of(element))

    @classmethod
    def is_visible(cls, element_name, page_object_class, search_context, locator=None, default_time=10):
        try:
            cls.find_wait_for_visible(element_name, page_object_class, search_context, locator, default_time)
            return True
        except TimeoutException:
            logging.info("{} is not visible".format(element_name))
            return False
