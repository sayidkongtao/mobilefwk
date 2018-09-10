# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

import os
import unittest

# Basic Path ---------------------------------------------------------------
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def create_suite():
    # 定义单元测试容器
    test_suites = unittest.TestSuite()

    # 定搜索用例文件的方法
    discover = unittest.defaultTestLoader.discover(PATH("testcase"), pattern='test_*.py', top_level_dir=None)

    # 将测试用例加入测试容器中
    for test_suite in discover:
        for case_name in test_suite:
            test_suites.addTest(case_name)
    return test_suites


test_case = create_suite()
