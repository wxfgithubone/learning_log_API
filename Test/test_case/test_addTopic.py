from Test.Common.addApi import Add
from Test.Utils.getExcelData import get_data
import pytest
import os

topic_data = get_data(2, 6)


class TestAddTopic:
    @pytest.mark.parametrize('in_body, exp_data', topic_data)
    def test_add_topic(self, in_body, exp_data):
        reps = Add().add_topic(in_body)
        assert reps.url == exp_data


if __name__ == '__main__':
    pytest.main(['test_addTopic.py', '-s', '--alluredir', '../../Report/tmp'])
    os.system('allure generate ../../Report/tmp -o ../../Report/report')
    os.system('allure serve ../../Report/tmp')







