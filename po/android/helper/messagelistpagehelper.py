# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from po.android.pages.messagelistpage import MessageListPage
from po.android.androdpages import AndroidPages
from utils.utils import Utils
import logging
from common import globalvariable


class MessageListHelper(object):

    @classmethod
    def logger(cls):
        return logging.getLogger(globalvariable.get_value("LOGGER_NAME"))

    @classmethod
    def login(cls, android_pages):
        cls.logger().info("Login app")
        if isinstance(android_pages, AndroidPages):
            android_pages.navigationpage.reset()
            android_pages.navigationpage.goto_accountdomainselect()
            android_pages.accountdomainselectpage.goto_login()
            android_pages.loginpage.goto_message_list()
            Utils.wait_until_condition(lambda: android_pages.messagelistpage.at())
            android_pages.messagelistpage.check_update()
            android_pages.messagelistpage.wait_for_page_fresh()
        else:
            raise AttributeError("parameter android_pages is not instance of AndroidPages")

    @classmethod
    def relaunch_app(cls, page):
        cls.logger().info("relaunch_app")
        if isinstance(page, MessageListPage):
            page.launch_app()
            page.at()
            page.wait_for_page_fresh()
        else:
            raise AttributeError("parameter page is not instance of MessageListPage")



