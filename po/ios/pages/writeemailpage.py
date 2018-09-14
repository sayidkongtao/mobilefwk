# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.ios.pageobjects.button import Button
from po.ios.pageobjects.input import Input
from po.ios.pageobjects.text import Text
from utils.utils import Utils


class WriteEmailPage(BasePage):
    def __init__(self, appium_driver):
        super(WriteEmailPage, self).__init__(appium_driver)

    @property
    def goto_message_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID,
             '//XCUIElementTypeNavigationBar[@name="PMWriteMailVC"]/XCUIElementTypeButton[1]'),
            "<",
            "WriteEmailPage",
            self.driver
        )

    @property
    def send_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, "发送"),
            "发送",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_to_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, "write add user"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_cc_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, "write add user"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_bcc_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, "write add user"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    # receive table
    @property
    def receive_label(self):
        return Utils.find(
            Text,
            (MobileBy.ID, "cn.cj.pe:id/to_lable"),
            "收件人",
            "WriteEmailPage",
            self.driver
        )

    @property
    def first_receiver(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '//XCUIElementTypeStaticText[contains(@name,"收件人")]//parent::XCUIElementTypeOther//XCUIElementTypeTextField'),
            "first_receiver",
            "WriteEmailPage",
            self.driver
        )

    @property
    def delete_receive(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, "移除"),
            "移除",
            "WriteEmailPage",
            self.driver
        )

    # cc table
    @property
    def cc_bcc_item(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '抄送/密送:'),
            "抄送/密送",
            "WriteEmailPage",
            self.driver
        )

    @property
    def cc_item(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//*[@resource-id="cn.cj.pe:id/cc_wrapper"]'),
            "抄送",
            "WriteEmailPage",
            self.driver
        )

    @property
    def first_p_under_cc_item(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '//XCUIElementTypeStaticText[contains(@name,"抄")]//parent::XCUIElementTypeOther//XCUIElementTypeTextField'),
            "first_p_under_cc_item",
            "WriteEmailPage",
            self.driver
        )

    @property
    def bcc_item(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/bcc_lable'),
            "密送",
            "WriteEmailPage",
            self.driver
        )

    @property
    def first_p_under_bcc_item(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH,
             '//*[@resource-id="cn.cj.pe:id/bcc_wrapper"]//ios.view.ViewGroup//ios.widget.TextView'),
            "first_p_under_cc_item",
            "WriteEmailPage",
            self.driver
        )

    @property
    def subject_input(self):
        return Utils.find(
            Input,
            (MobileBy.XPATH,
             '//XCUIElementTypeStaticText[contains(@name,"主")]//following-sibling::XCUIElementTypeTextField'),
            "主题",
            "WriteEmailPage",
            self.driver
        )

    # cancel table
    @property
    def cancel_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, '取消'),
            "取消",
            "WriteEmailPage",
            self.driver
        )

    @property
    def give_up_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, '放弃'),
            "放弃",
            "WriteEmailPage",
            self.driver
        )

    @property
    def save_to_draft_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, '保存为草稿'),
            "保存为草稿",
            "WriteEmailPage",
            self.driver
        )

    @property
    def warning_message(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '放弃写邮件并保存草稿箱？'),
            "warning_message",
            "WriteEmailPage",
            self.driver
        )

    @property
    def send_direct_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, '直接发送'),
            "send_direct_button",
            "WriteEmailPage",
            self.driver
        )

    # result page
    @property
    def back_result_button(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="发送失败"]/XCUIElementTypeButton'),
            "<",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    @property
    def send_success_img(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, 'send_success7.png'),
            "send_success_img",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    @property
    def send_failed_img(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, 'write_send_error.png'),
            "发送失败",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    @property
    def back_to_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ACCESSIBILITY_ID, '返回邮箱'),
            "返回邮箱",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    # content table
    @property
    def content_input(self):
        return Utils.find(
            Input,
            (MobileBy.ID, 'cn.cj.pe:id/message_content'),
            "正文部分",
            "WriteEmailPage",
            self.driver
        )

# page logic
    def at(self):
        return self.add_to_button.is_visible()

    def goto_select_contact_page(self):
        self.logger.info("goto_select_contact_page")
        self.add_to_button.click()

    def give_up_send_email(self):
        self.logger.info("give_up_send_email")
        self.goto_message_button.click()
        if self.give_up_email_button.is_visible(3):
            self.give_up_email_button.click()

    def delete_first_contact(self):
        first_receiver = self.first_receiver
        first_receiver.click()
        # need to click twice
        first_receiver.click()
        delete_receive = self.delete_receive
        delete_receive.click()
        Utils.wait_disappear(delete_receive)
        Utils.wait_disappear(first_receiver)

    def add_cc_bcc(self):
        self.cc_bcc_item.click()
        self.cc_item.click()
        self.cc_item.send_keys("test")
        self.receive_label.click()
        self.bcc_item.click()
        self.bcc_item.send_keys("test")
        self.receive_label.click()
        cc_text = self.first_p_under_cc_item.text()
        bcc_text = self.first_p_under_bcc_item.text()
        return cc_text, bcc_text

    def send_without_subject(self):
        self.send_button.click()
        self.send_direct_button.click()
        Utils.wait_until_condition(lambda: self.send_success_img.is_visible(60))
        self.back_to_email_button.click()

    def save_email_to_draft(self, subject):
        self.subject_input.click()
        self.subject_input.send_keys(subject)
        self.goto_message_button.click()
        save_draft = self.save_to_draft_button
        save_draft.click()
        Utils.wait_disappear(save_draft)

    def send_email_with_subject_content(self, subject, content):
        self.subject_input.click()
        self.subject_input.send_keys(subject)
        self.content_input.click()
        self.content_input.send_keys(content)
        self.send_button.click()
        Utils.wait_until_condition(lambda: self.send_success_img.is_visible(60))
        self.back_to_email_button.click()

    def send_email_failed(self, contact, subject, content):
        self.subject_input.click()
        self.subject_input.send_keys(subject)
        self.content_input.click()
        self.content_input.send_keys(content)
        self.receive_label.click()
        self.receive_label.send_keys(contact)
        self.send_button.click()
        Utils.wait_until_condition(lambda: self.send_failed_img.text() == "发送失败")
        self.back_result_button.click()
