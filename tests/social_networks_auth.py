import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.implicitly_wait(15)  # Задаем неявное ожидание 15 сек
    pytest.driver.set_window_size(1920, 1080)

    yield

    pytest.driver.quit()


def test_vk_transition():
    """Тест на проверку перехода на вход в аккаунт с помощью соц. сети VK, кнопка "VK"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'oidc_vk').click()  # Кнопка "VK"

    element_vk_enter = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'vkuiLink')))
    assert element_vk_enter.text == 'Подробнее о VK ID', 'Не произошёл переход на "Вход с помощью VK ID"'

    time.sleep(3)  # Для визуального подтверждения совершённого перехода

    pytest.driver.quit()


def test_odnoklassniki_transition():
    """Тест на проверку перехода на вход в аккаунт с помощью соц. сети Одноклассники, кнопка "Одноклассники"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'oidc_ok').click()  # Кнопка "Одноклассники"

    element_odnoklassniki_enter = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'ext-widget_h_tx')))
    assert element_odnoklassniki_enter.text == 'Одноклассники', \
        'Не произошёл переход на вход в аккаунт с помощью соц. сети "Одноклассники"'

    time.sleep(3)  # Для визуального подтверждения совершённого перехода

    pytest.driver.quit()


def test_mail_transition():
    """Тест на проверку перехода на вход в аккаунт с помощью соц. сети Mail.ru, кнопка "Mail.ru"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'oidc_mail').click()  # Кнопка "Mail.ru"

    element_mail_enter = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'header__logo')))
    assert element_mail_enter.text == 'Мой Мир@Mail.Ru', \
        'Не произошёл переход на вход в аккаунт с помощью соц. сети "Mail.ru"'

    time.sleep(3)  # Для визуального подтверждения совершённого перехода

    pytest.driver.quit()


def test_yandex_transition():
    """Тест на проверку перехода на вход в аккаунт с помощью соц. сети Яндекс, кнопка "Яндекс"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'oidc_ya').click()  # Кнопка "Яндекс"

    time.sleep(3)  # Для визуального подтверждения совершённого перехода

    element_yandex_enter = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.TAG_NAME, 'h1')))
    assert element_yandex_enter.text == 'Войдите с Яндекс ID', \
        'Не произошёл переход на вход в аккаунт с помощью соц. сети "Яндекс"'

    pytest.driver.quit()

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver tests/social_networks_auth.py
