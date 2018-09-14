# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import os
import unittest
from appium import webdriver
from common import globalvariable
from testcase import test_demo


if __name__ == "__main__":
    # desired_caps
    desired_caps = {
        "platformName": "Android",
        "PlatformVersion": "6.0",
        "deviceName": "GSL0217214000631",
        "appPackage": "cn.cj.pe",
        "appActivity": "com.mail139.about.LaunchActivity",
        "app": r"C:\Users\Administrator\Desktop\testForAppium\139Email.apk",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "unicodeKeyboard": "true",
        "resetKeyboard": "true",
        "noReset": True
    }

    desired_caps_bak = {
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

    # driver = webdriver.Remote(os.getenv('APPIUM_URL'), desired_caps)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    globalvariable.init(desired_caps.get("deviceName", "unknown"), desired_caps.get("platformName", "Android"))
    globalvariable.set_value("APPIUM_DRIVER", driver)
    suite = unittest.TestSuite()
    suite.addTests(test_demo.suite())
    report_file = os.path.join(globalvariable.get_value("TODAY_RESULT"), "Report.html")
    report_title = "Demo"
    desc = "Demo For Test"
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    '''
        with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite)
    '''
