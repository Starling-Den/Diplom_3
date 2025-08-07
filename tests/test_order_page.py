from data.data import email, password
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_page import OrderPage
from tests.conftest import driver
import pytest
import allure

import time

class TestOrderPage:
    @allure.title('Тест увеличения счетчика заказов после создания нового заказа')
    def test_all_counter_increase_after_new_order(self, driver):
        order_feed_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Заходим в аккаунт'):
            account_page.login(email, password)
        with allure.step('Нажимаем на "Ленту заказов"'):
            order_feed_page.click_feed()
        with allure.step('Смотрим на текущий счетчик заказов за все время'):
            begin_all_counter = order_feed_page.get_total_orders_counter()
        with allure.step('Оформляем заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.click_place_an_order()
        with allure.step('Закрываем окно с деталями'):
            order_feed_page.click_close_order_details()
        with allure.step('Заходим на страницу с заказами'):
            order_feed_page.open_feed_page()
        with allure.step('Снова смотрим на текущий счетчик заказов за все время'):
            finish_all_counter = order_feed_page.get_total_orders_counter()
        with allure.step('Проверяем, что счетчик стал больше после оформления заказа'):
            assert finish_all_counter > begin_all_counter

    @allure.title('Тест увеличения счетчика заказов за сегодня после создания нового заказа')
    def test_all_counter_today_increase_after_new_order(self, driver):
        order_feed_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Заходим в аккаунт'):
            account_page.login(email, password)
        with allure.step('Нажимаем на "Ленту заказов"'):
            order_feed_page.click_feed()
        with allure.step('Смотрим на текущий счетчик заказов за сегодня'):
            begin_today_counter = order_feed_page.get_today_completed_counter()
        with allure.step('Оформляем заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.click_place_an_order()
        with allure.step('Закрываем окно с деталями'):
            order_feed_page.click_close_order_details()
        with allure.step('Заходим на страницу с заказами'):
            order_feed_page.click_feed()
        with allure.step('Снова смотрим на текущий счетчик заказов за сегодня'):
            finish_today_counter = order_feed_page.get_today_completed_counter()
        with allure.step('Проверяем, что счетчик стал больше после оформления заказа'):
            assert finish_today_counter > begin_today_counter

    @allure.title('Тест появления номера заказа в колонке "В работе" после оформления заказа')
    def test_order_number_appear_in_progress_place(self, driver):
        order_feed_page = OrderPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Заходим в аккаунт'):
            account_page.login(email, password)
        with allure.step('Оформляем заказ'):
            order_feed_page.click_constructor()
            main_page.drag_and_drop_ingredient()
            order_feed_page.click_place_an_order()
        with allure.step('Смотрим на id заказа'):
            order_id = order_feed_page.get_order_id_from_details()
        with allure.step('Закрываем окно с деталями'):
            order_feed_page.click_close_order_details()
        with allure.step('Заходим на страницу с заказами'):
            order_feed_page.click_feed()
        with allure.step('Проверяем, что id заказа появился в колонке "В работе"'):
            assert order_feed_page.is_order_number_in_progress_place(order_id)
