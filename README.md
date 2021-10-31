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



