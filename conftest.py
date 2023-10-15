import yaml
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from logging import log

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)



@pytest.fixture()
def browser():
    #site1 = BasePage(testdata['address'])
    service = Service(testdata['driver_path'])
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)
    driver.maximize_window()
    # driver.get(address)
    # time.sleep(testdata['sleep_time'])
    yield driver
    driver.quit()