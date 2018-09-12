# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import unittest

from common.commonnittest import CommonUnittest
from po.android.helper import giveupemailhelper
from utils.utils import Utils


class Demo(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforeClass()

    def setUp(self):
        self.logger.info("start to test: {}".format(self._testMethodName))
        self.assertTrue(self.android_pages.messagelistpage.at())
        self.android_pages.messagelistpage.check_update()
        self.android_pages.messagelistpage.wait_for_page_fresh()

    def test_login_4(self):
        self.android_pages.navigationpage.goto_accountdomainselect()
        self.android_pages.accountdomainselectpage.goto_login()
        self.android_pages.loginpage.goto_message_list()
        self.assertTrue(self.android_pages.messagelistpage.at())
        self.android_pages.messagelistpage.check_update()
        self.android_pages.messagelistpage.wait_for_page_fresh()

    def test_goto_write_email_page_5(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())

    def test_select_contact_6(self):
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        giveupemailhelper.give_up(self.driver)

    def test_search_and_select_contact_7(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.search_then_select("Postmaster")
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        giveupemailhelper.give_up(self.driver)

    def test_select_group_contact_8(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_under_group()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context, first_receiver)
        giveupemailhelper.give_up(self.driver)

    def delete_receiver_9(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        self.android_pages.writeemailpage.delete_first_contact()
        giveupemailhelper.give_up(self.driver)

    def add_cc_bcc_10(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        cc_text, bcc_text = self.android_pages.writeemailpage.add_cc_bcc()
        self.assertTrue(cc_text, "test")
        self.assertTrue(bcc_text, "test")
        giveupemailhelper.give_up(self.driver)

    def send_email_without_subject_11(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        self.android_pages.writeemailpage.send_without_subject()
        self.android_pages.messagelistpage.goto_sent_page()
        text = self.android_pages.messagelistpage.first_email_subject.text()
        self.assertTrue(text, "无主题")

    def send_email_success_12(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        subject = Utils.now()
        context = "Content" + subject
        self.android_pages.writeemailpage.send_email_with_subject_content(subject, context)

    def save_email_to_draft_14(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        subject = Utils.now()
        self.android_pages.writeemailpage.save_email_to_draft(subject)
        self.android_pages.messagelistpage.goto_draft_page()
        text = self.android_pages.messagelistpage.first_email_subject.text()
        self.assertTrue(text, "subject")

    def send_email_failed_15(self):
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        subject = Utils.now()
        context = "Content" + subject
        self.android_pages.writeemailpage.send_email_failed("sayid_kttao", subject, context)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(
        map(
            Demo,
            [
                "send_email_failed_15"
             ]
        )
    )
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
