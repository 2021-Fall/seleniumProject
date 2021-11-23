from src.webelement_alerts import *
from webelement_class import *


email = 'mycool@email.com'

# STEPS
# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()

# ---------    EXECUTIONS ----------------
# test_alert_single_button()
# test_alert_multi_button()

# test_go_to_authentication_page()
# test_create_account(email)
# test_explicit_wait()
# test_drag_drop()
test_mouse_hover_over(driver)

sleep(5)
driver.quit()