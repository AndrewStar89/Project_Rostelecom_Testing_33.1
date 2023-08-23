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


def test_positive_mail_and_phone():
    """Тест на проверку поля "E-mail или мобильный телефон" при введении корректных данных
    (телефон должен быть в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, email должен быть в формате example@email.ru)."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'kc-register').click()  # Кнопка "Зарегистрироваться"

    element_registration_title = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    assert element_registration_title.text == 'Регистрация', 'Не произошёл переход на форму регистрации'

    # Вводим значение в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.positive_email)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

    # Проверяем, что мы ввели корректные данные и сообщение об ошибке не появилось

    try:
        WebDriverWait(pytest.driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                               'rt-input-container__meta')))
        not_found = False
    except Exception as e:
        not_found = True
        print(e)
    assert not_found, 'Введены неверные данные'

    # Удаляем содержимое поля "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').click()
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим второе значение в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.positive_phone)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

    # Проверяем, что мы ввели корректные данные и сообщение об ошибке не появилось

    try:
        WebDriverWait(pytest.driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                               'rt-input-container__meta')))
        not_found = False
    except Exception as e:
        not_found = True
        print(e)
    assert not_found, 'Введены неверные данные'

    # Удаляем содержимое поля "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').click()
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим третье значение в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.positive_phone_2)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

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


def test_negative_mail_and_phone():
    """Тест на проверку поля "E-mail или мобильный телефон" при введении некорректных данных
    (телефон должен быть в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, email должен быть в формате example@email.ru)."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'kc-register').click()  # Кнопка "Зарегистрироваться"

    element_registration_title = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    assert element_registration_title.text == 'Регистрация', 'Не произошёл переход на форму регистрации'

    # Вводим значение (случайные символы) в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.negative_mail_or_phone)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

    time.sleep(3)
    # Для визуального подтверждения, что появилось сообщение об ошибке в поле "E-mail или мобильный телефон"

    element_mail_or_phone_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_mail_or_phone_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                       'или email в формате example@email.ru', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').click()
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим второе значение (спецсимволы) в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.negative_mail_or_phone_2)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

    time.sleep(3)
    # Для визуального подтверждения, что появилось сообщение об ошибке в поле "E-mail или мобильный телефон"

    element_mail_or_phone_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_mail_or_phone_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                       'или email в формате example@email.ru', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').click()
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим третье значение (кодировка (кириллица, китайские символы)) в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.negative_mail_or_phone_3)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

    time.sleep(3)
    # Для визуального подтверждения, что появилось сообщение об ошибке в поле "E-mail или мобильный телефон"

    element_mail_or_phone_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_mail_or_phone_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                       'или email в формате example@email.ru', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').click()
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим четвёртое значение (числа) в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.negative_mail_or_phone_4)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

    time.sleep(3)
    # Для визуального подтверждения, что появилось сообщение об ошибке в поле "E-mail или мобильный телефон"

    element_mail_or_phone_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_mail_or_phone_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                       'или email в формате example@email.ru', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').click()
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Вводим пятое значение (строка длиной больше 1000 символов) в поле "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').send_keys(RegistrationData.negative_mail_or_phone_5)

    pytest.driver.find_element(By.ID, 'password').click()  # Нажимаем на поле "Пароль"

    time.sleep(3)
    # Для визуального подтверждения, что появилось сообщение об ошибке в поле "E-mail или мобильный телефон"

    element_mail_or_phone_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_mail_or_phone_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                       'или email в формате example@email.ru', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "E-mail или мобильный телефон"

    pytest.driver.find_element(By.ID, 'address').click()
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.ID, 'address').send_keys(Keys.DELETE)

    # Нажимаем на кнопку "Зарегистрироваться" с незаполненными полями

    pytest.driver.find_element(By.NAME, 'register').click()

    time.sleep(3)
    # Для визуального подтверждения, что появилось сообщение об ошибке в поле "E-mail или мобильный телефон"

    element_mail_or_phone_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_mail_or_phone_error_message.text == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, ' \
                                                       'или email в формате example@email.ru' or \
           'Необходимо заполнить поле кириллицей. От 2 до 30 символов.' or \
           'Длина пароля должна быть не менее 8 символов', 'Введены верные данные. Сообщение об ошибке не появилось'

    pytest.driver.quit()

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver tests/registration_e-mail_or_phone.py
