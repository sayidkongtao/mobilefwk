# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from po.ios.pageobjects.button import Button
from po.ios.pageobjects.input import Input
from po.ios.pageobjects.text import Text
from po.ios.pages.writeemailpage import WriteEmailPage
from utils.utils import Utils


class EmailContentPage(WriteEmailPage):
    def __init__(self, appium_driver):
        super(EmailContentPage, self).__init__(appium_driver)

    # email content
    @property
    def next_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="PMMailDetailsVC2"]/XCUIElementTypeButton[3]'),
            "Next Button",
            "EmailContent",
            self.driver
        )

    @property
    def previous_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="PMMailDetailsVC2"]/XCUIElementTypeButton[2]'),
            "Previous Button",
            "EmailContent",
            self.driver
        )

    @property
    def email_time(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '(//XCUIElementTypeNavigationBar[@name="PMMailDetailsVC2"]//following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[3]'),
            "邮件Time",
            "EmailContent",
            self.driver
        )

    @property
    def default_email_sender(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '(//XCUIElementTypeNavigationBar[@name="PMMailDetailsVC2"]//following-sibling::XCUIElementTypeOther//XCUIElementTypeStaticText)[2]'),
            "发送人",
            "EmailContent",
            self.driver
        )

    @property
    def reply_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH,
             '(//XCUIElementTypeImage[@name="separator.png"]//following-sibling::XCUIElementTypeButton)[1]'),
            "回复",
            "EmailContent",
            self.driver
        )

    @property
    def forward_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH,
             '(//XCUIElementTypeImage[@name="separator.png"]//following-sibling::XCUIElementTypeButton)[3]'),
            "转发",
            "EmailContent",
            self.driver
        )

    # reply email content and forward email content
    @property
    def reply_email_content(self):
        return Utils.find(
            Input,
            (MobileBy.ID, "cn.cj.pe:id/message_content"),
            "reply_email_content",
            "RE_EmailContent",
            self.driver
        )

    @property
    def confirm_contains_old_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, '确定'),
            "确定",
            "RE_EmailContent",
            self.driver
        )

    # page logic
    def reply_forward_email_success(self):
        self.send_button.click()
        if self.confirm_contains_old_email_button.is_visible():
            self.confirm_contains_old_email_button.click()
        Utils.wait_until_condition(lambda: self.send_success_img.is_visible(60))
        self.back_to_email_button.click()

    def check_next_button(self):
        first_title = self.email_time.text()
        self.next_email_button.click()
        second_title = self.email_time.text()
        return first_title != second_title

    def check_previous_button(self):
        Utils.wait_time(3)
        first_title = self.email_time.text()
        self.next_email_button.click()
        Utils.wait_time(3)
        self.email_time.text()
        self.previous_email_button.click()
        Utils.wait_time(3)
        second_title = self.email_time.text()
        return first_title == second_title

    def reply_email_success(self):
        sender = self.default_email_sender.text()
        self.reply_button.click()
        # receiver = self.first_receiver.text()
        text = self.subject_input.text()
        self.reply_forward_email_success()
        return text.startswith("Re")

    def forward_email_success(self):
        self.forward_button.click()
        self.first_receiver.send_keys("Sayid")
        text = self.subject_input.text()
        self.reply_forward_email_success()
        return text.startswith("Fwd:")
