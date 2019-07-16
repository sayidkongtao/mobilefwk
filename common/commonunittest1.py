# -*- coding: utf-8 -*-

import unittest
from common.logger import logger
from common import environment
from common.loadenv import load_env


class CommonUnittest(unittest.TestCase):

    base_command = ""
    account = {}
    api_url = ""

    def setUp(self):
        logger.info("start to test: {}".format(self._testMethodName))
        logger.info(self._testMethodDoc)

    def tearDown(self):
        self.after_each_test(self)

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def setUpClass(cls):
        cls.load_env()

    @classmethod
    def __list2reason(cls, test_case, exc_list):
        if exc_list and exc_list[-1][0] is test_case:
            return exc_list[-1][1]

    @classmethod
    def after_each_test(cls, test_case):
        if hasattr(test_case, '_outcome'):  # Python 3.4+
            result = test_case.defaultTestResult()  # these 2 methods have no side effects
            test_case._feedErrorsToResult(result, test_case._outcome.errors)
        else:  # Python 3.2 - 3.3 or 2.7
            result = getattr(test_case, '_outcomeForDoCleanups', test_case._resultForDoCleanups)
        error = cls.__list2reason(test_case, result.errors)
        failure = cls.__list2reason(test_case, result.failures)

        logger.info("Result of test case: {} is : {}".format(test_case._testMethodName,
                                                             "Pass" if result.wasSuccessful() else "Failed"))
        if not result.wasSuccessful():
            typ, text = ('ERROR', error) if error else ('FAIL', failure)
            text = text if text.find("During handling of the above exception") < 0 \
                else text[0:text.find("During handling of the above exception")]
            logger.error("The details is \n{text}".format(typ=typ, text=text))

    @classmethod
    def load_env(cls):
        load_env()
        cls.account = environment.ACCOUNT
        cls.api_url = environment.API_URL
        cls.base_command = environment.BASE_COMMAND
        cls.api_client = environment.API_CLIENT
        cls.bs_version = environment.BS_VERSION
