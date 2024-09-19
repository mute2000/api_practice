# 导包
from api.login import LoginApi
from api.course import CourseApi
from api.contract import ContractApi

class TestAddContract:
    # 定义类级别变量
    token = None
    # 前置处理
    def setup_method(self):
        # 实例化接口对象
        self.login_api = LoginApi()
        self.course_api = CourseApi()
        self.contract_api = ContractApi()
    # 后置处理
    def teardown_method(self):
        pass

    # 登录成功    
    def test_login(self):
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
        TestAddContract.token = res_login.json().get("token")

    # 添加课程
    def test_addContract(self):
        add_data = {
            "name":"课程01",
            "subject":"6",
            "price":"899",
            "applicablePerson":"2",
            "info":"课程01"
        }
        res_course = self.course_api.add_course(course_data=add_data, token = TestAddContract.token)
        print(res_course.status_code)
        print(res_course.json())

    # 上传合同
    def test_uploadContract(self):
        f = open("./data/test.pdf","rb")
        res_contract = self.contract_api.upload_contract(contract_data=f, token = TestAddContract.token)
        print(res_contract.status_code)
        print(res_contract.json())

    # 添加合同
    def test_addContract(self):
        add_data = {
            "name":"测试1",
            "phone":"15155949221",
            "contractNo":"HT20251111",
            "subject":"6",
            "courseId":"99",
            "channel":"0",
            "activityId":77,
            "filename":"{{fileName}}"
        }
        res_contract = self.contract_api.add_contract(add_contract_data=add_data, token = TestAddContract.token)
        print(res_contract.status_code)
        print(res_contract.json())