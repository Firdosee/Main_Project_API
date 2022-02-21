from User.User_Authenticate import Test_User_Authenticate


class Test_Authenticate_User:
    def test_authenticate_user(self):
        userAuth = Test_User_Authenticate()
        userAuth.test_user_authenticate()