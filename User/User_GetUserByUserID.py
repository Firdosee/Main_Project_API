import json
import requests
from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

from User.User_Login import Test_User_Login


class Test_User_GetUserByUserID:
    def test_get_user_by_user_ID(self):
        try:

            e1 = Excel_Data()
            log = abc_test_Base.getLogger()
            login = Test_User_Login()

            base_dict = e1.getAPIData("BaseData", "URL")

            # Providing the URL for getting the user by user ID
            URL = base_dict['BaseURL'] + base_dict['LoginByUserIDURL'] + str(base_dict['UserID'])
            log.info("URL is provided")


            # Providing the header
            header = {
                "Authorization": 'Bearer '+login.test_login_user()}
            log.info("Header is provided")

            # fetching the response
            respUserID = requests.get(URL, headers=header)
            log.info("Response is sent")

            log.info("The fetched user details is as below:")
            log.info(respUserID.text)

            # Validating the status code
            assert respUserID.status_code == 200, "Invalid status code"
            log.info("Status code is validated")

        except Exception as e:
            log = abc_test_Base.getLogger()
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False