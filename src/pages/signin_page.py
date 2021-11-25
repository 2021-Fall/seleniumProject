from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class SignInPage(BasePage):
    """
    locators and operations on Sign In Page
    """
    # Locators:
    __sign_in_link = "//a[contains(text(),'Sign in')]"
    __mr_gender_id = "id_gender1"
    __mrs_gender_id = "id_gender2"

    # operations (functions)
    def click_signin_link(self):
        self.click_element_by_locator(self.__sign_in_link)

    def select_gender(self, gender: str):
        if gender.lower() == 'mr':
            element = self.driver.find_element(By.ID, self.__mr_gender_id)
        else:
            element = self.driver.find_element(By.ID, self.__mrs_gender_id)
        element.click()


class SignUpPage(SignInPage):
    pass


class ContactsPage(BasePage):

    def select_heading(self, heading):
        pass
