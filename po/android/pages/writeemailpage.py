# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.android.pageobjects.button import Button
from utils.utils import Utils
from po.android.pageobjects.text import Text


class WriteEmailPage(BasePage):
    def __init__(self, appium_driver):
        super(WriteEmailPage, self).__init__(appium_driver)

    @property
    def goto_message_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/actionbar_back"),
            "<",
            "WriteEmailPage",
            self.driver
        )

    @property
    def send_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/txt_send"),
            "发送",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_to_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/add_to"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_cc_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/add_cc"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def add_bcc_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/add_bcc"),
            "add_to_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def first_receiver(self):
        return Utils.find_visible(
            Text,
            (MobileBy.XPATH, '//android.widget.RelativeLayout[@resource-id="cn.cj.pe:id/to_layout"]\
            //android.view.View//android.widget.TextView'),
            "first_receiver",
            "WriteEmailPage",
            self.driver
        )

    @property
    def cancel_email_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/left'),
            "取消",
            "WriteEmailPage",
            self.driver
        )

    @property
    def give_up_email_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/mid'),
            "放弃",
            "WriteEmailPage",
            self.driver
        )

    @property
    def save_to_email_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/mid'),
            "保存为草稿",
            "WriteEmailPage",
            self.driver
        )

    @property
    def warning_message(self):
        return Utils.find_visible(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/message'),
            "warning_message",
            "WriteEmailPage",
            self.driver
        )

    @property
    def send_direct_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/right'),
            "send_direct_button",
            "WriteEmailPage",
            self.driver
        )

    @property
    def send_success_img(self):
        return Utils.find_visible(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/gif_success_img'),
            "send_success_img",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

    @property
    def back_to_email_button(self):
        return Utils.find_visible(
            Button,
            (MobileBy.ID, 'cn.cj.pe:id/back_to_list'),
            "back_to_email_button",
            "SendEmailPageResult_WriteEmailPage",
            self.driver
        )

# page logic
    def at_write_email_page(self):
        return self.add_to_button.is_visible()

    def goto_select_contact_page(self):
        self.logger.info("goto_select_contact_page")
        self.add_to_button.click()

    def give_up_send_email(self):
        self.logger.info("give_up_send_email")
        self.goto_message_button.click()
        self.give_up_email_button.click()
