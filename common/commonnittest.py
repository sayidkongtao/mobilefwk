# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

import logging
import os
import unittest

from appium import webdriver

from common import globalvariable
from po.android.androdpages import AndroidPages

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class CommonUnittest(unittest.TestCase):
    desired_caps = {
        "platformName": "Android",
        "PlatformVersion": "6.0",
        "deviceName": "HC43YWW01974",
        "appPackage": "cn.cj.pe",
        "appActivity": "com.mail139.about.LaunchActivity",
        "app": PATH(os.path.join(".." + os.sep, "data", "package", "android", "PE-V8.1.3.apk")),
        "newCommandTimeout": 7200,
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "chromedriverExecutableDir": r"C:\Users\Administrator\Desktop\testForAppium\chrome_driver",
        "chromedriverChromeMappingFile": r"C:\Users\Administrator\Desktop\testForAppium\mapping.json"
    }

    @classmethod
    def setUpBeforeClass(cls):
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cls.desired_caps)
        globalvariable.init(cls.desired_caps.get("deviceName", None))
        cls.logger = logging.getLogger(globalvariable.get_value("LOGGER_NAME"))
        cls.android_pages = AndroidPages(cls.driver)
