import json
import requests
from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

baseURI = "https://hqm-gateway-urtjok3rza-wl.a.run.app/"
class Test_User_Login:
    def test_login_user(self):
        try:
            log = abc_test_Base.getLogger()
            log.info("Logging in as admin")
            url = baseURI + 'user/login/generate-token'
            headers = {'content-type': 'application/json'}
            dataObj = Excel_Data()
            dictionaryData = dataObj.getAPIData("User", "Register_user_madara")
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

