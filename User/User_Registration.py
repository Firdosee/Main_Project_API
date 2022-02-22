import json
import requests
from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

class Test_User_Registration:

    def test_register_user(self):
        try:
            register_dict = {}  # To store user credentials
            log = abc_test_Base.getLogger()
            base_dict = {}  # To store the URLs
            header_dict = {}  # To store the headers

            e1 = Excel_Data()
            base_dict = e1.getAPIData("BaseData", "URL")

            # Providing the URL
            URL = base_dict['BaseURL'] + base_dict['RegistrationURL']
            log.info("URL is provided")


            # Providing the header
            headers = {'content-type': 'application/json'}
            log.info("Headers are provided")

            # Providing the payload

            register_dict = e1.getAPIData("User", "Register_usernew")

            payload = {
                "userName": str(register_dict['userName']),
                "firstName": str(register_dict['firstName']),
                "lastName": str(register_dict['lastName']),
                "password": str(register_dict['password']),
                "email": str(register_dict['email']),
                "phone": str(register_dict['phone']),
                "hubatch": {
                    "huBatchId": int(register_dict['huBatchId'])
                }
            }
            log.info("Payload is provided and as below:")
            log.info(payload)

            # Fetching the response
            resp = requests.post(URL, data=json.dumps(payload), headers=headers)

            log.info("Response is as below:")
            log.info(resp.text)

            # Validating the status code
            assert resp.status_code == 201, "Invalid status"
            log.info("Registration is done Successfully")
            log.info("Status code is validated")

        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False