import json

import requests

from Data_Config.Excel import Excel_Data
from Logger.Base_Logger import abc_test_Base

baseURI = "https://hqm-gateway-urtjok3rza-wl.a.run.app/"


class Test_API_Admin_Question:

    def test_get_all_question(self):
        try:
            e1 = Excel_Data()
            title_dict = e1.getAPIData("Admin_Quiz", "get_all_questions")
            question_number = str(title_dict['question_number'])
            log = abc_test_Base.getLogger()
            url = baseURI + 'question/get-questions/' + question_number
            headers = {'content-type': 'application/json'}
            log.info("Getting all questions")
            resp = requests.get(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            data = resp.json()
            log.info("Below is the response obtained...")
            log.info(data)
            assert code == 200, "Invalid status"
            log.info("All questions have been obtained Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_update_a_question(self):
        try:
            log = abc_test_Base.getLogger()
            url = baseURI + 'question/update'
            headers = {'content-type': 'application/json'}
            e1 = Excel_Data()
            log.info("updating question...")
            # add_single_quiz_dict = e1.getAPIData("Admin_Quiz", "update_a_question")
            # title = e1.random_text_generator()
            payload = {

                "questionId": 134,

                "title": "Which of the following statement is correct for AngularJS??",

                "marks": 2,

                "options": [

                    {

                        "optionId": 4,

                        "title": "AngularJS is a SQL framework",

                        "value": False

                    },

                    {

                        "optionId": 3,

                        "title": "AngularJS is a JavaScript framework",

                        "value": False

                    },

                    {

                        "optionId": 2,

                        "title": "AngularJS is a Java framework",

                        "value": False

                    },

                    {

                        "optionId": 1,

                        "title": "AngularJS is an HTML framework",

                        "value": False

                    }

                ],

                "answer": "3"

            }
            log.info("Update question payload is as below:")
            log.info(payload)
            resp = requests.put(url, data=json.dumps(payload), headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            # data = resp.json()
            log.info("Below is the response obtained...")
            # log.info(data)
            assert code == 201, "Invalid status"
            log.info("Question has been updated Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False

    def test_delete_a_question(self):
        try:
            log = abc_test_Base.getLogger()
            e1 = Excel_Data()
            delete_question = e1.getAPIData("Admin_Quiz", "delete_a_question")
            delete_question_id = delete_question['question_number']
            url = baseURI + 'delete/' + delete_question_id
            headers = {'content-type': 'application/json'}
            log.info("Deleting question...")
            resp = requests.delete(url, headers=headers)
            code = resp.status_code
            print(code)
            log.info(code)
            # data = resp.json()
            log.info("Below is the response obtained...")
            # log.info(data)
            assert code == 201, "Invalid status"
            log.info("Question has been updated Successfully")
        except Exception as e:
            log.info("Exception occurred please find details below")
            log.exception(e)
            assert False
