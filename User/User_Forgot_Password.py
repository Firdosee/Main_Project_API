import json
import logging

import requests
from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base
from User.User_Login import Test_User_Login


class Test_User_Forgot_Password:
    def test_user_forgot_password(self):
        try:
            base_dict = {}  # To capture URLs
            login_dict = {}  # To get the user credentials
            head_dict = {}  # To get the headers

            log = abc_test_Base.getLogger()
            e = Excel_Data()

            login_dict = e.getAPIData("User", "Register_user_itachi")
            base_dict = e.getAPIData("BaseData", "URL")

            # Providing the URL
            URL = base_dict["BaseURL"] + base_dict["ForgotPasswordURL"] + login_dict['email']
            log.info("URL is provided")
            log.info(URL)

            # Fetching the response
            resp = requests.post(URL)

            log.info("The response is as below:")
            log.info(resp.text)

            # Validating the status code
            assert resp.status_code == 200, 'Invalid status code'
            log.info("Status code is validated")

        except Exception as e:
            log = abc_test_Base.getLogger()
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False
