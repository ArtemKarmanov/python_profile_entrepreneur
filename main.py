# MyProfile app

separator = '------------------------------------------'

# user profile
user_name = ''
user_age = 0
user_phone_input = ''
user_phone = ''
user_email = ''
user_info = ''
user_postcode = ''
user_mail_adress = ''

# entrepreneuer profile
bank_checking_account = ''
bank_name = ''
bank_code = ''
bank_correspondent_account = ''
entrepreneur_number = ''
entrepreneur_number_taxpayer = ''

def numbers_count(number):
    number_count = 0
    while number > 0:
        number //= 10
        number_count += 1
    return number_count

def general_info_user(user_name, user_age, user_phone, user_email, user_postcode, user_mail_adress, user_info):
    print(separator)
    print('Имя:    ', user_name)
    if user_age % 10 == 1:
        years = 'год'
    elif 2 <= user_age % 10 <= 4:
        years = 'года'
    else: 
        years = 'лет'

    print('Возраст:', user_age, years)
    print('Телефон:', user_phone)
    print('E-mail: ', user_email)
    print('Индекс: ', user_postcode)
    print('Адрес: ', user_mail_adress)
    if user_info:
            print('Дополнительная информация:')
            print(user_info)

def info_entrepreneuer(entrepreneur_number, entrepreneur_number_taxpayer, bank_checking_account, bank_name, bank_code, bank_correspondent_account):
    print('\nИнформация о предпринимателе')
    print('ОГРНИП: ', entrepreneur_number)
    print('ИНН: ', entrepreneur_number_taxpayer)
    print('Банковские реквизиты')
    print('Р/с: ', bank_checking_account)
    print('Банк: ', bank_name)
    print('БИК: ', bank_code)
    print('К/с: ', bank_correspondent_account)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(separator)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу\n')

    option_menu = int(input('Введите номер пункта меню: '))
    if option_menu == 0:
            break

    if option_menu == 1:
        # submenu 1: edit info
        while True:
            print(separator)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад\n')

            option_edit = int(input('Введите номер пункта меню: '))
            if option_edit == 0:
                break
            if option_edit == 1:
                # input general info
                user_name = input('Введите имя: ')
                while True:
                    # validate user age
                    user_age = int(input('Введите возраст: '))
                    if user_age > 0:
                        break
                    print('Возраст должен быть положительным')
                
                user_phone_input = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                for number in user_phone_input:
                    if number == '+' or ('0' <= number <= '9'):
                        user_phone += number

                user_email = input('Введите адрес электронной почты: ')

                user_postcode_input = input('Введите почтовый индекс: ')
                for number in user_postcode_input:
                    if '0' <= number <= '9':
                        user_postcode += number

                user_mail_adress = input('Введите почтовый адрес (без индекса): ')
                user_info = input('Введите дополнительную информацию:\n')

            elif option_edit == 2:
                # input info entrepreneur
                while True:
                    entrepreneur_number = int(input('Введите ОГРНИП: '))
                    if numbers_count(entrepreneur_number) == 15:
                        break
                    print('Введите ОГРНИП состоящий из 15 цифр.')

                entrepreneur_number_taxpayer = int(input('Введите ИНН: '))
                while True:
                    bank_checking_account = int(input('Введите расчётный счёт: '))
                    if numbers_count(bank_checking_account) == 20:
                        break
                    print('Введите расчётный счёт состоящий из 20 цифр.')
              
                bank_name = input('Введите название банка: ')
                bank_code = int(input('Введите БИК: '))
                bank_correspondent_account = int(input('Введите корреспондентский счёт: '))
            else:
                print('Введите корректный пункт меню')
    elif option_menu == 2:
        # submenu 2: print info
        while True:
            print(separator)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад\n')

            option_info = int(input('Введите номер пункта меню: '))
            if option_info == 0:
                break
            if option_info == 1:
                general_info_user(user_name, user_age, user_phone, user_email, user_postcode, user_mail_adress, user_info)

            elif option_info == 2:
                general_info_user(user_name, user_age, user_phone, user_email, user_postcode, user_mail_adress, user_info)
              
                info_entrepreneuer(entrepreneur_number, entrepreneur_number_taxpayer, bank_checking_account, bank_name, bank_code, bank_correspondent_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
