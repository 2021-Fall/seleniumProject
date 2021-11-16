from time import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# VARIABLES - Test Data
email = 'mycool@email.com'
cust_fname = 'John'
cust_lname = 'Doe'
password = 'ForgetMeAsUsual123'
state = 'New Jersey'
filepath = '../screenshots/'

# STEPS
# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()

# 2. open the automationpractice.com demo website
driver.get("http://automationpractice.com/index.php")

# click on sign in
driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]").click()
sleep(3)

# enter email address to Create an Account field, mycool@email.com, click on create account
driver.find_element(By.ID, "email_create").send_keys(email)
driver.find_element(By.ID, "SubmitCreate").click()
sleep(3)

# radio button: click on Mr
mr_gender = driver.find_element(By.ID, "id_gender1")
mrs_gender = driver.find_element(By.ID, "id_gender2")
mrs_gender.click()

# Enter first name
cfirst_name = driver.find_element(By.NAME, "customer_firstname")
cfirst_name.send_keys(cust_fname)

# Enter last name
clast_name = driver.find_element(By.NAME, "customer_lastname")
clast_name.send_keys(cust_lname)

# Enter Password
driver.find_element(By.ID, "passwd")

# check Sign up for our newsletter
nl_checkbox = driver.find_element(By.ID, "newsletter")
nl_checkbox.click()
sleep(5)
driver.save_screenshot(filepath + 'signup1.png')

# clear it and enter different name
cfirst_name.clear()
cfirst_name.send_keys('Jonathan')

# verify email, get text , make sure it is what we entered
# verify Mr is selected
print("Is gender type MR selected? - ", mr_gender.is_selected())
print("Is gender type MRS selected? - ", mrs_gender.is_selected())
if mrs_gender.is_selected():
    mr_gender.click()

print("Is gender type MR selected? - ", mr_gender.is_selected())
print("Is gender type MRS selected? - ", mrs_gender.is_selected())

# verify Sign up is checked
print("Is Sign Up checkbox checked? - ", nl_checkbox.is_selected())

# verify One of the Error messages when required field is not entered
address_msg_xpath = "//input[@id='address1']/../span"
address_msg_elem = driver.find_element(By.XPATH, address_msg_xpath)
address_msg = ''
if address_msg_elem.is_displayed():
    address_msg = driver.find_element(By.XPATH, address_msg_xpath).text
else:
    print("Address message is not displayed.")
print("address_msg displayed: ", address_msg)
driver.save_screenshot(filepath + 'signup2.png')

# Drop down Select State
# verify state is selected
# html DOM - document object model
# driver.execute_script('arguments[0].click();', driver.find_element(By.ID, 'someid'))
driver.execute_script('window.scrollBy(0,800)')  # executing java script code

state_ddown = Select(driver.find_element(By.ID, 'id_state'))

state_ddown.select_by_value('2')
# state_ddown.options - returns all available options
print('current selections: ', state_ddown.all_selected_options[0].text)  # returns all selected options
sleep(5)
state_ddown.select_by_visible_text('California')
print('current selections: ', state_ddown.all_selected_options[0].text)  # returns all selected options
sleep(5)
state_ddown.select_by_index(2)
print('current selections: ', state_ddown.all_selected_options[0].text)  # returns all selected options

# H/W
# ....
# click on Register

# Agenda for next classes:
# practice websites: "https://courses.letskodeit.com/practice", "https://jqueryui.com/droppable/"

# Selenium - 2 classes:
# handling drop down list: Select class
# handling js Alert , ok, cancel, entering text, switch_to.Alert

# explicit wait : WebDriverWait class, expected_conditions class
# https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver

# mouse movements: hover over on the element, drag and drop : ActionChains Class

# Framework - 2 classes:
# Pytest (unit testing), Page object Modeling

# xpath: '//span[@class="inline-infos"]' vs css_selector: 'span.inline-infos'
