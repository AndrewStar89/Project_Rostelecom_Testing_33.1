import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from variables import AuthData
import time


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.implicitly_wait(15)  # Задаем неявное ожидание 15 сек
    pytest.driver.set_window_size(1920, 1080)

    yield

    pytest.driver.quit()


def test_positive_auth_login():
    """Тест на проверку авторизации клиента по корректному логину и корректному паролю, кнопка "Логин"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    time.sleep(20)  # на случай появления CAPTCHA

    # Локаторы:

    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()  # Кнопка "Логин"

    # Вводим значение в поле "Логин"

    pytest.driver.find_element(By.CLASS_NAME, 'rt-input__input').send_keys(AuthData.login)

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(AuthData.password)

    pytest.driver.find_element(By.ID, 'kc-login').click()  # Кнопка "Войти"

    element_personal_account = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.ID, 'lk-btn')))
    assert element_personal_account.text == 'Личный кабинет', 'Не произошёл вход в учётную запись'
    pytest.driver.find_element(By.ID, 'logout-btn').click()  # Кнопка "Выйти"

    pytest.driver.quit()


def test_negative_auth_login():
    """Тест на проверку авторизации клиента по некорректному логину и корректному паролю, кнопка "Логин"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()  # Кнопка "Логин"

    # Вводим значение в поле "Логин"

    pytest.driver.find_element(By.CLASS_NAME, 'rt-input__input').send_keys(AuthData.invalid_login)

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(AuthData.password)

    pytest.driver.find_element(By.ID, 'kc-login').click()  # Кнопка "Войти"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке

    element_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.ID, 'form-error-message')))
    assert element_error_message.text == 'Неверный логин или пароль', 'Введённые данные оказались верны'

    pytest.driver.quit()

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver tests/auth_login.py
