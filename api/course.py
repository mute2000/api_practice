# 导包
import requests
# 创建接口类
class CourseApi:
    # 初始化
    def __init__(self):
        self.course_url = "https://kdtx-test.itheima.net/api/clues/course"
    # 添加课程
    def add_course(self, course_data, token):
        return requests.post(url=self.course_url, json=course_data, headers={"Authorization": token})