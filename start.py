# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

import os
import unittest

from appium import webdriver

from common import globalvariable
from public.HTMLTestRunner import HTMLTestRunner
from testcase import test_demo

if __name__ == "__main__":
    # desired_caps
    desired_caps_loc = {
        "platformName": "Android",
        "PlatformVersion": "6.0",
        "deviceName": "HC43YWW01974",
        "appPackage": "cn.cj.pe",
        "appActivity": "com.mail139.about.LaunchActivity",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "noReset": True
    }

    desired_caps = {
        "platformName": os.getenv('APPIUM_PLATFORM'),
        "PlatformVersion": os.getenv('APPIUM_DEVICE_VERSION'),
        "deviceName": os.getenv('APPIUM_DEVICE_NAME'),
        "appPackage": os.getenv('APPIUM_APP_PACKAGE'),
        "appActivity": os.getenv('APPIUM_APP_ACTIVITY'),
        "app": os.getenv('APPIUM_APP_FILE'),
        "newCommandTimeout": os.getenv('APPIUM_NEW_COMMAND_TIMEOUT'),
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "noReset": True
    }

    driver = webdriver.Remote(os.getenv('APPIUM_URL'), desired_caps)
    # driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    globalvariable.init(desired_caps.get("deviceName", "unknown"), desired_caps.get("platformName", "Android"))
    globalvariable.set_value("APPIUM_DRIVER", driver)
    suite = unittest.TestSuite()
    suite.addTests(test_demo.suite())
    report_file = os.path.join(globalvariable.get_value("TODAY_RESULT"), "Report.html")
    report_title = "Demo"
    desc = "Demo For Test"

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
