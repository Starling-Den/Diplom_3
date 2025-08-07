import time

from pages.account_page import AccountPage
from pages.main_page import MainPage
from tests.conftest import driver
import pytest
import allure


class TestMainPage:
    @allure.title('Тест перехода по клику на конструктор')
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Переходим на страницу логина'):
            account_page.open_login_page()
        with allure.step('Жмем на кнопку "Конструктор'):
            main_page.click_construct()
        with allure.step('Проверяем, что на странице появился блок с "Соберите бургер"'):
            assert main_page.is_burger_constructor_visible()

    @allure.title('Тест перехода по клику на ленту заказов')
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Переходим на страницу логина'):
            account_page.open_login_page()
        with allure.step('Жмем на кнопку "Лента Заказов'):
            main_page.click_order_feed()
        with allure.step('Проверяем, что на странице появился блок с "Лента заказов"'):
            assert main_page.is_order_feed_counter_visible()

    @allure.title('Тест появления окна с деталями при клике на ингредиент')
    def test_click_ingredient(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Переходим на страницу логина'):
            account_page.open_login_page()
        with allure.step('Жмем на кнопку "Конструктор'):
            main_page.click_construct()
        with allure.step('Жмем на ингредиент'):
            main_page.click_ingredient()
        with allure.step('Проверяем, что появилось окно с деталями'):
            assert main_page.is_ingredient_details_visible()

    @allure.title('Тест закрытия окна с деталями при клике по крестику')
    def test_close_details(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Переходим на страницу логина'):
            account_page.open_login_page()
        with allure.step('Жмем на кнопку "Конструктор'):
            main_page.click_construct()
        with allure.step('Жмем на ингредиент'):
            main_page.click_ingredient()
        with allure.step('Жмем на крестик'):
            main_page.close_ingredient_details()
        with allure.step('Проверяем, что окно с деталями закрылось'):
            assert not main_page.is_ingredient_details_visible()

    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        with allure.step('Переходим на страницу логина'):
            account_page.open_login_page()
        with allure.step('Жмем на кнопку "Конструктор'):
            main_page.click_construct()
        with allure.step('Смотрим на счетчик ингредиента'):
            begin_counter = main_page.get_ingredient_counter()
        with allure.step('Перетаскиваем булку'):
            main_page.drag_and_drop_ingredient()
        with allure.step('Снова мотрим на счетчик ингредиента'):
            finish_counter = main_page.get_ingredient_counter()
        with allure.step('Проверяем, что счетчик увеличился на 2'):
            assert finish_counter == begin_counter + 2
