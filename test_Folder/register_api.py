#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/7/21 0010 23:09
# @Author : 王**
# @Site : 广州 
# @File : register.py
# @Software: PyCharm
import requests
import json
base_url = "http://localhost:8000/user/login/"  # 访问的url


def get_token():
    """获取token供后面的接口使用"""
    re = requests.get(base_url)
    cookie = re.cookies
    token = re.cookies.items()[0][1]
    print("get登陆的cookie：", cookie)
    return token


url = 'http://localhost:8000/'
client = requests.session()
client.get(url)
if 'csrftoken' in client.cookies:
    csrftoken = client.cookies['csrftoken']
else:
    csrftoken = client.cookies['csrf']
print(csrftoken)


def register():
    """注册"""
    url = 'http://localhost:8000/users/register/'
    body = {"username": "测试07",
            "password1": "wxf123456",
            "password2": "wxf123456"}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
              "X-CSRFToken": csrftoken}
    re_1 = requests.post(url, body, headers=header, cookies=client.cookies)
    cookie_1 = re_1.cookies
    print(re_1)
    return cookie_1


print("注册的cookie：", register())


def new_topic():
    """添加主题"""
    url = "http://localhost:8000/new_topic/"
    body = {"text": "灌灌灌灌灌灌灌灌灌灌灌灌灌"}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
              "X-CSRFToken": csrftoken}
    re_2 = requests.post(url, body, headers=header, cookies=client.cookies)
    cookie_2 = re_2.cookies['csrftoken']
    print(re_2)
    return cookie_2

print(new_topic())


class LoginFN(object):
    """
    构造请求数据
    """
    def __init__(self):
        self.url_open = 'http://localhost:8000/topics/'
        self.url_login = 'http://localhost:8000/users/login/'

        self.s = requests.Session()

        # 加headers 伪造请求头。
        self.s.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko)Chrome/51.0.2704.103 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        # 取消安全认证
        self.s.verify = False

    def get_csrf_token(self):
        """
        因为登录时需要先获取csrfToken值，所以先get获取，
        然后在下方post数据的时候使用。
        :return: csrfToken
        """
        page = self.s.get(self.url_open)
        csrfToken = page.cookies['csrftoken']
        return csrfToken

    def login_fn(self):
        csrfToken = self.get_csrf_token()
        form_data = {
            'username': '测试01',
            'password': 'wxf123456',
            'captcha': '',
            'chkRememberMe': 'true',
            'referer': 'aHR0cHM6Ly9ob21lLmJldGExLmZuL21lbWJlci9ob21l',
            'CSRF_TOKEN': csrfToken,
            'deviceId': '801142e17bf4ecc19cbbb32b22eec213',
        }
        req = self.s.post(self.url_login, data=form_data)
        # res = json.loads(req.content)  # 把json 对象转换成python对象
        # assert res['ret'] == 200  # 开发自定义的一个status,登录成功就返还ret 200
        print(req.content)


if __name__ == '__main__':
    LoginFN().login_fn()













