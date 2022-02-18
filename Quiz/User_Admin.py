import json

import requests

from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

baseURI = "https://hqm-gateway-urtjok3rza-wl.a.run.app/"


class Test_User_Admin:

    def test_Admin_Loginuser(self):
        try:
            log = abc_test_Base.getLogger()
            log.info("Logging in as admin")
            url = baseURI + 'user/login/generate-token'
            headers = {'content-type': 'application/json'}
            dataObj = Excel_Data()
            dictionaryData = dataObj.getAPIData("Admin_Quiz","login")
            userName = str(dictionaryData['userName'])
            password = str(dictionaryData['password'])
            log.info("Fetching payload data for admin")
            payload = {
                "userName": "" + userName + "",
                "password": "" + password + ""
            }
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            statuscode = response.status_code
            data = response.json()
            bearer_token = data['token']
            log.info("Bearer token is ")
            log.info(bearer_token)
            log.info(statuscode)
            assert statuscode == 200
            log.info("Successfully Logged in")
            return bearer_token
        except Exception as e:
            print("Exception occured", e)

    def test_save_all_hux(self):
        try:
            log = abc_test_Base.getLogger()
            e1 = Excel_Data()
            title_dict = e1.getAPIData("Admin_Quiz", "save_hux")
            url = baseURI + 'user/hux/saveHuxBatch'
            log.info(title_dict)
            headers = {'content-type': 'application/json'}
            huBatchTitle = e1.random_text_generator()
            startDate = title_dict['startDate']
            endDate = str(title_dict['endDate'])

            payload = {
                "huBatchTitle": "" + huBatchTitle + "",
                "startDate": "" + startDate + "",
                "endDate": "" + endDate + ""
            }
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 201, "Invalid status"
            log.info("All hux is saved Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_get_hux_batch(self):
        try:
            log = abc_test_Base.getLogger()
            e1 = Excel_Data()
            title_dict = e1.getAPIData("Admin_Quiz", "get_all_hux")
            url = baseURI + 'user/hux/getAllHux'
            headers = {'content-type': 'application/json'}
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 200, "Invalid status"
            log.info("Hux is has been obtained Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_get_alluser_by_huid(self):
        try:
            log = abc_test_Base.getLogger()
            e1 = Excel_Data()
            data_dict = e1.getAPIData("Admin_Quiz", "get_alluser_by_huid")
            batchid = str(data_dict['huBatchId'])
            url = baseURI + 'user/login/getAllUsers?huBatchId=' + batchid
            headers = {'content-type': 'application/json'}
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 200, "Invalid status"
            log.info("All hux users have been obtained Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_get_alluser_admin(self):
        try:
            log = abc_test_Base.getLogger()
            log.info("Fetching all user Admin details...")
            e1 = Excel_Data()
            log.info("Calling the login as admin method")
            u1 = Test_User_Admin()
            bearer = u1.test_Admin_Loginuser()
            log.info(bearer)
            url = baseURI + 'user/login/getAllUserAdmin'
            headers = {'content-type': 'application/json','Authorization': 'Bearer ' +bearer}
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 200, "Invalid status"
            log.info("get all user admin use case is successfully passed")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False
