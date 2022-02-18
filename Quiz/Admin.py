import json

import requests

from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

baseURI = "https://hqm-gateway-urtjok3rza-wl.a.run.app/"


class Test_API_Admin:

    def test_add_single_quiz(self):
        try:
            add_single_quiz_dict = {}
            log = abc_test_Base.getLogger()
            url = baseURI + 'quiz/add-quiz'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            log.info("Getting data for add new quiz payload")
            add_single_quiz_dict = e1.getAPIData("Admin_Quiz", "add_single_quiz")
            title = e1.random_text_generator()
            categoryId = str(add_single_quiz_dict['categoryId'])
            payload = {
                "title": "" + title + "",
                "categoryId": "" + categoryId + ""
            }
            log.info("Add single quiz payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 201, "Invalid status"
            log.info("New quiz has been added Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_add_new_question(self):
        try:
            add_new_question = {}
            log = abc_test_Base.getLogger()
            url = baseURI + 'question/add'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            log.info("Getting data for add new question payload")
            # add_new_question = e1.getAPIData("Admin_Quiz", "add_question")
            # add_new_question_payload = add_new_question['payload']
            payload = {"title": "What are methods?",
                       "marks": 1,
                       "options": [
                           {
                               "optionId": 1,
                               "title": "option1",
                               "value": False
                           },
                           {
                               "optionId": 2,
                               "title": "option2",
                               "value": False
                           },
                           {
                               "optionId": 3,
                               "title": "option3",
                               "value": False
                           },
                           {
                               "optionId": 4,
                               "title": "option4",
                               "value": False
                           }
                       ],
                       "answer": "1",
                       "quizId": "8"
                       }
            log.info("Add question is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 201, "Invalid status"
            log.info("New question has been added Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_publish_quiz(self):
        try:
            add_new_question = {}
            log = abc_test_Base.getLogger()
            url = baseURI + 'quiz/publish'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            log.info("Getting data for publishing quiz payload")
            payload = {
                "quizId": "7",
                "huxId": "3",
                "totalQuestions": 1,
                "totalMarks": 2
            }
            log.info("Publish quiz payload is as below:")
            log.info(payload)
            resp = requests.post(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 200, "Invalid status"
            log.info("Quiz has been published Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_add_category(self):
        try:
            log = abc_test_Base.getLogger()
            e1 = Excel_Data()
            title_dict = e1.getAPIData("Admin_Quiz", "add_category")
            title = title_dict['title']
            log.info("category is " + title)
            url = baseURI + 'quiz/add-category?categoryTitle=' + title
            # log.info("url is ",url)
            headers = {'content-type': 'application/json'}
            resp = requests.post(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 201, "Invalid status"
            log.info("Category has been added Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_get_all_quiz(self):
        try:
            log = abc_test_Base.getLogger()
            url = baseURI + 'quiz/get-all-quizzes-by-admin'
            log.info("Getting list of all quiz")
            headers = {'content-type': 'application/json'}
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 200, "Invalid status"
            log.info("Quiz list is successfully obtained")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False
