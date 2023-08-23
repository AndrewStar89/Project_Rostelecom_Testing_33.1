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


def test_positive_last_name():
    """Тест на проверку поля "Фамилия" при введении корректных данных
    (фамилия должна содержать минимум 2 символа состоящих из букв кириллицы или знака тире (-))."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'kc-register').click()  # Кнопка "Зарегистрироваться"

    element_registration_title = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    assert element_registration_title.text == 'Регистрация', 'Не произошёл переход на форму регистрации'

    # Вводим значение в поле "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').send_keys(RegistrationData.positive_last_name)

    pytest.driver.find_element(By.NAME, 'firstName').click()  # Нажимаем на поле "Имя"

    # Проверяем, что мы ввели корректные данные и сообщение об ошибке не появилось

    try:
        WebDriverWait(pytest.driver, 15).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                              'rt-input-container__meta')))
        not_found = False
    except Exception as e:
        not_found = True
        print(e)
    assert not_found, 'Введены неверные данные'

    # Удаляем содержимое поля "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').click()
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Keys.DELETE)

    # Вводим второе значение в поле "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').send_keys(RegistrationData.positive_last_name_2)

    pytest.driver.find_element(By.NAME, 'firstName').click()  # Нажимаем на поле "Имя"

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


def test_negative_last_name():
    """Тест на проверку поля "Фамилия" при введении некорректных данных
    (фамилия должна содержать минимум 2 символа состоящих из букв кириллицы или знака тире (-))."""

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/')

    # Локаторы:

    pytest.driver.find_element(By.ID, 'kc-register').click()  # Кнопка "Зарегистрироваться"

    element_registration_title = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    assert element_registration_title.text == 'Регистрация', 'Не произошёл переход на форму регистрации'

    # Вводим значение в поле "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').send_keys(RegistrationData.negative_last_name)

    pytest.driver.find_element(By.NAME, 'firstName').click()  # Нажимаем на поле "Имя"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Фамилия"

    element_last_name_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').click()
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Keys.DELETE)

    # Вводим второе значение в поле "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').send_keys(RegistrationData.negative_last_name_2)

    pytest.driver.find_element(By.NAME, 'firstName').click()  # Нажимаем на поле "Имя"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Фамилия"

    element_last_name_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    # Удаляем содержимое поля "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').click()
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Keys.CONTROL + "a")
    pytest.driver.find_element(By.NAME, 'lastName').send_keys(Keys.DELETE)

    # Вводим третье значение в поле "Фамилия"

    pytest.driver.find_element(By.NAME, 'lastName').send_keys(RegistrationData.negative_last_name_3)

    pytest.driver.find_element(By.NAME, 'firstName').click()  # Нажимаем на поле "Имя"

    time.sleep(3)  # Для визуального подтверждения, что появилось сообщение об ошибке в поле "Фамилия"

    element_last_name_error_message = WebDriverWait(pytest.driver, 15).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'rt-input-container__meta')))
    assert element_last_name_error_message.text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.', \
        'Введены верные данные. Сообщение об ошибке не появилось'

    pytest.driver.quit()

# python -m pytest -v --driver Chrome --driver-path /tests/chromedriver tests/registration_last_name.py
