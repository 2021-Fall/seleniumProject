# Title of the page
## Title 2 text
### title 3

# Selenium WebDriver with Python

## Selenium setup
1.  download selenium
go to the Terminal (pycharm)
    ```python
    pip install selenium # library, code written by developers, open source
    pip freeze # to check the selenium is in the list
    ```
2. download chromedriver 
   - check the version of your chrome browser (if you dont have chrome browser, donwload and install it)
   - download the chromedriver from this location: [driver website](https://chromedriver.storage.googleapis.com/index.html?path=95.0.4638.54/)
    - select chromedriver_win32.zip if you have windows
    - Extract the downloaded folder and copy the chromedriver file

3. save in the Python main location  
   - Go to  python main folder: "C:\Program Files\Python39"
   - paste the copied chromedriver file here
    
4. import selenium, run sample code

```python
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.thelevelupsolutions.com/")
driver.maximize_window()
driver.quit() # close all tabs
```


## What is HTML?
- Document Object Model - html document (DOM)
- tag : 
  head, body, div, button, 
  span, a (links)
  input (text, password, submit, checkbox, radio, file)
  form, select, 
```html
<head></head>
<body></body>
```

### Using chrome developers tools options to inspect web elements
- Tags are purple
- Attributes are in red
- Values of the attributes will be in blue
- text in the elements, that are in the tags, will be in black


hw: read and try out 
- https://www.w3schools.com/html/html_intro.asp
- https://www.w3schools.com/html/html_elements.asp
- https://www.w3schools.com/html/html_attributes.asp
- https://www.w3schools.com/html/html_links.asp
- https://www.w3schools.com/html/html_forms.asp (all other pages for html forms)


### Finding the element 

```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()

driver.find_element_by_id() # fastest way of finding element from html document.
driver.find_element_by_name()

driver.find_element_by_xpath()      # technics, build
driver.find_element_by_css_selector()  # technics, build 

driver.find_element_by_link_text()
driver.find_elements_by_class_name() # class names might be dynamic
driver.find_element_by_partial_link_text()
driver.find_element_by_tag_name()

```


### Agenda for Automation classes on Selenium

- webdriver - handling browser 
- webelement - working with elements
- framework - manage the code better