# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from po.android.pages.writeemailpage import WriteEmailPage
from po.android.pages.messagelistpage import MessageListPage


def give_up(appium_driver):
    write_page = WriteEmailPage(appium_driver)
    write_page.give_up_send_email()
    MessageListPage(appium_driver).at()
    MessageListPage(appium_driver).wait_for_page_fresh()
