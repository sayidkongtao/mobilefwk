# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import unittest
from common.commonnittest import CommonUnittest
from po.android.helper import giveupemailhelper


class Demo(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforeClass()

    def setUp(self):
        self.logger.info("start to test: {}".format(self._testMethodName))

    def test_login_4(self):
        self.android_pages.navigationpage.goto_accountdomainselect()
        self.android_pages.accountdomainselectpage.goto_login()
        self.android_pages.loginpage.goto_message_list()
        self.assertTrue(self.android_pages.messagelistpage.at_message_list_page())
        self.android_pages.messagelistpage.check_update()
        self.android_pages.messagelistpage.wait_for_page_fresh()

    def test_goto_write_email_page_5(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at_write_email_page())

    def test_select_contact_6(self):
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        giveupemailhelper.give_up(self.driver)

    def test_select_specific_contact_7(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at_write_email_page())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.search_then_select("Postmaster")
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        giveupemailhelper.give_up(self.driver)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(
        map(
            Demo,
            ["test_login_4",
             "test_goto_write_email_page_5",
             "test_select_contact_6",
             "test_select_specific_contact_7"
             ]
        )
    )
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
