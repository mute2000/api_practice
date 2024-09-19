from api.login import LoginApi

class TestLogin:
    uuid = None
    def setup_method(self):
        self.login_api = LoginApi()

        res_code = self.login_api.code()
        print(res_code.json())

        TestLogin.uuid = res_code.json().get("uuid")
        print(TestLogin.uuid)

    def test_login(self):
        login_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLogin.uuid
        }

        res_login = self.login_api.login(login_data=login_data)
        
        assert 200 == res_login.status_code

        assert '成功' in res_login.text

        assert 200 == res_login.json().get("code")
    
    def test_login2(self):
        login_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLogin.uuid
        }

        res_login = self.login_api.login(login_data=login_data)
        
        assert 200 == res_login.status_code

        assert '错误' in res_login.text

        assert 500 == res_login.json().get("code")

    def test_login3(self):
        login_data = {
            "username": "asjdajsdkj",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": TestLogin.uuid
        }

        res_login = self.login_api.login(login_data=login_data)
        
        assert 200 == res_login.status_code

        assert '错误' in res_login.text

        assert 500 == res_login.json().get("code")