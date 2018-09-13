# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from po.android.pageobjects.button import Button
from po.android.pageobjects.input import Input
from po.android.pageobjects.text import Text
from po.android.pages.writeemailpage import WriteEmailPage
from utils.utils import Utils


class EmailContentPage(WriteEmailPage):
    def __init__(self, appium_driver):
        super(EmailContentPage, self).__init__(appium_driver)

    # email content
    @property
    def next_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/actionbar_next'),
            "Next Button",
            "EmailContent",
            self.driver
        )

    @property
    def previous_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/actionbar_previous'),
            "Previous Button",
            "EmailContent",
            self.driver
        )

    @property
    def email_title(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/title'),
            "邮件主题",
            "EmailContent",
            self.driver
        )

    @property
    def default_email_sender(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/from'),
            "发送人",
            "EmailContent",
            self.driver
        )

    @property
    def reply_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH,
             '//android.widget.LinearLayout[@resource-id="cn.cj.pe:id/bottomBar_message"]//android.widget.TextView[@text="回复"]'),
            "回复",
            "EmailContent",
            self.driver
        )

    @property
    def forward_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH,
             '//android.widget.LinearLayout[@resource-id="cn.cj.pe:id/bottomBar_message"]//android.widget.TextView[@text="转发"]'),
            "转发",
            "EmailContent",
            self.driver
        )

    # reply email content and forward email content
    @property
    def receiver(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/contact_to'),
            "收件人邮箱",
            "EmailContent",
            self.driver
        )

    @property
    def email_subject(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/subject'),
            "主题",
            "EmailContent",
            self.driver
        )

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
            (MobileBy.ID, 'cn.cj.pe:id/sure_btn'),
            "确定",
            "RE_EmailContent",
            self.driver
        )

    # page logic
    def reply_forward_email_success(self, value="test"):
        self.reply_email_content.send_keys(value)
        self.send_button.click()
        if self.confirm_contains_old_email_button.is_visible(5):
            self.confirm_contains_old_email_button.click()
        Utils.wait_until_condition(lambda: self.send_success_img.is_visible(60))
        self.back_to_email_button.click()

    def check_next_button(self):
        first_title = self.email_title.text()
        self.next_email_button.click()
        second_title = self.email_title.text()
        return first_title != second_title

    def check_previous_button(self):
        first_title = self.email_title.text()
        self.next_email_button.click()
        self.email_title.text()
        self.previous_email_button.click()
        second_title = self.email_title.text()
        return first_title == second_title

    def reply_email_success(self, value="test"):
        sender = self.default_email_sender.text()
        self.reply_button.click()
        receiver = self.receiver.text()
        text = self.subject_input.text()
        self.reply_forward_email_success(value)
        return text.startswith("Re"), sender.strip() == receiver.strip()

    def forward_email_success(self, value="test"):
        self.forward_button.click()
        self.receiver.send_keys("Sayid")
        text = self.subject_input.text()
        self.reply_forward_email_success(value)
        return text.startswith("Fwd:")
