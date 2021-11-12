from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()

# 2. open the google.com
driver.get("https://www.google.com/")

# 3. search for 'selenium'
search_box = driver.find_element(By.NAME, 'q')  # selenium 3, 4
# entering the text in the input (text) form
search_box.send_keys('selenium')
search_box.send_keys(Keys.ENTER)

# 4. capture the result text
result_msg = driver.find_element(By.ID, 'result-stats').text
print('I got the result here: \n\t', result_msg)

# 5. close the browser
# driver.close()   # closes current tab
driver.quit()  # close all tabs
