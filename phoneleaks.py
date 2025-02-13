import os
import phonenumbers
import requests
from phonenumbers import geocoder, carrier

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_banner():
    print(r"""
 ██▓███   ██░ ██  ▒█████   ███▄    █ ▓█████  ██▓    ▓█████ ▄▄▄       ██ ▄█▀  ██████ 
▓██░  ██▒▓██░ ██▒▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▓██▒    ▓█   ▀▒████▄     ██▄█▒ ▒██    ▒ 
▓██░ ██▓▒▒██▀▀██░▒██░  ██▒▓██  ▀█ ██▒▒███   ▒██░    ▒███  ▒██  ▀█▄  ▓███▄░ ░ ▓██▄   
▒██▄█▓▒ ▒░▓█ ░██ ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██░    ▒▓█  ▄░██▄▄▄▄██ ▓██ █▄   ▒   ██▒
▒██▒ ░  ░░▓█▒░██▓░ ████▓▒░▒██░   ▓██░░▒████▒░██████▒░▒████▒▓█   ▓██▒▒██▒ █▄▒██████▒▒
▒▓▒░ ░  ░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒░▓  ░░░ ▒░ ░▒▒   ▓▒█░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
░▒ ░      ▒ ░▒░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░░ ░ ▒  ░ ░ ░  ░ ▒   ▒▒ ░░ ░▒ ▒░░ ░▒  ░ ░
░░        ░  ░░ ░░ ░ ░ ▒     ░   ░ ░    ░     ░ ░      ░    ░   ▒   ░ ░░ ░ ░  ░  ░  
          ░  ░  ░    ░ ░           ░    ░  ░    ░  ░   ░  ░     ░  ░░  ░         ░  
                                                                                     """)

def hlr_request(phone_number):
    parsed_number = phonenumbers.parse(phone_number, None)
    country = geocoder.description_for_number(parsed_number, "ru")
    carrier_name = carrier.name_for_number(parsed_number, "ru")
    region = geocoder.description_for_number(parsed_number, "ru")

    return {
        "Телефон": phone_number,
        "Страна": country,
        "Регион": region,
        "Оператор": carrier_name,
    }

def format_hlr_info(hlr_info):
    return f"""HLR Запрос:
├ Телефон: {hlr_info['Телефон']}
├ Страна: {hlr_info['Страна']}
├ Регион: {hlr_info['Регион']}
└ Оператор: {hlr_info['Оператор']}
"""

def leak_osint_request(phone_number, token):
    data = {
        "token": token,
        "request": phone_number,
        "limit": 100,
        "lang": "ru",
        "type": "short"  # или "json", в зависимости от требуемого формата
    }
    url = 'https://server.leakosint.com/'
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Поднимает исключение для плохих ответов
        return response.json()
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None

def format_osint_info(osint_info):
    formatted_info = ""

    if isinstance(osint_info, dict):
        if not osint_info:  # Проверка на пустой словарь
            formatted_info = "Не найдено\n"
        else:
            for key, value in osint_info.items():
                if key.lower() in ['mcc', 'mnc']:
                    formatted_info += f"├ {key.upper()}: {value}\n"
                else:
                    if isinstance(value, str):
                        value = value.replace('[+', '').replace(']', '').replace('{', '').replace('}', '')
                    formatted_info += f"├ {key}: {value}\n"
    elif isinstance(osint_info, list):
        if not osint_info:  # Проверка на пустой список
            formatted_info = "Не найдено\n"
        else:
            for entry in osint_info:
                if isinstance(entry, dict):
                    for key, value in entry.items():
                        if key.lower() in ['mcc', 'mnc']:
                            formatted_info += f"├ {key.upper()}: {value}\n"
                        else:
                            if isinstance(value, str):
                                value = value.replace('[+', '').replace(']', '').replace('{', '').replace('}', '')
                            formatted_info += f"├ {key}: {value}\n"
    else:
        formatted_info = "Не найдено\n"  # Если тип данных не соответствует ожидаемому

    return formatted_info

def main():
    while True:
        clear_screen()
        display_banner()
        token = input("API от LeakOsint: ")
        phone_number = input("Введите запрос:")

        hlr_info = hlr_request(phone_number)
        print(format_hlr_info(hlr_info))

        # Убедимся, что номер телефона имеет правильный формат для социальных сетей
        formatted_phone_number = phone_number.lstrip('+')  # Удаление символа '+' для формата URL

        print("\nСоциальные сети:")
        print(f"├ Ватсап: https://wa.me/{formatted_phone_number}")
        print(f"└ Телеграм: https://t.me/{formatted_phone_number}")

        osint_info = leak_osint_request(phone_number, token)
        if osint_info:
            print("\nБазы LeakOsint:")
            formatted_info = format_osint_info(osint_info)
            print(formatted_info)

        # Запрос на продолжение поиска
        cont = input("\nХотите продолжить поиск? (да/нет): ").strip().lower()
        if cont != 'да':
            break

if __name__ == "__main__":
    main()