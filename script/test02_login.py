# 导包
import requests

# 发送请求
url = "https://kdtx-test.itheima.net/api/login"
header_data = {"Content-Type": "application/json"}
login_data = {
  "username": "admin",
  "password": "HM_2023_test",
  "code": "2",
  "uuid": "447914350a9d4c68b52a4c3cff385326"
}

response = requests.post(url = url, headers=header_data, json=login_data)

# 断言
print(response.status_code)
print(response.json())
