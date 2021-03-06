# -*- coding: utf-8 -*-
import logging
import os
import time

from common.customlog import CustomLog

# Basic Path ---------------------------------------------------------------
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


#  初始化
def init(logger_name=None):
    global _global_dict
    try:
        _global_dict
    except NameError:
        # 获取系统当前时间
        _global_dict = {}
        project_start_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        project_start_day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        today_result = PATH(os.path.join(".." + os.sep, "result", project_start_day))
        _global_dict["PROJECT_START_TIME"] = project_start_time
        _global_dict["PROJECT_START_DAY"] = project_start_day
        _global_dict["TODAY_RESULT"] = today_result
        if not os.path.exists(today_result):
            os.mkdir(today_result)
        # init log
        logger_name = logger_name if logger_name else "Single"
        CustomLog(logger_name, os.path.join(today_result, project_start_time + "_log.log"), logging.INFO)
        _global_dict["LOGGER_NAME"] = logger_name


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key, def_value=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    return _global_dict.get(key, def_value)
