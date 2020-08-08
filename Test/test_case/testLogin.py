from lib.apiLib.apiLogin import LoginApi
from lib.webLib.getExcelData import get_excel_data
import json, pytest

# for one in range(1, 5):
#     #  获取数据
#     bodyData = get_excel_data('sheetName', one)
#     # 登录发送请求
#     res = LoginApi().login(bodyData[0])
#     # 断言
#     expData = json.loads(bodyData[1]['message'])
#     if res['message'] == expData:
#         print('pass')
#     else:
#         print('fail')


# class Test01:
#     @pytest.mark.parametrize('in_data', [1, 2, 3])
#     def test_01(self, in_data):
#         assert 1+1 == in_data


class TestLogin:
    # @pytest.mark.parametrize('in_body, ecp_data',)
    def test_login(self):
        res = LoginApi().login()
        assert res['message'] == '登录成功'


if __name__ == '__main__':
    pytest.main(['testLogin.py'])


