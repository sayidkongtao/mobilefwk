# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import unittest
import warnings

from common.commonnittest import CommonUnittest
from po.android.pages.examplepage import ExamplePage


class Example(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.setUpBeforeClass()

    def setUp(self):
        print(self._outcome)
        print(self._testMethodName)

    def test_click(self):
        self.logger.info("start to test")
        example_page = ExamplePage(self.driver)
        example_page.swipe_left()
        example_page.swipe_left()
        example_page.click_button_1()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
