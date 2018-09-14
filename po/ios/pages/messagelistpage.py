# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from appium.webdriver.common.mobileby import MobileBy

from common.basepage import BasePage
from po.ios.pageobjects.button import Button
from po.ios.pageobjects.text import Text
from utils.utils import Utils


class MessageListPage(BasePage):
    def __init__(self, appium_driver):
        super(MessageListPage, self).__init__(appium_driver)

    @property
    def title(self):
        return Utils.find(
            Text,
            (MobileBy.ID, 'cn.cj.pe:id/actionbar_sub_title'),
            "title",
            "MessageListPage",
            self.driver
        )

    @property
    def refresh_quee_view_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/refresh_quee_view"),
            "refresh_quee_view_button",
            "MessageListPage",
            self.driver
        )

    @property
    def write_email_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="PMInbox"]/XCUIElementTypeButton[4]'),
            "write_email_button",
            "MessageListPage",
            self.driver
        )

    @property
    def close_button(self):
        return Utils.find(
            Button,
            (MobileBy.ID, "cn.cj.pe:id/close"),
            "close_button for update",
            "MessageListPage",
            self.driver
        )

# left menu
    @property
    def more_button(self):
        return Utils.find(
            Button,
            (MobileBy.XPATH, '//XCUIElementTypeNavigationBar[@name="PMInbox"]/XCUIElementTypeButton[1]'),
            'more_menu',
            "MessageListPage",
            self.driver
        )

    @property
    def folder(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '文件夹'),
            "文件夹",
            "MessageListPage",
            self.driver
        )

    @property
    def sent_email(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '已发送'),
            "已发送",
            "MessageListPage",
            self.driver
        )

    @property
    def draft_email(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '草稿箱'),
            "已发送",
            "MessageListPage",
            self.driver
        )

    # email list
    @property
    def first_email_subject(self):
        return Utils.find(
            Text,
            (MobileBy.XPATH, '//ios.widget.TextView[@resource-id="cn.cj.pe:id/mail_subject"]'),
            "第一个邮件主题",
            "MessageListPage",
            self.driver
        )

    # bottom bar
    @property
    def email_bar(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '邮件'),
            "邮件",
            "MessageListPage",
            self.driver
        )

    @property
    def contact_bar(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '联系人'),
            "联系人",
            "MessageListPage",
            self.driver
        )

    @property
    def find_bar(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '发现'),
            "发现",
            "MessageListPage",
            self.driver
        )

    @property
    def mine_bar(self):
        return Utils.find(
            Text,
            (MobileBy.ACCESSIBILITY_ID, '我的'),
            "我的",
            "MessageListPage",
            self.driver
        )

# page logic
    def at(self):
        self.logger.info("Wait for page MessageListPage")
        Utils.wait_until_condition(lambda: self.write_email_button.is_visible())
        return True

    def check_update(self):
        self.logger.info("check whether has version update")
        close_button = self.close_button

        if close_button.is_visible():
            self.logger.info("close version update")
            close_button.click()
            self.check_update()
        else:
            self.logger.info("no version update info displayed")
        return self

    def goto_write_email_page(self):
        self.logger.info("goto_write_email_page")
        self.write_email_button.click()

    def goto_sent_page(self):
        self.more_button.click()
        self.sent_email.click()
        Utils.wait_until_condition(lambda: self.title.text() == "已发送")
        self.wait_for_page_fresh()

    def goto_draft_page(self):
        self.more_button.click()
        self.draft_email.click()
        Utils.wait_until_condition(lambda: self.title.text() == "草稿箱")
        self.wait_for_page_fresh()

    def goto_contact_list_page(self):
        self.logger.info("goto_contact_list_page")
        self.contact_bar.click()

    def wait_for_page_fresh(self):
        refresh_quee_view_button = self.refresh_quee_view_button
        if refresh_quee_view_button.is_visible(6):
            Utils.wait_disappear(refresh_quee_view_button)
