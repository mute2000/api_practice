# 接口封装时，依据的接口文档封装接口信息，需要使用的测试数据从测试用例传递，接口方法被调用需要时需要返回响应数据


# 导包
import requests

# 创建接口类
class LoginApi:
    # 初始化
    def __init__(self):
        self.code_url = "https://kdtx-test.itheima.net/api/captchaImage"
        self.login_url = "https://kdtx-test.itheima.net/api/login"

    # 验证码接口
    def code(self):
        return requests.get(url=self.code_url)
    # 登录接口
    def login(self, login_data):
        return requests.post(url=self.login_url, json=login_data)
