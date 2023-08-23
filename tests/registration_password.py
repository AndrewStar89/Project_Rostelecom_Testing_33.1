import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from variables import RegistrationData
import time


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    pytest.driver.implicitly_wait(15)  # Задаем неявное ожидание 15 сек
    pytest.driver.set_window_size(1920, 1080)

    yield

    pytest.driver.quit()


def test_positive_password():
    """Тест на проверку поля "Пароль" при введении корректных данных
    (длина пароля должна быть не менее 8 символов, пароль должен содержать хотя бы одну заглавную букву,
    пароль должен содержать только латинские буквы)."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'kc-register').click()  # Кнопка "Зарегистрироваться"

    element_registration_title = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    assert element_registration_title.text == 'Регистрация', 'Не произошёл переход на форму регистрации'

    pytest.driver.find_element(By.CLASS_NAME, 'rt-eye-icon').click()  # Нажимаем на значок видимости пароля

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(RegistrationData.positive_password)

    pytest.driver.find_element(By.ID, 'password-confirm').click()  # Нажимаем на поле "Подтверждение пароля"

    # Проверяем, что мы ввели корректные данные и сообщение об ошибке не появилось

    try:
        WebDriverWait(pytest.driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                              'rt-input-container__meta')))
        not_found = False
    except Exception as e:
        not_found = True
        print(e)
    assert not_found, 'Введены неверные данные'

    # Удаляем содержимое поля "Пароль"

    pytest.driver.find_element(By.ID, 'password').click()
    pytest.driver.find_element(By.ID, 'password').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'password').send_keys(Keys.DELETE)

    # Вводим второе значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(RegistrationData.positive_password_2)

    pytest.driver.find_element(By.ID, 'password-confirm').click()  # Нажимаем на поле "Подтверждение пароля"

    # Проверяем, что мы ввели корректные данные и сообщение об ошибке не появилось

    try:
        WebDriverWait(pytest.driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                              'rt-input-container__meta')))
        not_found = False
    except Exception as e:
        not_found = True
        print(e)
    assert not_found, 'Введены неверные данные'

    pytest.driver.quit()


def test_negative_password():
    """Тест на проверку поля "Пароль" при введении некорректных данных (Кириллица)
    (длина пароля должна быть не менее 8 символов, пароль должен содержать хотя бы одну заглавную букву,
    пароль должен содержать только латинские буквы)."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'kc-register').click()  # Кнопка "Зарегистрироваться"

    element_registration_title = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    assert element_registration_title.text == 'Регистрация', 'Не произошёл переход на форму регистрации'

    pytest.driver.find_element(By.CLASS_NAME, 'rt-eye-icon').click()  # Нажимаем на значок видимости пароля

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(RegistrationData.negative_password)

    pytest.driver.find_element(By.ID, 'password-confirm').click()  # Нажимаем на поле "Подтверждение пароля"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Пароль"

    element_password_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_password_error_message.text == 'Длина пароля должна быть не менее 8 символов', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "Пароль"

    pytest.driver.find_element(By.ID, 'password').click()
    pytest.driver.find_element(By.ID, 'password').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'password').send_keys(Keys.DELETE)

    # Вводим второе значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(RegistrationData.negative_password_2)

    pytest.driver.find_element(By.ID, 'password-confirm').click()  # Нажимаем на поле "Подтверждение пароля"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Пароль"

    element_password_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_password_error_message.text == 'Пароль должен содержать только латинские буквы', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    pytest.driver.quit()


def test_negative_password_2():
    """Тест на проверку поля "Пароль" при введении некорректных данных (Латиница)
    (длина пароля должна быть не менее 8 символов, пароль должен содержать хотя бы одну заглавную букву,
    пароль должен содержать только латинские буквы)."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'kc-register').click()  # Кнопка "Зарегистрироваться"

    element_registration_title = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    assert element_registration_title.text == 'Регистрация', 'Не произошёл переход на форму регистрации'

    pytest.driver.find_element(By.CLASS_NAME, 'rt-eye-icon').click()  # Нажимаем на значок видимости пароля

    # Вводим значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(RegistrationData.negative_password_3)

    pytest.driver.find_element(By.ID, 'password-confirm').click()  # Нажимаем на поле "Подтверждение пароля"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Пароль"

    element_password_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_password_error_message.text == 'Пароль должен содержать хотя бы одну заглавную букву', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "Пароль"

    pytest.driver.find_element(By.ID, 'password').click()
    pytest.driver.find_element(By.ID, 'password').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'password').send_keys(Keys.DELETE)

    # Вводим второе значение в поле "Пароль"

    pytest.driver.find_element(By.ID, 'password').send_keys(RegistrationData.negative_password_4)

    pytest.driver.find_element(By.ID, 'password-confirm').click()  # Нажимаем на поле "Подтверждение пароля"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Пароль"

    element_password_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_password_error_message.text == 'Длина пароля должна быть не менее 8 символов', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    pytest.driver.quit()

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver tests/registration_password.py
