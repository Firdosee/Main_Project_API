import json
import logging

import requests
from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base


class Test_User_Confirm_Password:
    def test_confirm_password(self):
        try:
            base_dict = {}  # To capture URLs
            login_dict = {}  # To get the user credentials
            head_dict = {} # To get the headers

            log = abc_test_Base.getLogger()
            e = Excel_Data()
            base_dict = e.getAPIData("BaseData", "URL")

            # Providing the URL
            URL = base_dict['BaseURL'] + base_dict['ConfirmPasswordURL']
            log.info("URL is provided")

            login_dict = e.getAPIData("User", "Register_user_itachi")

            # Providing the payload
            payload = {
                "userEmail": login_dict['email'],
                "newPassword": login_dict['newPassword']
            }
            log.info("Payload is provided")

            # Providing the headers
            header = e.getAPIData("Header", "Header")
            log.info("Header is provided")

            # fetching the response
            resp = requests.post(URL, data=json.dumps(payload), headers=header)

            log.info("The response body is as below")
            log.info(resp.text)

            # Validating the status code
            assert resp.status_code == 200, 'Invalid status code'
            log.info("Status code is validated")

        except Exception as e:
            log = abc_test_Base.getLogger()
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False