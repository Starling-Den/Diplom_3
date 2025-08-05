from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.account_page_locators import AccountPageLocators
from data.data import *
from pages.base_page import BasePage

class AccountPage(BasePage):
    def open_login_page(self):
        self.navigate_to(login_site)

    def login(self, email, password):
        self.open_login_page()
        self.add_text_to_element(AccountPageLocators.email_input, email)
        self.add_text_to_element(AccountPageLocators.password_input, password)
        self.click_with_js(AccountPageLocators.button_login)
