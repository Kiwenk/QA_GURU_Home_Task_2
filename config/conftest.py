import pytest
from selene import browser

#Фикстура для запуска браузера с определёнными параметрами + закрытие на тирдайуне
@pytest.fixture(autouse=True)
def browser_management():
    browser.config.window_width = 1200
    browser.config.window_height = 1200
    yield
    browser.quit()
