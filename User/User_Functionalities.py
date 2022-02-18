import json

import requests

from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

baseURI = "https://hqm-gateway-urtjok3rza-wl.a.run.app/"


class Test_API_User:

    def test_register_a_user(self):
        try:
            register_dict = {}
            log = abc_test_Base.getLogger()
            url = baseURI + 'user/'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            log.info("Getting data for registration payload")
            register_dict = e1.getAPIData("User", "Register_user")
            userName = str(register_dict['userName'])
            firstName = str(register_dict['firstName'])
            lastName = str(register_dict['lastName'])
            password = str(register_dict['password'])
            email = str(register_dict['email'])
            phone = int(register_dict['phone'])
            #profile = int(register_dict['profile'])
            hubatchid = int(register_dict['huBatchId'])

            payload = {
                "userName": "" + userName + "",
                "firstName": "" + firstName + "",
                "lastName": "" + lastName + "",
                "password": "" + password + "",
                "email": "" + email + "",
                "phone":  phone ,
                "hubatch": {
                    "huBatchId": hubatchid
                }
            }
            log.info("Registration payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            assert code == 201, "Invalid status"
            log.info("Registration is done Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False
