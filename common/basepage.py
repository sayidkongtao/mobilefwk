# -*- coding: utf-8 -*-
__author__ = 'Tao Kong'
import logging
import os
import time

from common import globalvariable

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), path
    )
)


class BasePage:
    def __init__(self, appium_driver):
        self.__driver = appium_driver
        self.logger = logging.getLogger(globalvariable.get_value("LOGGER_NAME"))

    @property
    def driver(self):
        return self.__driver

    @property
    def window_width(self):
        width = self.driver.get_window_size()['width']
        return width

    @property
    def window_height(self):
        height = self.driver.get_window_size()['height']
        return height

    @property
    def window_size(self):
        size = self.driver.get_window_size()
        return {'width': size['width'], 'height': size['height']}

    def back(self):
        self.driver.back()

    def press_key(self, code):
        self.driver.press_keycode(code)

    def switch_to_web_view(self, view_name):
        self.driver.switch_to.context(view_name)

    def set_value_by_keys(self, value):
        letterToCodeHashMap = {}
        lettersStr = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z @ . + _ 0 1 2 3 4 5 6 7 8 9".split()
        androidCodes = [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
                        53, 54, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                        51, 52, 53, 54, 77, 56, 81, 69, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        for index in range(len(lettersStr)):
            letterToCodeHashMap[lettersStr[index]] = androidCodes[index]
        for i in range(len(value)):
            code = letterToCodeHashMap.get(value[i])
            self.pressKey(code)
            time.sleep(0.5)

    # 屏幕向上滑动
    def swipe_up(self, t=1000):
        x1 = int(self.window_width * 0.5)  # x坐标
        y1 = int(self.window_height * 0.75)  # 起始y坐标
        y2 = int(self.window_height * 0.25)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(1.5)

    # 屏幕向下滑动
    def swipe_down(self, t=1000):
        x1 = int(self.window_width * 0.5)  # x坐标
        y1 = int(self.window_height * 0.25)  # 起始y坐标
        y2 = int(self.window_height * 0.75)  # 终点y坐标
        self.driver.swipe(x1, y1, x1, y2, t)
        time.sleep(1.5)

    # 屏幕向左滑动
    def swipe_left(self, t=1000):
        x1 = int(self.window_width * 0.75)
        y1 = int(self.window_height * 0.5)
        x2 = int(self.window_width * 0.05)
        self.driver.swipe(x1, y1, x2, y1, t)
        time.sleep(1.5)

    # 屏幕向右滑动
    def swipe_right(self, t=1000):
        x1 = int(self.window_width * 0.05)
        y1 = int(self.window_height * 0.5)
        x2 = int(self.window_width * 0.75)
        self.driver.swipe(x1, y1, x2, y1, t)
        time.sleep(1.5)

    # savePngName:生成图片的名称
    def save_png_name(self, name):
        """
        name：自定义图片的名称
        """
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = os.path.join(".." + os.sep + ".." + os.sep, "result", day, "image", day)
        tm = self.save_time()
        img_type = ".png"
        if os.path.exists(PATH(fp)):
            filename = os.path.join(PATH(fp), tm + "_" + name + img_type)
            print(PATH(filename))
            # print "True"
            return PATH(filename)
        else:
            os.makedirs(PATH(fp))
            filename = os.path.join(PATH(fp), tm + "_" + name + img_type)
            print(PATH(filename))
            # print "True"
            return PATH(filename)

    # 获取系统当前时间
    def save_time(self):
        """
        返回当前系统时间以括号中（2014-08-29-15_21_55）展示
        """
        return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

    # saveScreenshot:通过图片名称，进行截图保存
    def save_screenshot(self, name):
        """
        快照截图
        name:图片名称
        """
        # 获取当前路径
        # print os.getcwd()
        image = self.driver.save_screenshot(self.save_png_name(name))
        return image
