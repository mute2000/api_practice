from api.login import LoginApi

class TestAddContract:
    def setup_method(self):
        self.login_api = LoginApi()


    def test_addContract(self):
        # 获取验证码
        res_code = self.login_api.code()
        print(res_code.status_code)
        print(res_code.json())

        login_data1 = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_code.json().get("uuid")
        }        

        # 登录
        res_login = self.login_api.login(login_data=login_data1)
        print(res_login.status_code)
        print(res_login.json())