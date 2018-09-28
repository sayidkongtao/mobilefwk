# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from po.android.pageobjects.input import Input
from po.android.pageobjects.text import Text
from utils.utils import Utils


class WriteEmailPage(BasePage):
    def __init__(self, appium_driver):
        super(WriteEmailPage, self).__init__(appium_driver)

    @property
    def goto_message_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/actionbar_back"),
            "<",
            "WriteEmailPage",
            self.driver
        )

    @property
    def send_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/txt_send"),
            "发送",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_to_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/add_to"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_cc_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/add_cc"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_bcc_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/add_bcc"),
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
            (MobileBy.XPATH, '(//android.widget.RelativeLayout[@resource-id="cn.cj.pe:id/to_layout"]\
             //android.widget.TextView)[2]'),
            "first_receiver",
            "WriteEmailPage",
            self.driver
        )

    @property
    def delete_receive(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, '//*[@text="移除"]'),
            "移除",
            "WriteEmailPage",
            self.driver
        )

    # cc table
    @property
    def cc_bcc_item(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/cc_lable'),
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
             '(//*[@resource-id="cn.cj.pe:id/cc_wrapper"]//android.widget.TextView)[2]'),
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
             '(//*[@resource-id="cn.cj.pe:id/bcc_layout"]//android.widget.TextView)[2]'),
            "first_p_under_cc_item",
            "WriteEmailPage",
            self.driver
        )

    @property
    def subject_input(self):
        return Utils.find(
            Input,
            (MobileBy.ID, 'cn.cj.pe:id/subject'),
            "主题",
            "WriteEmailPage",
            self.driver
        )

    # cancel table
    @property
    def cancel_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/left'),
            "取消",
            "WriteEmailPage",
            self.driver
        )

    @property
    def give_up_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/mid'),
            "放弃",
            "WriteEmailPage",
            self.driver
        )

    @property
    def save_to_draft_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/right'),
            "保存为草稿",
            "WriteEmailPage",
            self.driver
        )

    @property
    def warning_message(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/message'),
            "warning_message",
            "WriteEmailPage",
            self.driver
        )

    @property
    def send_direct_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/right'),
            "send_direct_button",
            "WriteEmailPage",
            self.driver
        )

    # result page
    @property
    def back_result_button(self):
        return Utils.find(
            Text,
            (MobileBy.ID, "cn.cj.pe:id/hjl_headicon"),
            "<",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    @property
    def send_success_img(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//*[@resource-id="cn.cj.pe:id/gif_success_img"]'),
            "send_success_img",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    @property
    def send_failed_text(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/progressText'),
            "发送失败",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    @property
    def back_to_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/back_to_list'),
            "back_to_email_button",
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
        self.cc_item.send_keys("test@aa.com")
        self.receive_label.click()
        self.bcc_item.click()
        self.bcc_item.send_keys("test@aa.com")
        self.receive_label.click()
        cc_text = self.first_p_under_cc_item.text()
        bcc_text = self.first_p_under_bcc_item.text()
        return cc_text, bcc_text

    def send_without_subject(self):
        self.send_button.click()
        self.send_direct_button.click()
        Utils.wait_until_condition(lambda: self.send_success_img.is_visible())
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
        Utils.wait_until_condition(lambda: self.send_success_img.is_visible())
        self.back_to_email_button.click()

    def send_email_failed(self, contact, subject, content):
        self.subject_input.click()
        self.subject_input.send_keys(subject)
        self.content_input.click()
        self.content_input.send_keys(content)
        self.receive_label.click()
        self.receive_label.send_keys(contact)
        self.send_button.click()
        Utils.wait_until_condition(lambda: self.send_failed_text.text() == "发送失败")
        self.back_result_button.click()
