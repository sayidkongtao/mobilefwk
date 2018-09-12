# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import unittest

from common.commonnittest import CommonUnittest
from po.android.helper import giveupemailhelper
from utils.utils import Utils
from po.android.helper.messagelistpagehelper import MessageListHelper

class Demo(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforeClass()

    def setUp(self):
        self.logger.info("start to test: {}".format(self._testMethodName))

    def login_4(self):
        MessageListHelper.login(self.android_pages)

    def goto_write_email_page_5(self):
        MessageListHelper.login(self.android_pages)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())

    def select_contact_6(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        giveupemailhelper.give_up(self.driver)

    def search_and_select_contact_7(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.search_then_select("Postmaster")
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)

    def select_group_contact_8(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_under_group()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context, first_receiver)
        giveupemailhelper.give_up(self.driver)

    def delete_receiver_9(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertTrue(context["name"], first_receiver)
        self.android_pages.writeemailpage.delete_first_contact()
        giveupemailhelper.give_up(self.driver)

    def add_cc_bcc_10(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        cc_text, bcc_text = self.android_pages.writeemailpage.add_cc_bcc()
        self.assertTrue(cc_text, "test")
        self.assertTrue(bcc_text, "test")
        giveupemailhelper.give_up(self.driver)

    def send_email_without_subject_11(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
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
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
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
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
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
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
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
                "login_4",
                "goto_write_email_page_5",
                "select_contact_6",
                "search_and_select_contact_7",
                "select_group_contact_8",
                "delete_receiver_9",
                "add_cc_bcc_10",
                "send_email_without_subject_11",
                "send_email_success_12",
                "save_email_to_draft_14",
                "send_email_failed_15"
             ]
        )
    )
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
