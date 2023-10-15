import time
import yaml
import pytest
from testpage import OperationsHelper

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


# site = Site(testdata['address'])

def test_login(browser):
    value = OperationsHelper(browser)
    value.go_to_site()
    value.enter_login(testdata['username'])
    value.enter_password(testdata['password'])
    value.enter_button()
    assert True


def test_contact_us(browser):
    value = OperationsHelper(browser)
    value.go_to_site()
    value.enter_login(testdata['username'])
    value.enter_password(testdata['password'])
    value.enter_button()
    time.sleep(3)
    value.enter_link()
    time.sleep(3)
    value.enter_name(testdata['name'])
    value.enter_email(testdata['email'])
    value.enter_content(testdata['content'])
    value.enter_contact_us()
    assert True


if __name__ == '__main__':
    pytest.main(['-v'])