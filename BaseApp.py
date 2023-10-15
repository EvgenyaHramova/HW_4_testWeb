import logging
from httpcore import TimeoutException
from logging_config import setup_logging
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = testdata['address']
        self.logger = setup_logging()

    def find_element(self, locator, time=10):
        try:            
            return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator),
                                                          message=f"элемент {locator} не найден")
        except:
            logging.exception('Find element exception:')
            element = None
        return element

    
    def get_element_property(self, locator, el_property):
        """Метод, возвращающий свойство одного элемента"""
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(el_property)
        else:
            logging.error(f'Property {el_property} not found in element with locator {locator}')
        return None

    def go_to_site(self):
        """Переход на указанную страницу"""
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception('Exception while open the site')
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception('Exception with alert')
            return None

    def close(self):
        self.driver.close()
        