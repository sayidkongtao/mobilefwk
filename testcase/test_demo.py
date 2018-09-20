# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import unittest

from common import globalvariable
from common.commonnittest import CommonUnittest
from po.ios.helper import giveupemailhelper
from po.ios.helper.messagelistpagehelper import MessageListHelper
from utils.utils import Utils


class Demo(CommonUnittest):

    @classmethod
    def setUpClass(cls):
        cls.setUpBeforeClass()

    def setUp(self):
        self.logger.info("start to test: {}".format(self._testMethodName))
        globalvariable.set_value("test_method", self._testMethodName)

    def login_4(self):
        MessageListHelper.login(self.ios_pages)

    def goto_write_email_page_5(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())

    def select_contact_6(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        self.ios_pages.writeemailpage.goto_select_contact_page()
        context = self.ios_pages.selectcontactpage.select_first_contact("Sayid")
        # first_receiver = self.ios_pages.writeemailpage.first_receiver.text()
        # self.assertEqual(context, first_receiver)
        giveupemailhelper.give_up(self.driver)

    def search_and_select_contact_7(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        self.ios_pages.writeemailpage.goto_select_contact_page()
        context = self.ios_pages.selectcontactpage.search_then_select("Sayid")
        # first_receiver = self.ios_pages.writeemailpage.first_receiver.text()
        # self.assertEqual(context, first_receiver)

    def select_group_contact_8(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        self.ios_pages.writeemailpage.goto_select_contact_page()
        context = self.ios_pages.selectcontactpage.select_under_group("读信联系人", "湖北移动")
        # first_receiver = self.ios_pages.writeemailpage.first_receiver.text()
        # self.assertEqual(context, first_receiver)
        giveupemailhelper.give_up(self.driver)

    def delete_receiver_9(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        self.ios_pages.writeemailpage.goto_select_contact_page()
        context = self.ios_pages.selectcontactpage.select_first_contact("Sayid")
        # first_receiver = self.ios_pages.writeemailpage.first_receiver.text()
        # self.assertEqual(context, first_receiver)
        self.ios_pages.writeemailpage.delete_first_contact()
        giveupemailhelper.give_up(self.driver)

    def add_cc_bcc_10(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        cc_text, bcc_text = self.ios_pages.writeemailpage.add_cc_bcc()
        # self.assertEqual(cc_text, "test@")
        # self.assertEqual(bcc_text, "test@")
        giveupemailhelper.give_up(self.driver)

    def send_email_without_subject_11(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        self.ios_pages.writeemailpage.goto_select_contact_page()
        context = self.ios_pages.selectcontactpage.select_first_contact("Sayid")
        first_receiver = self.ios_pages.writeemailpage.first_receiver.text()
        # self.assertEqual(context, first_receiver)
        self.ios_pages.writeemailpage.send_without_subject()
        self.ios_pages.messagelistpage.goto_sent_page()
        text = self.ios_pages.messagelistpage.first_email_subject.text()
        self.assertEqual(text, "(无主题)")

    def send_email_success_12(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        self.ios_pages.writeemailpage.goto_select_contact_page()
        context = self.ios_pages.selectcontactpage.select_first_contact("Sayid")
        first_receiver = self.ios_pages.writeemailpage.first_receiver.text()
        # self.assertEqual(context, first_receiver)
        subject = Utils.now()
        context = "Content" + subject
        self.ios_pages.writeemailpage.send_email_with_subject_content(subject, context)

    def save_email_to_draft_14(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        self.ios_pages.writeemailpage.goto_select_contact_page()
        context = self.ios_pages.selectcontactpage.select_first_contact("Sayid")
        first_receiver = self.ios_pages.writeemailpage.first_receiver.text()
        # self.assertEqual(context, first_receiver)
        subject = Utils.now()
        self.ios_pages.writeemailpage.save_email_to_draft(subject)
        self.ios_pages.messagelistpage.goto_draft_page()
        text = self.ios_pages.messagelistpage.first_email_subject.text()
        self.assertEqual(text, subject)

    def send_email_failed_15(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_write_email_page()
        self.assertTrue(self.ios_pages.writeemailpage.at())
        subject = Utils.now()
        context = "Content" + subject
        self.ios_pages.writeemailpage.goto_select_contact_page()
        self.ios_pages.selectcontactpage.select_first_contact("Abcde")
        self.ios_pages.writeemailpage.send_email_failed(subject, context)

    def goto_contact_details_16(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_contact_list_page()
        name = self.ios_pages.contactlistpage.search_then_select_to_contentdetails("Sayid")
        self.logger.info("Check: 此页面为联系人详情页面")
        self.ios_pages.contactdetailspage.at()

    def check_previous_email_17(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_contact_list_page()
        name = self.ios_pages.contactlistpage.search_then_select_to_contentdetails("Sayid")
        check_name = self.ios_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.ios_pages.contactdetailspage.at()
        self.ios_pages.contactdetailspage.goto_email_history()
        self.ios_pages.emailhistorypage.goto_email_content("Sayid")
        reuslt = self.ios_pages.emailcontentpage.check_previous_button()
        self.logger.info("Check: 切换至上一封邮件内容")
        self.assertTrue(reuslt)

    def check_next_email_18(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_contact_list_page()
        name = self.ios_pages.contactlistpage.search_then_select_to_contentdetails("Sayid")
        check_name = self.ios_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.ios_pages.contactdetailspage.at()
        self.ios_pages.contactdetailspage.goto_email_history()
        self.ios_pages.emailhistorypage.goto_email_content("Sayid")
        reuslt = self.ios_pages.emailcontentpage.check_next_button()
        self.logger.info("Check: 切换至下一封邮件内容")
        self.assertTrue(reuslt)

    def check_reply_email_19(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_contact_list_page()
        name = self.ios_pages.contactlistpage.search_then_select_to_contentdetails("Sayid")
        check_name = self.ios_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.ios_pages.contactdetailspage.at()
        self.ios_pages.contactdetailspage.goto_email_history()
        self.ios_pages.emailhistorypage.goto_email_content("Sayid")
        re = self.ios_pages.emailcontentpage.reply_email_success()
        self.logger.info("Check: subject contains RE")
        self.assertTrue(re)

    def check_forward_email_20(self):
        MessageListHelper.relaunch_app(self.ios_pages.messagelistpage)
        self.ios_pages.messagelistpage.goto_contact_list_page()
        name = self.ios_pages.contactlistpage.search_then_select_to_contentdetails("Sayid")
        check_name = self.ios_pages.contactdetailspage.name.text()
        self.logger.info("Check: 此页面为联系人详情页面")
        self.ios_pages.contactdetailspage.at()
        self.ios_pages.contactdetailspage.goto_email_history()
        self.ios_pages.emailhistorypage.goto_email_content("Sayid")
        fwd = self.ios_pages.emailcontentpage.reply_email_success()
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
