import random
import string
import os
import hashlib
from datetime import datetime
from faker import Faker
from pystyle import Colors, Colorate, Center
import qrcode

fake = Faker()

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_custom_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Невозможно создать пароль: не выбраны символы для использования.")
    
    return ''.join(random.choice(characters) for _ in range(length))

def prompt_password_criteria():
    length = int(input("Введите длину пароля: "))
    use_uppercase = input("Использовать заглавные буквы? (y/n): ").lower() == 'y'
    use_digits = input("Использовать цифры? (y/n): ").lower() == 'y'
    use_symbols = input("Использовать символы? (y/n): ").lower() == 'y'
    
    return generate_custom_password(length, use_uppercase, use_digits, use_symbols)

def generate_number(country_code):
    number = fake.phone_number()
    return f"+{country_code} {number}"

def generate_identity():
    return fake.name()

def generate_mullvad_key():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

def generate_discord_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(59))

def generate_credit_card():
    return fake.credit_card_number(card_type=None)

def generate_email():
    return fake.email()

def generate_birthdate():
    return fake.date_of_birth()

def generate_uuid():
    return fake.uuid4()

def generate_mac():
    return fake.mac_address()

def generate_address():
    return fake.address()

def generate_username():
    return fake.user_name()

def generate_quote():
    return fake.sentence()

def generate_company():
    return fake.company()

def generate_job():
    return fake.job()

def generate_license_plate():
    return fake.license_plate()

def generate_ssn():
    return fake.ssn()

def generate_coordinates():
    latitude = round(random.uniform(-90.0, 90.0), 6)
    longitude = round(random.uniform(-180.0, 180.0), 6)
    return f"Latitude: {latitude}, Longitude: {longitude}"

def generate_fake_news():
    headlines = [
        "Ученые обнаружили новый вид насекомых в Амазонке",
        "Известный актер объявил о своем участии в новом проекте",
        "Исследование показало, что шоколад полезен для здоровья",
        "Новая технология обещает революцию в медицине",
        "Археологи нашли древний артефакт в Египте"
    ]
    bodies = [
        "Сегодня утром команда исследователей сообщила о своем открытии.",
        "Событие вызвало бурную реакцию в социальных сетях.",
        "Эксперты предсказывают значительное влияние на индустрию.",
        "Местные жители выражают свою поддержку.",
        "Новость распространилась с невероятной скоростью."
    ]
    return f"Headline: {random.choice(headlines)}\nBody: {random.choice(bodies)}"

def generate_color_palette():
    def random_color():
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))
    palette = [random_color() for _ in range(5)]
    return palette

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img_path = "qrcode.png"
    img.save(img_path)
    return img_path

def generate_bitcoin_address():
    return fake.cryptocurrency_address()

def generate_bitcoin_private_key():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(64))

def generate_stock_profile():
    return {
        "company": fake.company(),
        "symbol": ''.join(random.choices(string.ascii_uppercase, k=4)),
        "price": round(random.uniform(10, 1000), 2),
        "volume": random.randint(1000, 1000000)
    }

