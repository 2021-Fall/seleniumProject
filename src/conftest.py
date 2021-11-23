import pytest
from time import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='session')
def driver():
    # SETUP - steps to do before <scope>
    print("\n*********** I am a SETUP **************************")
    print("initializing the browser...")
    opts = Options()
    opts.add_argument('--disable-notifications')
    # options.add_argument('--headless')  # running the chrome on background
    # 1. open the browser
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(20)  # synchronizing the browser
    driver.maximize_window()

    yield driver
    print("\n*********** I am a TEARDOWN **************************")
    sleep(5)
    print("closing the browser ...")
    driver.quit()
    print("Test cases are completed!!")


