import json
import logging

import requests
from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base
from User.User_Login import Test_User_Login


class Test_User_Authenticate:
    def test_user_authenticate(self):
        try:
            base_dict = {}  # To capture URLs
            login_dict = {}  # To get the user credentials
            head_dict = {}  # To get the headers
            login = Test_User_Login()

            log = abc_test_Base.getLogger()
            e = Excel_Data()

            base_dict = e.getAPIData("BaseData", "URL")

            # Capturing the Base URL
            URL = base_dict['BaseURL']+base_dict["AuthenticateURL"]
            log.info("URL is provided")

            # Providing the header
            header = {'Authorization': 'Bearer '+login.test_login_user()}
            log.info("Header is provided")

            # Fetching the response
            resp = requests.get(URL, headers=header)
            log.info("Response is as below")
            log.info(resp)

            # Status code validation
            assert resp.status_code == 200, 'Invalid statuscode'
            log.info("Status code is validated")
        except Exception as e:
            log = abc_test_Base.getLogger()
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False