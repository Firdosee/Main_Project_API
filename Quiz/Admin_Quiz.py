import json

import requests

from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

baseURI = "https://hqm-quiz-urtjok3rza-wl.a.run.app/"


class Test_Admin_Quiz:

    def get_all_pending_quiz(self, Admin,get_all_pending_quiz_1):
        global log
        try:
            get_all_pending_quiz = {}
            log = abc_test_Base.getLogger()
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            get_all_pending_quiz_dict = e1.getAPIData(Admin,get_all_pending_quiz_1)
            userId = get_all_pending_quiz_dict['userId']
            #log.info("User ID is " + userId)
            url = baseURI + 'quiz/get-pending-quizzes?userId=' + userId
            log.info("Getting All the pending quiz ")
            log.info(url)
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            body = resp.json()
            log.info(body)

            assert code == 200, "Invalid status"
            log.info("Got all the pending quiz")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_all_quizs(self, Admin, get_all_quizs):
        global log
        try:
            get_all_quizs = {}
            log = abc_test_Base.getLogger()
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            get_all_quizs = e1.getAPIData("Admin", "get_all_quizs")
            userId = get_all_quizs['userId']
            log.info("User ID is " + userId)
            url = baseURI + 'quiz/get-quizzes/' + userId
            log.info("Getting All the quiz...")
            log.info(url)
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            body = resp.json()
            log.info(body)

            assert code == 200, "Invalid status"
            log.info("Got all the quiz")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_a_single_quiz(self, Admin, get_a_single_quiz_1):
        global log
        try:
            get_a_single_quiz = {}
            log = abc_test_Base.getLogger()
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            get_a_single_quiz = e1.getAPIData(Admin, get_a_single_quiz_1)
            userId = get_a_single_quiz['userId']
            quizId = get_a_single_quiz['quizId']
            log.info("User ID is " + userId)
            url = baseURI + 'quiz/' + userId + "/" + quizId
            log.info("Getting a single quiz...")
            log.info(url)
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            body = resp.json()
            log.info(body)

            assert code == 200, "Invalid status"
            log.info("Got a single quiz")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_submitted_quiz(self,Admin, get_submitted_quiz_1):
        global log
        try:
            get_submitted_quiz = {}
            log = abc_test_Base.getLogger()
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            get_submitted_quiz = e1.getAPIData(Admin, get_submitted_quiz_1)
            userId = get_submitted_quiz['userId']
            log.info("User ID is " + userId)
            url = baseURI + 'quiz/get-submitted-quizzes?userId=' + userId
            log.info("Getting the submitted quiz...")
            log.info(url)
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            body = resp.json()
            log.info(body)

            assert code == 200, "Invalid status"
            log.info("Got the submitted quiz")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def submit_a_quiz(self,Admin, submit_a_quiz_1):
        try:
            submit_a_quiz = {}
            log = abc_test_Base.getLogger()
            url = baseURI + 'user/'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            submit_a_quiz = e1.getAPIData(Admin, submit_a_quiz_1)
            userId = submit_a_quiz['userId']
            quizId = submit_a_quiz['quizId']
            scoreObtained = int(submit_a_quiz['scoreObtained'])
            log.info("User ID is " + userId)
            url = baseURI + 'quiz/submit'
            log.info("Submit the quiz ")

            payload = {
                "quizId": "" + quizId + "",
                "userId": "" + userId + "",
                "scoreObtained": scoreObtained
            }
            log.info("Submit payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            log.info(resp.json())
            print(code)
            log.info(code)
            assert code == 200, "Invalid status"
            log.info("Quiz Submission is done Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def get_all_categories(self):
        global log
        try:
            log = abc_test_Base.getLogger()
            headers = {'content-type': 'application/json'}
            url = baseURI + 'quiz/get-all-categories'
            log.info("Getting All the Category ")
            log.info(url)
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            body = resp.json()
            log.info(body)
            with open("response.txt", "w") as f:
                f.write(resp.text)
            assert code == 200, "Invalid status"
            log.info("Got All the Category")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False
