from selenium.webdriver.common.by import By

class OrderPageLocators:
    place_an_order = (By.XPATH,
                      "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")

    constructor_button = (By.XPATH, "//p[contains(text(), 'Конструктор')]")

    order_counter = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    today_counter = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")

    feed_title = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")

    close_order_details_button = (By.XPATH, "//button[@type='button']//*[name()='svg']")

    order_in_progress_locator = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li[1]")

    order_id = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")

    order_feed_button = (By.XPATH, "//p[contains(text(), 'Лента Заказов')]")
