# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import unittest

from common import globalvariable
from common.commonnittest import CommonUnittest
from po.android.helper import giveupemailhelper
from po.android.helper.messagelistpagehelper import MessageListHelper
from utils.utils import Utils


class Demo(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforeClass()

    def setUp(self):
        self.logger.info("start to test: {}".format(self._testMethodName))
        globalvariable.set_value("test_method", self._testMethodName)

    def login_4(self):
        MessageListHelper.login(self.android_pages)

    def goto_write_email_page_5(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())

    def select_contact_6(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertEqual(context["name"], first_receiver.strip())
        giveupemailhelper.give_up(self.driver)

    def search_and_select_contact_7(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.search_then_select("Sayid")
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertEqual(context["name"], first_receiver.strip())

    def select_group_contact_8(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_under_group()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertEqual(context, first_receiver.strip())
        giveupemailhelper.give_up(self.driver)

    def delete_receiver_9(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.select_first_contact()
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertEqual(context["name"], first_receiver.strip())
        self.android_pages.writeemailpage.delete_first_contact()
        giveupemailhelper.give_up(self.driver)

    def add_cc_bcc_10(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        cc_text, bcc_text = self.android_pages.writeemailpage.add_cc_bcc()
        self.assertEqual(cc_text.strip(), "test")
        self.assertEqual(bcc_text.strip(), "test")
        giveupemailhelper.give_up(self.driver)

    def send_email_without_subject_11(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.search_then_select("Sayid")
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertEqual(context["name"], first_receiver.strip())
        self.android_pages.writeemailpage.send_without_subject()
        self.android_pages.messagelistpage.goto_sent_page()
        text = self.android_pages.messagelistpage.first_email_subject.text()
        self.assertEqual(text, "无主题")

    def send_email_success_12(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        self.android_pages.writeemailpage.goto_select_contact_page()
        context = self.android_pages.selectcontactpage.search_then_select("Sayid")
        first_receiver = self.android_pages.writeemailpage.first_receiver.text()
        self.assertEqual(context["name"], first_receiver.strip())
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
        self.assertEqual(context["name"], first_receiver.strip())
        subject = Utils.now()
        self.android_pages.writeemailpage.save_email_to_draft(subject)
        self.android_pages.messagelistpage.goto_draft_page()
        text = self.android_pages.messagelistpage.first_email_subject.text()
        self.assertEqual(text, subject)

    def send_email_failed_15(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.android_pages.writeemailpage.at())
        subject = Utils.now()
        context = "Content" + subject
        self.android_pages.writeemailpage.send_email_failed("sayid_kttao", subject, context)

    def goto_contact_details_16(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_contact_list_page()
        name = self.android_pages.contactlistpage.search_then_select_to_("Sayid")
        check_name = self.android_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.assertEqual(name, check_name)

    def check_previous_email_17(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_contact_list_page()
        name = self.android_pages.contactlistpage.search_then_select_to_("Sayid")
        check_name = self.android_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.assertEqual(name, check_name)
        self.android_pages.contactdetailspage.goto_email_history()
        self.android_pages.emailhistorypage.goto_email_content()
        result = self.android_pages.emailcontentpage.check_previous_button()
        self.logger.info("Check: 切换至上一封邮件内容")
        self.assertTrue(result)

    def check_next_email_18(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_contact_list_page()
        name = self.android_pages.contactlistpage.search_then_select_to_("Sayid")
        check_name = self.android_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.assertEqual(name, check_name)
        self.android_pages.contactdetailspage.goto_email_history()
        self.android_pages.emailhistorypage.goto_email_content()
        result = self.android_pages.emailcontentpage.check_next_button()
        self.logger.info("Check: 切换至下一封邮件内容")
        self.assertTrue(result)

    def check_reply_email_19(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_contact_list_page()
        name = self.android_pages.contactlistpage.search_then_select_to_("Sayid")
        check_name = self.android_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.assertEqual(name, check_name)
        self.android_pages.contactdetailspage.goto_email_history()
        self.android_pages.emailhistorypage.goto_email_content()
        re, sender = self.android_pages.emailcontentpage.reply_email_success()
        self.logger.info("Check: subject contains RE")
        self.assertTrue(re)
        self.logger.info("Check: sender")
        self.assertTrue(sender)

    def check_forward_email_20(self):
        MessageListHelper.relaunch_app(self.android_pages.messagelistpage)
        self.android_pages.messagelistpage.goto_contact_list_page()
        name = self.android_pages.contactlistpage.search_then_select_to_("Sayid")
        check_name = self.android_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.assertEqual(name, check_name)
        self.android_pages.contactdetailspage.goto_email_history()
        self.android_pages.emailhistorypage.goto_email_content()
        fwd = self.android_pages.emailcontentpage.reply_email_success()
        self.logger.info("Check: subject contains Fwd:")
        self.assertTrue(fwd)


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTests(
        map(
            Demo,
            [
                # "login_4",
                "goto_write_email_page_5",
                "select_contact_6",
                "search_and_select_contact_7",
                "select_group_contact_8",
                "delete_receiver_9",
                "add_cc_bcc_10",
                "send_email_without_subject_11",
                "send_email_success_12",
                "save_email_to_draft_14",
                "send_email_failed_15",
                "goto_contact_details_16",
                "check_previous_email_17",
                "check_next_email_18",
                "check_reply_email_19",
                "check_forward_email_20"
             ]
        )
    )
    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
