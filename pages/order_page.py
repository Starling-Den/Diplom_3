from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators
from data.data import *
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Получаем общее кол-во заказов')
    def get_total_orders_counter(self):
        return int(self.get_text_from_element(OrderPageLocators.order_counter))

    @allure.step('Получаем кол-во заказов за день')
    def get_today_completed_counter(self):
        element = self.find_element_with_wait(OrderPageLocators.today_counter)
        return int(element.text.strip())

    @allure.step('Переходим на страницу с заказами')
    def open_feed_page(self):
        self.navigate_to(order_tape_site)
        self.wait_for_element_visible(OrderPageLocators.feed_title)

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor(self):
        self.click_to_element(OrderPageLocators.constructor_button)

    @allure.step('Кликаем по кнопке "Лента заказов"')
    def click_feed(self):
        self.click_when_clickable(OrderPageLocators.order_feed_button)

    @allure.step('Кликаем по кнопке закрытия окна с деталями заказа')
    def click_close_order_details(self):
        self.click_to_element(OrderPageLocators.close_order_details_button)

    @allure.step('Проверяем, находится ли номер заказа и колонке с заказами')
    def is_order_number_in_progress_place(self, order_id):
        formatted_id = f"{int(order_id):07d}"
        self.find_and_format_locator(OrderPageLocators.order_in_progress_locator, formatted_id)
        return True

    @allure.step('Кликаем по кнопке "Оформить заказ"')
    def click_place_an_order(self):
        self.click_to_element(OrderPageLocators.place_an_order)

    @allure.step('Получаем id заказа')
    def get_order_id_from_details(self):
        self.wait_for_element_visible(OrderPageLocators.order_id)
        return self.get_text_from_element(OrderPageLocators.order_id)
