from time import *
import pytest

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class BasePage:
    """
    Base class for all other pages, includes common selenium operations
    """

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(self.driver, 20)

    def click_element_by_locator(self, locator, method='xpath', wait_time=10):
        """click with explicit wait"""
        try:
            # elem = driver.find_element(xpath) - this is with implicit wait
            self.wdwait = WebDriverWait(self.driver, wait_time)
            element = object  # very general data type
            if method == 'xpath':
                element = self.wdwait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elif method == 'id':
                element = self.wdwait.until(EC.presence_of_element_located((By.ID, locator)))
            elif method == 'css':
                element = self.wdwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            element.click()
        except (NoSuchElementException, TimeoutException) as err:
            print('Error on click element by locator, check locator', locator)
            print(err)

    def enter_text_by_locator(self, message, locator, method='xpath'):
        try:
            element = object  # very general data type
            if method == 'xpath':
                element = self.wdwait.until(EC.presence_of_element_located((By.XPATH, locator)))
            elif method == 'id':
                element = self.wdwait.until(EC.presence_of_element_located((By.ID, locator)))
            elif method == 'css':
                element = self.wdwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            element.send_keys(message)
        except (NoSuchElementException, TimeoutException) as err:
            print('Error on enter text by locator, check locator', locator)
            print(err)
            pytest.fail("Entering Text by locator failed.")

    def is_element_displayed(self, xpath):
        # logic here
        return True
