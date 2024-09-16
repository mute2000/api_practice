# 导包
import requests

# 发送请求
response = requests.get(url="https://kdtx-test.itheima.net/api/captchaImage")

# 断言
print(response.status_code)
print(response.text)
