from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ждем и находим элемент')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Считываем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Кликаем по элементу')
    def click_to_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Заполняем поле')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Форматируем локатор')
    def format_locator(self, locator, num):
        method, locator_str = locator
        locator_str = locator_str.format(num)
        return method, locator_str

    @allure.step('Кликаем по элементу, когда кликабелен')
    def click_when_clickable(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Ждем выполнения условия')
    def wait_until_condition(self, condition, timeout=40):
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step('Проверяем, появился ли элемент')
    def is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Ждем изменения текста элемента по локатору')
    def find_and_wait_until_text_changes(self, locator, initial_text, timeout=40):
        self.wait_until_condition(
            lambda _: self.get_text_from_element(locator) != initial_text, timeout
        )
        return self.find_element_with_wait(locator)

    @allure.step('Ждем появление элемента')
    def wait_for_element_visible(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Перетаскиваем')
    def drag_and_drop(self, source_locator, target_locator):
        """
        Перетаскивает элемент из source_locator в target_locator используя ActionChains.

        Args:
            source_locator: Локатор исходного элемента (например, (By.ID, "element1"))
            target_locator: Локатор целевого элемента (например, (By.CSS_SELECTOR, ".target"))
        """
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)

        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()

    @allure.step('Проверяем, отображается ли элемент')
    def is_element_displayed(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element.is_displayed()
        except TimeoutException:
            return False

    @allure.step('Переходим на страницу')
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step('Находим и форматируем элемент')
    def find_and_format_locator(self, locator, dynamic_value):
        formatted_locator = self.format_locator(locator, dynamic_value)
        return self.find_element_with_wait(formatted_locator)

    @allure.step('Кликаем по элементу с помощью js')
    def click_with_js(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)
