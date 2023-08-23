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


def test_positive_auth_personal_account():
    """Тест на проверку авторизации клиента по корректному номеру лицевого счёта и корректному паролю,
    кнопка "Лицевой счёт"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    time.sleep(20)  # на случай появления CAPTCHA

    # Локаторы:

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()  # Кнопка "Лицевой счёт"

    # Вводим значение в поле "Лицевой счёт"

    pytest.driver.find_element(By.CLASS_NAME, 'rt-input__input').send_keys(AuthData.personal_account)

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(AuthData.password)

    pytest.driver.find_element(By.ID, 'kc-login').click()  # Кнопка "Войти"

    element_personal_account = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.ID, 'lk-btn')))
    assert element_personal_account.text == 'Личный кабинет', 'Не произошёл вход в учётную запись'
    pytest.driver.find_element(By.ID, 'logout-btn').click()  # Кнопка "Выйти"

    pytest.driver.quit()


def test_negative_auth_personal_account():
    """Тест на проверку авторизации клиента по некорректному номеру лицевого счёта и корректному паролю,
    кнопка "Лицевой счёт"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()  # Кнопка "Лицевой счёт"

    # Вводим значение в поле "Лицевой счёт"

    pytest.driver.find_element(By.CLASS_NAME, 'rt-input__input').send_keys(AuthData.invalid_personal_account)

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(AuthData.password)

    pytest.driver.find_element(By.ID, 'kc-login').click()  # Кнопка "Войти"

    element_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.ID, 'form-error-message')))
    assert element_error_message.text == 'Неверный логин или пароль', 'Введённые данные оказались верны'

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке

    pytest.driver.quit()


def test_negative_auth_personal_account_2():
    """Тест на проверку авторизации клиента по некорректному номеру лицевого счёта, кнопка "Лицевой счёт".
    Ожидаем текст ошибки с сообщением "Проверьте, пожалуйста, номер лицевого счета"."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()  # Кнопка "Лицевой счёт"

    # Вводим значение в поле "Лицевой счёт"

    pytest.driver.find_element(By.CLASS_NAME, 'rt-input__input').send_keys(AuthData.personal_account[:-1])

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(AuthData.password)

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Лицевой счёт"

    element_error_message_for_personal_account = WebDriverWait(pytest.driver, 15).until(ec.presence_of_element_located(
        (By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_error_message_for_personal_account.text == 'Проверьте, пожалуйста, номер лицевого счета', \
        'Верный номер лицевого счёта'

    pytest.driver.quit()

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver tests/auth_personal_account.py
