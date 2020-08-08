from config import HOST
from Test.Common.loginApi import Login
import requests


class Del(object):
    """删除类"""

    def __init__(self):
        self.session = Login().get_session()
        self.header = {"Content-Type": "application/x-www-form-urlencoded"}

    def del_entry(self):
        url = f'{HOST}/del_entry/6/'
        reps = requests.get(url=url, headers=self.header, cookies=self.session)
        return reps.text

    def del_img(self):
        url = f'{HOST}/del_img/7/'
        reps = requests.get(url=url, headers=self.header, cookies=self.session)
        return reps.text


if __name__ == '__main__':
    print(Del().del_img())



