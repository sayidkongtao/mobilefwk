# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

import logging
import os
import unittest

from common import globalvariable
from po.ios.androdpages import IOSPages

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class CommonUnittest(unittest.TestCase):

    def setUp(self):
        self.logger.info("start to test: {}".format(self._testMethodName))

    def tearDown(self):
        pass
        # result = self.defaultTestResult()
        # self._feedErrorsToResult(result, self._outcome.errors)
        # self.logger.info("Result of test case: {} is : {}".format(self._testMethodName, result.wasSuccessful()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @classmethod
    def setUpBeforeClass(cls):
        # globalvariable.init(cls.desired_caps.get("deviceName", cls.desired_caps.get("PLATFORMNAME", "default_android")))
        cls.driver = globalvariable.get_value("APPIUM_DRIVER")
        cls.logger = logging.getLogger(globalvariable.get_value("LOGGER_NAME"))
        cls.android_pages = IOSPages(cls.driver)
