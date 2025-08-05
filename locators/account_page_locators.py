from selenium.webdriver.common.by import By


class AccountPageLocators:

    button_account = (By.XPATH, "//p[contains(text(), 'Личный Кабинет']")
    button_login = (By.CSS_SELECTOR, '.button_button__33qZ0')
    button_logout = (By.XPATH, "//button[contains(text(), 'Выход')]")
    email_input = (By.XPATH, "//input[@name='name']")
    password_input = (By.XPATH, "//input[@name='Пароль']")
    button_order_history = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium']")
    order_finish = (By.XPATH, "//p[@class='OrderHistory_visible__19YMB text text_type_main-small'")
    login_after_logout = (By.XPATH, "//h2[contains(text*(, 'Вход')]")
    login_logout_burger = (By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']")
