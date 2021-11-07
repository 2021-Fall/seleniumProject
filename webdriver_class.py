# The WebDriver class provides a number of properties or attributes for browser
# interaction. We can use the properties and methods of the WebDriver class to interact
# with the browser window, alerts, frames and pop-up windows. It also provides
# features to automate browser navigation, access cookies, capture screenshots, and
# so on. In this chapter, we will explore some of the most important features of the
# WebDriver class.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()

# 2. open the automationpractice.com demo website
driver.get("http://automationpractice.com/index.php")
search_box = driver.find_element(By.XPATH, "//input[@id='search_query_top']")
search_box.send_keys('dress' + Keys.ENTER)

# Try following WebDriver property/attributes or methods:
# current url, current window handle, name, title, window_handles
# back(), forward(), refresh(), switch_to.window(window_name)

url = driver.current_url
print('current url: ', url)
win_name = driver.current_window_handle
browser_name = driver.name
page_title = driver.title
win_names = driver.window_handles

print(win_name)
print(browser_name)
print(page_title)
print(win_names)

print("######### webdriver methods: ############")
# back(), forward(), refresh(), switch_to.window(window_name)
driver.back()
print('current url: ', driver.current_url)
driver.forward()
print('current url: ', driver.current_url)
time.sleep(5)
driver.refresh()
