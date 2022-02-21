import json
import requests
from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

class Test_User_Login:
    def test_login_user(self):
       try:
            e1 = Excel_Data()
            login_dict = {}  # To store user credentials
            base_dict = {}  # To store the URLs
            header_dict = {}  # To store the headers
            log = abc_test_Base.getLogger()

            base_dict = e1.getAPIData("BaseData", "URL")

            # Providing te URL
            URL = base_dict['BaseURL'] + base_dict['LoginURL']
            log.info("URL is provided")

            # Providing the header
            header_dict = e1.getAPIData("Headers", "Header")
            log.info("Header is provided")

            login_dict = e1.getAPIData("User", "Register_user_madara")

            # Providing the payload
            payload = {
                "userName": login_dict['userName'],
                "password": login_dict['password']
            }
            log.info("Payload is provided and as below:")
            log.info(payload)

            # Fetching the rsponse
            resp = requests.post(URL, data=json.dumps(payload), headers=header_dict)
            log.info("Response is as below:")
            log.info(resp.text)

            # Validating the status code
            assert resp.status_code == 200, 'Invalid status code'
            log.info("Status code is validated")
            resp_dict = json.loads(resp.text)

            # Fetching and returning the token
            token = resp_dict['token']
            return token

       except Exception as e:
           log = abc_test_Base.getLogger()
           log.info("Exception occurred please find details below")
           log.exception(e)
           assert False