def generate_medical_profile():
    return {
        "name": fake.name(),
        "age": random.randint(0, 100),
        "blood_type": random.choice(["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]),
        "conditions": [fake.word() for _ in range(random.randint(0, 5))]
    }

def generate_passport_details():
    return {
        "passport_number": ''.join(random.choices(string.ascii_uppercase + string.digits, k=9)),
        "name": fake.name(),
        "nationality": fake.country(),
        "birthdate": fake.date_of_birth(),
        "expiry_date": fake.date_between(start_date="today", end_date="+10y")
    }

def print_gradient_text(text):
    print(Colorate.Vertical(Colors.green_to_white, text))

def print_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    title = """
  
   
                                                                                                                
     **                                     *                                                                   
      **                            *     **                                                                    
      **                           **     **                                                                    
      **                           **     **                                                                    
      **                         ******** **                                                       ***  ****    
  *** **      ***       ****    ********  **  ***       ****         ***    ***  ****       ***     **** **** * 
 *********   * ***     * ***  *    **     ** * ***     *  ***  *    * ***    **** **** *   * ***     **   ****  
**   ****   *   ***   *   ****     **     ***   ***   *    ****    *   ***    **   ****   *   ***    **         
**    **   **    *** **    **      **     **     **  **     **    **    ***   **    **   **    ***   **         
**    **   ********  **    **      **     **     **  **     **    ********    **    **   ********    **         
**    **   *******   **    **      **     **     **  **     **    *******     **    **   *******     **         
**    **   **        **    **      **     **     **  **     **    **          **    **   **          **         
**    **   ****    * **    **      **     **     **  **     **    ****    *   **    **   ****    *   ***        
 *****      *******   ***** **      **    **     **   ********     *******    ***   ***   *******     ***       
  ***        *****     ***   **            **    **     *** ***     *****      ***   ***   *****                
                                                 *           ***                                                
                                                *      ****   ***                                               
                                               *     *******  **                                                
                                              *     *     ****                                                  
                                                                                                                  
                      
   
                                                                            
"""

    developer = "Owner: @deathrebootpvp (Я ЛЮБЛЮ КАЖДЫЙ ДЕНЬ ВЕСЕЛЬЕ)"
    lines = "═" * 72

    menu = """
╔═══════════════════════════════════════════════════════════════════════════════════╗
║  1. Генерация Пароля             15. Генерация Должности                          ║
║  2. Генерация Номера             16. Генерация Номера Лицензии                    ║
║  3. Генерация Личности           17. Генерация SSN                                ║
║  4. Генерация Ключей Мулвад      18. Генерация QR-кода                            ║
║  5. Генерация Токенов Дискорд    19. Генерация Координат                          ║
║  6. Генерация Банковской Карты   20. Генерация Фальшивых Новостей                 ║
║  7. Генерация Email              21. Генерация Цветовых Палитр                    ║
║  8. Генерация Даты Рождения      22. Генерация Пользовательского Пароля           ║
║  9. Генерация UUID               23. Генерация Bitcoin-адреса                     ║
║ 10. Генерация MAC-адреса         24. Генерация Bitcoin-ключа                      ║
║ 11. Генерация Адреса             25. Генерация Акции                              ║
║ 12. Генерация Имени Пользователя 26. Генерация Медицинского Портфолио             ║
║ 13. Генерация Цитаты             27. Генерация Паспортных Данных                  ║
║ 14. Генерация Компании           28. Выход                                        ║
╚═══════════════════════════════════════════════════════════════════════════════════╝
    """

    print_gradient_text(Center.XCenter(title))
    print()
    print_gradient_text(Center.XCenter(lines))
    print_gradient_text(Center.XCenter(developer))
    print_gradient_text(Center.XCenter(lines))
    print()
    print_gradient_text(Center.XCenter(menu))

def main():
    while True:
        print_menu()
        option = input("Выберите опцию: ")

        if option == '1':
            print("Сгенерированный пароль:", generate_password())
        elif option == '2':
            country_code = input("Введите код страны: ")
            print("Сгенерированный номер телефона:", generate_number(country_code))
        elif option == '3':
            print("Сгенерированная личность:", generate_identity())
        elif option == '4':
            print("Сгенерированный ключ Mullvad:", generate_mullvad_key())
        elif option == '5':
            print("Сгенерированный токен Discord:", generate_discord_token())
        elif option == '6':
            print("Сгенерированный номер банковской карты:", generate_credit_card())
        elif option == '7':
            print("Сгенерированный email:", generate_email())
        elif option == '8':
            print("Сгенерированная дата рождения:", generate_birthdate())
        elif option == '9':
            print("Сгенерированный UUID:", generate_uuid())
        elif option == '10':
            print("Сгенерированный MAC-адрес:", generate_mac())
        elif option == '11':
            print("Сгенерированный адрес:", generate_address())
        elif option == '12':
            print("Сгенерированное имя пользователя:", generate_username())
        elif option == '13':
            print("Сгенерированная цитата:", generate_quote())
        elif option == '14':
            print("Сгенерированная компания:", generate_company())
        elif option == '15':
            print("Сгенерированная должность:", generate_job())
        elif option == '16':
            print("Сгенерированный номер лицензии:", generate_license_plate())
        elif option == '17':
            print("Сгенерированный SSN:", generate_ssn())
        elif option == '18':
            data = input("Введите данные для QR-кода: ")
            qr_path = generate_qr(data)
            print(f"QR-код сохранен как {qr_path}")
        elif option == '19':
            print("Сгенерированные координаты:", generate_coordinates())
        elif option == '20':
            print("Сгенерированные фальшивые новости:", generate_fake_news())
        elif option == '21':
            print("Сгенерированная цветовая палитра:", generate_color_palette())
        elif option == '22':
            print("Сгенерированный пользовательский пароль:", prompt_password_criteria())
        elif option == '23':
            print("Сгенерированный Bitcoin-адрес:", generate_bitcoin_address())
        elif option == '24':
            print("Сгенерированный Bitcoin-ключ:", generate_bitcoin_private_key())
        elif option == '25':
            print("Сгенерированный профиль акции:", generate_stock_profile())
        elif option == '26':
            print("Сгенерированное медицинское портфолио:", generate_medical_profile())
        elif option == '27':
            print("Сгенерированные паспортные данные:", generate_passport_details())
        elif option == '28':
            print("Выход")
            break
        else:
            print("Неверная опция. Пожалуйста, выберите снова.")
        
        input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    main()
