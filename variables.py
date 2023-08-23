import random
from string import printable

"""Данные для авторизации"""


class AuthData:
    phone_number = '+7 900 000-00-00'  # Введите свои данные

    password = 'EnterYourPassword!'  # Введите свои данные
    invalid_password = 'Something!'

    email = 'enteryour@mail.ru'  # Введите свои данные
    invalid_email = 'something666@mail.ru'

    login = 'rtkid_0000000000000'  # Введите свои данные
    invalid_login = 'rtkid_0000000000000'

    personal_account = '000000000000'  # Введите свои данные
    invalid_personal_account = '000000000000'


"""Данные для регистрации"""


class RegistrationData:
    positive_name = 'Андрей'
    positive_name_2 = 'Ан'
    negative_name = 'Andrew'
    negative_name_2 = 'А'
    negative_name_3 = '-Андрейандрейандрейандрейандрейандрей-'

    positive_last_name = 'Стародедов'
    positive_last_name_2 = 'Ст'
    negative_last_name = 'Starodedov'
    negative_last_name_2 = 'С'
    negative_last_name_3 = '-Стародедовстародедовстародедовстародедов-'

    positive_password = 'QATesting123'
    positive_password_2 = 'QATest12'
    negative_password = 'Тесты'
    negative_password_2 = 'Тесты123'
    negative_password_3 = 'qatesting123'
    negative_password_4 = 'QATest'

    positive_email = 'example@email.ru'
    positive_phone = '+7 000 000-00-00'
    positive_phone_2 = '+375 00 000-00-00'
    negative_mail_or_phone = 'qwerty!#&?'
    negative_mail_or_phone_2 = '☺☻♥♫☼►•™'
    negative_mail_or_phone_3 = 'Неверная电子邮件'
    negative_mail_or_phone_4 = '123456789'

    # Генерация строки из случайных символов

    def random_string_generator(self):

        random_string = ''.join(printable[random.randint(0, len(printable) - 1)] for _ in range(self))

        # Присвоение значения переменной

        value = random_string

        return value

    random_string = random_string_generator(1500)

    # Удаление всех символов, которые не являются буквами, цифрами или точкой
    # и объединение полученного результата в одну строку

    def remove_whitespace(self):
        return ''.join(c for c in self if c.isalpha() or c.isdigit() or c == '.')

    result = remove_whitespace(random_string)

    # Присвоение переменной результата функции со случайными символами

    negative_mail_or_phone_5 = result
