# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import logging
import os
import time

from appium.webdriver.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from common import globalvariable

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

    def __capture_screenshot(self, result):
        capture_driver = self.__driver
        # Capture the screen for each action
        if isinstance(self.__driver, WebElement):
            capture_driver = self.__driver.parent
        folder = globalvariable.get_value("test_method", "unknown")
        try:
            today_result = globalvariable.get_value("TODAY_RESULT")
            screenshot_path = os.path.join(today_result,
                                           "screenshot",
                                           folder
                                           )
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)
            capture_driver.save_screenshot(
                os.path.join(
                    screenshot_path,
                    self.page_name + "_" + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())) + "_"
                    + result + ".png"
                )
            )
        except Exception as e:
            self.logger.warning("failed to capture the screenshot, {}".format(e))
            # folder = "unknown"

    def find_element(self, visible=True):
        result = "pass"
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
            self.__capture_screenshot(result)

    def find_elements(self, visible=True):
        result = "pass"
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
            result = "failed"
            raise e

        finally:
            self.__capture_screenshot(result)

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
        text = ""
        try:
            self.logger.info("get text of element {} on page {}".format(self.element_name, self.page_name))
            text = self.find_element(self.locator).text
            self.logger.info("element {} text is: {} on page".format(self.element_name, text, self.page_name))
        except Exception as e:
            self.logger.warning(e)
            self.logger.info("Failed to get the text, so return the default value: ".format(" "))
        return text

    def press_key(self, code):
        try:
            self.__driver.press_keycode(code)
        except Exception as e:
            self.logger.error(e)
            raise e

    def set_value_by_keys(self, value):
        self.logger.info("set {} into element {} on page".format(value, self.element_name, self.page_name))
        letterToCodeHashMap = {}
        lettersStr = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z @ . + _ 0 1 2 3 4 5 6 7 8 9".split()
        androidCodes = [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                        53, 54, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                        51, 52, 53, 54, 77, 56, 81, 69, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        for index in range(len(lettersStr)):
            letterToCodeHashMap[lettersStr[index]] = androidCodes[index]
        for i in range(len(value)):
            code = letterToCodeHashMap.get(value[i])
            self.press_key(code)
            time.sleep(0.5)

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
