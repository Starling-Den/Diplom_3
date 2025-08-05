from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    def click_construct(self):
        self.click_to_element(MainPageLocators.button_construct)

    def click_order_feed(self):
        self.click_to_element(MainPageLocators.order_feed_button)

    def click_ingredient(self):
        self.click_to_element(MainPageLocators.ingredient_bun)

    def is_order_feed_counter_visible(self):
        return self.find_element_with_wait(MainPageLocators.completed_orders).is_displayed()

    def is_burger_constructor_visible(self):
        return self.find_element_with_wait(MainPageLocators.burger_constructor_section).is_displayed()

    def is_ingredient_details_visible(self):
        return self.is_element_displayed(MainPageLocators.close_ingredient_details_button)

    def close_ingredient_details(self):
        self.click_to_element(MainPageLocators.close_ingredient_details_button)

    def get_ingredient_counter(self):
        return int(self.get_text_from_element(MainPageLocators.ingredient_counter))

    def drag_and_drop_ingredient(self):
        self.drag_and_drop(MainPageLocators.ingredient_bun, MainPageLocators.order_target_top)