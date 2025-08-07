import pytest
from selenium import webdriver
from data.data import *

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(main_site)
    yield driver
    driver.quit()
