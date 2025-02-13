import os
import sys
from pystyle import Colors, Write, Center
import faker

def clear_console():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

def print_banner():
    banner = r'''
  ___ _   _  ____ ___   ____ _   _ ___ _____  _     
 |_ _| \ | |/ ___/ _ \ / ___| \ | |_ _|_   _|/ \    
  | ||  \| | |  | | | | |  _|  \| || |  | | / _ \   
  | || |\  | |__| |_| | |_| | |\  || |  | |/ ___ \  
 |___|_| \_|\____\___/ \____|_| \_|___| |_/_/   \_\ 
               РАЗРАБОТЧИК: @KADICK1                
               
'''
    Write.Print(banner, Colors.blue_to_white, interval=0.0000000000000001)

def generate_fake_data(num_persons):
    fake = faker.Faker('ru_RU')
    generated_data = []
    with open('Incognits.txt', 'w', encoding='utf-8') as file:
        for _ in range(num_persons):
            fake_name = fake.name()
            fake_gender = fake.random_element(elements=('Мужчина', 'Женщина'))
            fake_address = fake.address()
            fake_email = fake.email()
            fake_phone = fake.phone_number()
            fake_job = fake.job()
            fake_company = fake.company()
            fake_birthdate = fake.date_of_birth(minimum_age=18, maximum_age=90)
            fake_ssn = fake.ssn()
            fake_username = fake.user_name()
            fake_password = fake.password()
            fake_credit_card = fake.credit_card_full()
            fake_ip = fake.ipv4()
            fake_country = fake.country()
            fake_city = fake.city()

            data_entry = {
                "Имя": fake_name,
                "Пол": fake_gender,
                "Адрес": fake_address,
                "Email": fake_email,
                "Телефон": fake_phone,
                "Профессия": fake_job,
                "Компания": fake_company,
                "Дата рождения": fake_birthdate,
                "Социальный номер": fake_ssn,
                "Имя пользователя": fake_username,
                "Пароль": fake_password,
                "Кредитная карта": fake_credit_card,
                "IP адрес": fake_ip,
                "Страна": fake_country,
                "Город": fake_city,
            }
            generated_data.append(data_entry)

            file.write(f"Имя: {fake_name}\n")
            file.write(f"Пол: {fake_gender}\n")
            file.write(f"Адрес: {fake_address}\n")
            file.write(f"Email: {fake_email}\n")
            file.write(f"Телефон: {fake_phone}\n")
            file.write(f"Профессия: {fake_job}\n")
            file.write(f"Компания: {fake_company}\n")
            file.write(f"Дата рождения: {fake_birthdate}\n")
            file.write(f"Социальный номер: {fake_ssn}\n")
            file.write(f"Имя пользователя: {fake_username}\n")
            file.write(f"Пароль: {fake_password}\n")
            file.write(f"Кредитная карта: {fake_credit_card}\n")
            file.write(f"IP адрес: {fake_ip}\n")
            file.write(f"Страна: {fake_country}\n")
            file.write(f"Город: {fake_city}\n")
            file.write("\n\n")

    if num_persons <= 100:
        for data in generated_data:
            for key, value in data.items():
                Write.Print(f"{key}: {value}", Colors.blue_to_white, interval=0.0000000000000001)
                print()
            print()
        print()
        Write.Print("Личности сгенерированы и сохранены в файл Incognits.txt.", Colors.blue_to_white, interval=0.0000000000000001)

while True:
    clear_console()
    print_banner()

    Write.Print("Сколько личностей сгенерировать? ", Colors.blue_to_white, interval=0.0000000000000001)
    try:
        num_persons = int(input())
        if num_persons <= 0:
            raise ValueError
    except ValueError:
        Write.Print("\nПожалуйста, введите положительное целое число.", Colors.blue_to_white, interval=0.0000000000000001)
        Write.Print("\nНажмите Enter, чтобы продолжить...", Colors.blue_to_white, interval=0.0000000000000001)
        input()
        continue

    clear_console()
    print_banner()

    generate_fake_data(num_persons)

    if num_persons > 100:
        print()
        Write.Print("Личности сгенерированы и сохранены в файл Incognits.txt.", Colors.blue_to_white, interval=0.0000000000000001)

    Write.Print("\nНажмите Enter, чтобы начать сначала...", Colors.blue_to_white, interval=0.0000000000000001)
    input()
