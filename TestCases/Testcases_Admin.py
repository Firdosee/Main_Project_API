import json

import requests

from Logger.Base_Logger import abc_test_Base
from Quiz.Admin import Test_API_Admin
from Quiz.Admin_Question import Test_API_Admin_Question
from Quiz.Admin_Quiz import Test_Admin_Quiz
from Quiz.User_Admin import Test_User_Admin

t1 = Test_API_Admin()
t2 = Test_API_Admin_Question()
t3 = Test_Admin_Quiz()
t4 = Test_User_Admin()
logger = abc_test_Base()
log = logger.getLogger()


class Test_Usecases_Admin:

    def test_Admin_Loginuser(self):
        try:
            log.info("Executing testcase Admin_Loginuser_by_admin")
            t4.Admin_Loginuser("Admin_Quiz", "login")
            log.info("Testcase Admin_Loginuser_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_add_quiz_by_admin(self):
        try:
            log.info("Executing testcase add_quiz_by_admin")
            t1.add_single_quiz("Admin_Quiz", "add_single_quiz")
            log.info("Testcase add_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_add_new_question_by_admin(self):
        try:
            log.info("Executing testcase add_new_question_by_admin")
            t1.add_new_question("Admin_Quiz", "add_single_quiz")
            log.info("Testcase add_new_question_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_publish_quiz_by_admin(self):
        try:
            log.info("Executing testcase publish_quiz_by_admin")
            t1.publish_quiz()
            log.info("Testcase publish_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_add_category_by_admin(self):
        try:
            log.info("Executing testcase add_category_by_admin")
            t1.add_category("Admin_Quiz", "add_category")
            log.info("Testcase add_category_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_all_quiz_by_admin(self):
        try:
            log.info("Executing testcase get_all_quiz_by_admin")
            t1.get_all_quiz()
            log.info("Testcase get_all_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_all_question_by_admin(self):
        try:
            log.info("Executing testcase get_all_question_by_admin")
            t2.get_all_question()
            log.info("Testcase get_all_question_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_update_a_question_by_admin(self):
        try:
            log.info("Executing testcase update_a_question_by_admin")
            t2.update_a_question()
            log.info("Testcase update_a_question_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_delete_a_question_by_admin(self):
        try:
            log.info("Executing testcase delete_a_question_by_admin")
            t2.delete_a_question("Admin_Quiz", "delete_a_question")
            log.info("Testcase delete_a_question_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_all_pending_quiz_by_admin(self):
        try:
            log.info("Executing testcase get_all_pending_quiz_by_admin")
            t3.get_all_pending_quiz("Admin", "get_all_pending_quiz")
            log.info("Testcase get_all_pending_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_all_quizs_by_admin(self):
        try:
            log.info("Executing testcase get_all_quiz_by_admin")
            t3.get_all_quizs("Admin", "get_all_quizs")
            log.info("Testcase get_all_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_a_single_quiz_by_admin(self):
        try:
            log.info("Executing testcase get_a_single_quiz_by_admin")
            t3.get_a_single_quiz("Admin", "get_a_single_quiz")
            log.info("Testcase get_a_single_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_submitted_quiz_by_admin(self):
        try:
            log.info("Executing testcase get_submitted_quiz_by_admin")
            t3.get_submitted_quiz("Admin", "get_submitted_quiz")
            log.info("Testcase get_submitted_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_submit_a_quiz_by_admin(self):
        try:
            log.info("Executing testcase submit_a_quiz_by_admin")
            t3.submit_a_quiz("Admin", "submit_a_quiz")
            log.info("Testcase submit_a_quiz_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_all_categories_by_admin(self):
        try:
            log.info("Executing testcase get_all_categories_by_admin")
            t3.get_all_categories()
            log.info("Testcase get_all_categories_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_save_all_hux(self):
        try:
            log.info("Executing testcase save_all_hux_by_admin")
            t4.save_all_hux("Admin_Quiz", "save_hux")
            log.info("Testcase save_all_hux_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_hux_batch(self):
        try:
            log.info("Executing testcase get_hux_batch_by_admin")
            t4.get_hux_batch("Admin_Quiz", "get_all_hux")
            log.info("Testcase get_hux_batch_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_alluser_by_huid(self):
        try:
            log.info("Executing testcase get_alluser_by_huid_by_admin")
            t4.get_alluser_by_huid("Admin_Quiz", "get_alluser_by_huid")
            log.info("Testcase get_alluser_by_huid_by_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False

    def test_get_alluser_admin(self):
        try:
            log.info("Executing testcase get_alluser_admin")
            t4.get_alluser_admin()
            log.info("Testcase get_alluser_admin is successfully executed")
        except Exception as e:
            log.info("Exception has occurred while test execution")
            log.error(e)
            assert False
