# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import logging
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from common import globalvariable


class BasePageObject:

    # LOCATOR = (MobileBy.XPATH, "//button")

    def __init__(self, web_element, element_name):
        self.__root = web_element
        self.element_name = element_name
        self.logger = logging.getLogger(globalvariable.get_value("LOGGER_NAME"))

    @property
    def root(self):
        return self.__root

    def child_element(self, locator, visible=True, default_time=30):
        try:
            if visible:
                return WebDriverWait(self.__root, default_time).until(
                    ec.visibility_of_element_located(locator)
                )
            else:
                return WebDriverWait(self.__root, default_time).until(
                    ec.presence_of_element_located(locator)
                )
        except Exception as e:
            self.logger.error("%s 页面中未能找到 %s 元素" % (self, locator))
            raise e

    # 重新封装一组元素定位方法
    def child_elements(self, locator):
        try:
            if len(self.__root.find_elements(locator)):
                return self.__root.find_elements(locator)
        except Exception as e:
            self.logger.error("%s 页面中未能找到 %s 元素" % (self, locator))
            raise e

    # 重新封装输入方法
    def clear(self):
        try:
            self.logger.info("clear text on {}".format(self.element_name))
            self.__root.clear()
        except AttributeError as e:
            self.logger.error("%s 页面未能找到 %s 元素" % (self, self.element_name))
            raise e

    # 重新封装输入方法
    def send_keys(self, value, clear_first=False, click_first=False):
        try:
            if click_first:
                self.click()
            if clear_first:
                self.clear()
            self.logger.info("set {} into {}".format(value, self.element_name))
            self.root.send_keys(value)
        except AttributeError as e:
            self.logger.error("%s 页面未能找到 %s 元素" % (self, self.element_name))
            raise e

    # 重新封装按钮点击方法
    def click(self):
        try:
            self.logger.info("Click element {}".format(self.element_name))
            self.__root.click()
        except AttributeError as e:
            self.logger.error("%s 页面未能找到 %s 按钮" % (self, self.element_name))
            raise e

    def text(self):
        try:
            self.logger.info("get element {} text".format(self.element_name))
            text = self.__root.text
            self.logger.info("get element {} text: {}".format(self.element_name, text))
            return text
        except AttributeError as e:
            self.logger.error("%s 页面未能找到 %s 文本" % (self, self.element_name))
            raise e
