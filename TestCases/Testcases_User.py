import json

import requests

from Logger.Base_Logger import abc_test_Base
from Quiz.Admin import Test_API_Admin
from Quiz.Admin_Question import Test_API_Admin_Question
from Quiz.Admin_Quiz import Test_Admin_Quiz
from Quiz.User_Admin import Test_User_Admin

t1 = Test_API_Admin()
t2 = Test_API_Admin_Question()
t3 = Test_Admin_Quiz()
t4 = Test_User_Admin()
logger = abc_test_Base()
log = logger.getLogger()


class Test_Usecases_User:

    def test_Admin_Loginuser_u(self):
        try:
            log.info("Executing testcase Admin_Loginuser_by_admin")
            t4.Admin_Loginuser("Admin_Quiz", "login")
            log.info("Testcase Admin_Loginuser_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)