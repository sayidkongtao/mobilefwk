# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from common import globalvariable
from selenium.common.exceptions import TimeoutException
from appium.webdriver.webelement import WebElement
import os
import time

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BasePageObject(object):

    # LOCATOR = (MobileBy.XPATH, "//button")

    def __init__(self, locator, element_name, page_name, search_context, default_time=30):
        self.locator = locator
        self.element_name = element_name
        self.__driver = search_context
        self.page_name = page_name
        self.default_time = default_time
        self.logger = logging.getLogger(globalvariable.get_value("LOGGER_NAME"))

    @property
    def root(self):
        return self.find_element(self.locator)

    def find_element(self, visible=True):
        result = "pass"
        capture_driver = self.__driver
        try:
            if visible:
                return WebDriverWait(self.__driver, self.default_time).until(
                    ec.visibility_of_element_located(self.locator)
                )
            else:
                return WebDriverWait(self.__driver, self.default_time).until(
                    ec.presence_of_element_located(self.locator)
                )
        except Exception as e:
            self.logger.error(
                "on {} cannot find element: {}, locator: {}".format(self.page_name, self.element_name, self.locator)
            )
            result = "failed"
            raise e

        finally:
            if isinstance(self.__driver, WebElement):
                capture_driver = self.__driver.parent
            folder = globalvariable.get_value("test_method", "unknown")
            try:
                today_result = globalvariable.get_value("TODAY_RESULT")
                screenshot_path = os.path.join(today_result,
                                               "screenshot" + globalvariable.get_value("PROJECT_START_DAY"),
                                               folder
                                               )
                if not os.path.exists(screenshot_path):
                    os.mkdir(screenshot_path)
                capture_driver.save_screenshot(
                    os.path.join(
                        screenshot_path,
                        self.page_name + time.strftime('%Y-%m-%d', time.localtime(time.time())) + result
                    )
                )
            except Exception as e:
                print e
            finally:
                print "failed to capture the screenshot"
                folder = "unknown"

    def find_elements(self, visible=True):
        try:
            if visible:
                WebDriverWait(self.__driver, self.default_time).until(
                    ec.visibility_of_all_elements_located(self.locator)
                )
            else:
                WebDriverWait(self.__driver, self.default_time).until(
                    ec.presence_of_all_elements_located(self.locator)
                )

        except Exception as e:
            self.logger.error(
                "on {} cannot find elements: {}, locator: {}".format(self.page_name, self.element_name, self.locator)
            )
            raise e

    def clear(self):
        self.logger.info("clear text on element {} on page".format(self.element_name, self.page_name))
        self.find_element(self.locator).clear()

    def send_keys(self, value, clear_first=False, click_first=False):
        if click_first:
            self.click()
        if clear_first:
            self.clear()
        self.logger.info("set {} into element {} on page".format(value, self.element_name, self.page_name))
        self.find_element(self.locator).send_keys(value)

    def click(self):
        self.logger.info("Click element {} on page {}".format(self.element_name, self.page_name))
        self.find_element(self.locator).click()

    def text(self):
        self.logger.info("get text of element {} on page {}".format(self.element_name, self.page_name))
        text = self.find_element(self.locator).text
        self.logger.info("element {} text is: {} on page".format(self.element_name, text, self.page_name))
        return text

    def is_visible(self, default_time=10):
        try:
            WebDriverWait(self.__driver, default_time).until(
                ec.visibility_of_element_located(self.locator)
            )
            self.logger.info(
                "to check element {} on page {} visible: {}".format(self.element_name, self.page_name, True)
            )
            return True
        except TimeoutException:
            self.logger.info(
                "to check element {} on page {} visible: {}".format(self.element_name, self.page_name, False)
            )
            return False

    def to_disappear(self, default_time=45):
        try:
            WebDriverWait(self.__driver, default_time).until_not(
                ec.visibility_of_element_located(self.locator)
            )
            self.logger.info(
                "to check element {} on page {} disappear: {}".format(self.element_name, self.page_name, True)
            )
        except TimeoutException:
            self.logger.info(
                "to check element {} on page {} disappear: {}".format(self.element_name, self.page_name, False)
            )
