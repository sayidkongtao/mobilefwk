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
        "platformName": "ios",
        "PlatformVersion": "11.4.1",
        "deviceName": "iPhone",
        "newCommandTimeout": 7200,
        "udid": "17d28db11b1d8266059ec407dfda8dbda6f366c9",
        "automationName": "XCUITest",
        "bundleId": "com.leadtone.mig.139pe.iPhone",
        "noReset": "true"
    }

    desired_caps_bak = {
        "platformName": os.getenv('APPIUM_PLATFORM'),
        "PlatformVersion": os.getenv('APPIUM_DEVICE_VERSION'),
        "deviceName": os.getenv('APPIUM_DEVICE_NAME'),
        "udid": os.getenv('APPIUM_DEVICE_UDID'),
        "appPackage": os.getenv('APPIUM_APP_PACKAGE'),
        "appActivity": os.getenv('APPIUM_APP_ACTIVITY'),
        "bundleId": "com.leadtone.mig.139pe.iPhone",
        # "app": os.getenv('APPIUM_APP_FILE'),
        "newCommandTimeout": os.getenv('APPIUM_NEW_COMMAND_TIMEOUT'),
        "noReset": True
    }

    # driver = webdriver.Remote(os.getenv('APPIUM_URL'), desired_caps)
    driver = webdriver.Remote("http://10.10.58.13:4723/wd/hub", desired_caps)

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
