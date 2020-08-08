import requests
from lxml import html
from config import HOST


class Login(object):
    """返回sessionid"""

    def __init__(self):
        self.login_url = f'{HOST}/users/login/'

    def get_session(self):
        res = requests.get(url=self.login_url)
        csrf_cookie = requests.utils.dict_from_cookiejar(res.cookies)['csrftoken']
        tree = html.fromstring(res.text)
        auth_token = tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')[0]
        from_data = {
            "username": "wxf", "password": "wxf990824",
            "csrfmiddlewaretoken": auth_token, "next": "/", "submit": ""
        }
        header = {
            "Cookie": f"csrftoken={csrf_cookie}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
                          " (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
        }
        reps = requests.post(url=self.login_url, data=from_data,
                             headers=header, allow_redirects=False)  # allow_redirects=False禁止重定向
        user_cookie = {"sessionid": reps.cookies['sessionid']}
        return user_cookie


if __name__ == '__main__':
    print(Login().get_session())
    # Login().get_cookie()











