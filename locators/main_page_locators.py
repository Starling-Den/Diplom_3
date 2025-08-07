from selenium.webdriver.common.by import By

class MainPageLocators:

    button_construct = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    order_feed_button = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")

    ingredient_bun = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    ingredient_counter = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    burger_constructor_section = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")

    completed_orders = (By.XPATH, "//p[contains(text(), 'Готовы:')]")

    close_ingredient_details_button = (
    By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

    order_target_top = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
