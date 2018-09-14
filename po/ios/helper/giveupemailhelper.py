# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'

from po.ios.pages.messagelistpage import MessageListPage
from po.ios.pages.writeemailpage import WriteEmailPage


def give_up(appium_driver):
    write_page = WriteEmailPage(appium_driver)
    write_page.give_up_send_email()
    MessageListPage(appium_driver).at()
    MessageListPage(appium_driver).wait_for_page_fresh()


def save_email_to_draft(appium_driver):
    write_page = WriteEmailPage(appium_driver)
    write_page.save_email_to_draft()
    MessageListPage(appium_driver).at()
    MessageListPage(appium_driver).wait_for_page_fresh()



