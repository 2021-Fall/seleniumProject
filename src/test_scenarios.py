# from src.webelement_alerts import *
# from src.webelement_class import *
import pytest
email = 'mycool@email.com'


# STEPS
# 1. open the browser
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)  # synchronizing the browser
# driver.maximize_window()

# ---------    EXECUTIONS ----------------
# test_alert_single_button()
# test_alert_multi_button()

# test_go_to_authentication_page()
# test_create_account(email)
# test_explicit_wait()
# test_drag_drop()
# test_mouse_hover_over(driver)
#
# assert sum_of_num(3, 4) == 7  # make sure it returns = 7
# assert sum_of_num(-1, 6) == 5
# # assert sum_of_num('a', 6) == 'whee'  # requirement, BA, user, sme
# # assert sum_of_num('%', '\n') == 'Error'
#
# assert divide_num(4, 2) == 2
# assert divide_num(3, 0) != 0, "divide_num assertion failed"
#
# sleep(5)
# driver.quit()


@pytest.mark.myFirstCase
@pytest.mark.sample1
@pytest.mark.regression
def test_sample_pytst():
    assert 25 / 5 == 5
    print("\n TEST1: yeaah this is the first pytest executions!!!")


@pytest.mark.mySecondCase
@pytest.mark.regression
def test_sample_pytst2():
    print("\n TEST2: this is the first pytest executions!!!")
    assert 25 / 5 == 65
