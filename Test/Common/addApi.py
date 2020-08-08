from config import HOST
import requests
import json
from Test.Common.loginApi import Login


class Add(object):
    """新增类"""
    def __init__(self):
        self.session = Login().get_session()
        self.header = {"Content-Type": "application/x-www-form-urlencoded"}

    def add_topic(self, in_body):
        url = f'{HOST}/new_topic/'
        payload = in_body
        in_body = json.loads(payload)
        reps = requests.post(url=url, data=in_body, headers=self.header, cookies=self.session, allow_redirects=False)
        return reps.cookies

    def add_entry(self):
        url = f'{HOST}/new_entry/10/'
        payload = {"text": "你好，接口自动化填写"}
        reps = requests.post(url=url, data=payload, headers=self.header, cookies=self.session, allow_redirects=False)
        return reps.text

    def add_student(self):
        url = f'{HOST}/add_student/'
        payload = {
            "st_name": "你好，接口自动化填写",
            "age": "18",
            "sex": "男",
            "phone": "13052277120",
            "home": "河南"
        }
        reps = requests.post(url=url, data=payload, headers=self.header, cookies=self.session, allow_redirects=False)
        return reps.text

    def add_course(self):
        url = f'{HOST}/add_course/12/'
        payload = {
            "course": "语文",
            "score": "87"
        }
        reps = requests.post(url=url, data=payload, headers=self.header, cookies=self.session, allow_redirects=False)
        return reps.text

    def add_img(self):
        url = 'http://localhost:8000/add_img/'
        data = {"name": "你好，接口自动化填写"}
        payload = {"headimg": ('2023491.jpg', open('../../Data/2023491.jpg', 'rb'), 'image/jpeg')}
        reps = requests.post(url=url, data=data, files=payload, cookies=self.session, allow_redirects=False)
        return reps.text


if __name__ == '__main__':
    print(Add().add_topic())













