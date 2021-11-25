from time import *

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# VARIABLES
email = 'mycool@email.com'
cust_fname = 'John'
cust_lname = 'Doe'
password = 'ForgetMeAsUsual123'
state = 'New Jersey'
filepath = '../../screenshots/'


# STEPS
# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
# driver.maximize_window()

# 2. open the automationpractice.com demo website
url = "https://jqueryui.com/droppable/"
driver.get(url)
driver.switch_to.frame(0)

frome = driver.find_element(By.ID, 'draggable')
toel = driver.find_element(By.ID, 'droppable')
sleep(2)
actions = ActionChains(driver)
actions.drag_and_drop(frome, toel).perform()
actions.click_and_hold(frome).move_to_element(toel).perform()
