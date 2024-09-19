from api.login import LoginApi
import pytest


test_data = [
    ("admin", "HM_2023_test", 200, "成功", 200),
    ("", "HM_2023_test", 200, "错误", 500),
    ("asjdajsdkj", "HM_2023_test", 200, "错误", 500),
]
class TestLogin:
    uuid = None
    def setup_method(self):
        self.login_api = LoginApi()

        res_code = self.login_api.code()
        print(res_code.json())

        TestLogin.uuid = res_code.json().get("uuid")
        print(TestLogin.uuid)
    @pytest.mark.parametrize("username, password, status, manage, code", test_data)
    def test_login(self, username, password, status, manage, code):
        login_data = {
            "username": username,
            "password": password,
            "code": "2",
            "uuid": TestLogin.uuid
        }

        res_login = self.login_api.login(login_data=login_data)
        
        assert status == res_login.status_code

        assert manage in res_login.text

        assert code == res_login.json().get("code")
    