from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from data.data import *
from pages.base_page import BasePage


class OrderPage(BasePage):

    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderPageLocators.order_counter))

    def get_today_completed_counter(self):
        element = self.find_element_with_wait(OrderPageLocators.today_counter)
        return int(element.text.strip())

    def open_feed_page(self):
        self.navigate_to(order_tape_site)
        self.wait_for_element_visible(OrderPageLocators.feed_title)

    def click_constructor(self):
        self.click_to_element(OrderPageLocators.constructor_button)

    def click_feed(self):
        self.click_when_clickable(OrderPageLocators.order_feed_button)

    def click_close_order_details(self):
        self.click_when_clickable(OrderPageLocators.close_order_details_button)

    def is_order_number_in_progress_place(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        self.find_and_format_locator(OrderPageLocators.order_in_progress_locator, formatted_id)
        return True

    def click_place_an_order(self):
        self.click_to_element(OrderPageLocators.place_an_order)

    def get_order_id_from_details(self):
        self.wait_for_element_visible(OrderPageLocators.order_id)
        return self.get_text_from_element(OrderPageLocators.order_id)
