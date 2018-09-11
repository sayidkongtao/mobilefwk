# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import unittest
import warnings

from common.commonnittest import CommonUnittest


class Demo(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter('ignore', ResourceWarning)
        cls.setUpBeforeClass()

    def setUp(self):
        self.logger.info("start to test: {}".format(self._testMethodName))

    def test_login_4(self):
        self.android_pages.navigationpage.goto_accountdomainselect()
        self.android_pages.accountdomainselectpage.goto_login()
        self.android_pages.loginpage.goto_message_list()
        self.android_pages.messagelistpage.check_update()
        login_success = self.android_pages.messagelistpage.is_write_email_button_visible
        self.assertTrue(login_success)
        self.android_pages.messagelistpage.wait_for_page_fresh()

    def test_goto_write_email_page_5(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at_write_email_page())

    def test_select_contact_6(self):
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(map(Demo, ["test_login", "test_goto_write_email_page", "test_select_contact"]))
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
