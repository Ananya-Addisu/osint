import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import whois
import ipaddress
from ipwhois import IPWhois
import socket
import requests
import logging
import os
import tkinter as tk
from tkinter import filedialog, messagebox, Label, Button, W, Entry, StringVar
from urllib.parse import quote
import webbrowser
import json
import exiftool
from scapy.all import IP, ICMP, send
import time

logging.basicConfig(level=logging.INFO)

def get_phone_info(phone_number: str) -> str:
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        if not phonenumbers.is_valid_number(parsed_number):
            return "Номер телефона недействителен."
        
        country = geocoder.description_for_number(parsed_number, "ru")
        operator = carrier.name_for_number(parsed_number, "ru")
        timezones = timezone.time_zones_for_number(parsed_number)
        number_type = "мобильный" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "стационарный"
        
        return (f"Страна: {country}\n"
                f"Оператор: {operator}\n"
                f"Тип номера: {number_type}\n"
                f"Часовые пояса: {', '.join(timezones)}")
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Неверный формат номера телефона. Пожалуйста, используйте международный формат."

def get_ip_from_domain(domain: str) -> str:
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror as e:
        logging.error(f"Ошибка получения IP для домена {domain}: {e}")
        return None

def get_ip_info(ip: str) -> str:
    obj = IPWhois(ip)
    res = obj.lookup_rdap()
    network = res.get('network', {})
    asn_info = f"ASN: {res['asn']} ({res['asn_description']})" if res.get('asn') else "ASN: Не доступно"
    return (f"IP: {ip}\n"
            f"Страна: {network.get('country', 'Не доступно')}\n"
            f"Организация: {network.get('name', 'Не доступно')}\n"
            f"CIDR: {network.get('cidr', 'Не доступно')}\n"
            f"Дата начала: {network.get('start_address', 'Не доступно')}\n"
            f"Дата окончания: {network.get('end_address', 'Не доступно')}\n"
            f"{asn_info}")

def get_domain_ip_info(query: str) -> str:
    try:
        ipaddress.ip_address(query)
        return get_ip_info(query)
    except ValueError:
        try:
            ip = get_ip_from_domain(query)
            if ip:
                return get_ip_info(ip)
            else:
                return "Не удалось получить IP-адрес для данного домена."
        except Exception as e:
            logging.error(f"Ошибка при получении информации о домене {query}: {e}")
            return f"Ошибка при получении информации о домене: {e}"

def get_mac_info(mac: str) -> str:
    try:
        url = f"https://api.macvendors.com/{mac}"
        response = requests.get(url)
        if response.status_code == 200:
            vendor_info = response.text
            return f"Производитель MAC-адреса: {vendor_info}"
        else:
            return "Не удалось получить информацию о производителе MAC-адреса."
    except Exception as e:
        logging.error(f"Ошибка при получении информации о MAC-адресе {mac}: {e}")
        return f"Ошибка при получении информации о MAC-адресе: {e}"

def generate_search_links(image_url: str) -> dict:
    """Создает ссылки поиска на разных сервисах."""
    links = {
        'Яндекс': f'https://yandex.ru/images/touch/search?rpt=imageview&url={quote(image_url)}',
        'Google': f'https://www.google.com/searchbyimage?&image_url={quote(image_url)}&client=firefox-b-d',
        'Google Объектив': f'https://lens.google.com/uploadbyurl?url={quote(image_url)}',
        'TinEye': f'https://www.tineye.com/search/?url={quote(image_url)}',
        'UnlimBot': f'https://www.bing.com/images/search?view=detailv2&iss=sbi&form=SBIVSP&sbisrc=UrlPaste&q=imgurl:"{quote(image_url)}"'
    }
    return links

def open_link(url: str):
    """Открывает ссылку в браузере."""
    webbrowser.open_new_tab(url)

def start_search():
    """Запускает поиск по изображениям."""
    image_url = image_url_var.get()
    if not image_url:
        messagebox.showerror("Ошибка", "Введите ссылку на изображение!")
        return

    search_links = generate_search_links(image_url)

    # Создаем диалоговое окно с результатами
    result_window = tk.Toplevel(root)
    result_window.title("Ссылки для поиска")

    # Отображаем ссылки в диалоговом окне
    for i, (name, url) in enumerate(search_links.items()):
        link_label = Label(result_window, text=f"{name}: {url}")
        link_label.pack(anchor=W, padx=10, pady=5)

        # Создаем кнопку для открытия ссылки
        link_button = Button(result_window, text="Открыть", command=lambda url=url: open_link(url))
        link_button.pack(anchor=W, padx=10, pady=5)

def open_image_search():
    global root, image_url_var
    root = tk.Tk()
    root.title("Обратный поиск по изображениям")

    button_select = tk.Button(root, text="Загрузить изображение на Yapx.ru", command=lambda: messagebox.showinfo("Инструкции", "1. Загрузите изображение на Yapx.ru:\nhttps://yapx.ru/\n2. Скопируйте ссылку на изображение.\n3. Вставьте ссылку в поле ниже."))
    button_select.pack()

    label_image_url = Label(root, text="Вставьте ссылку на изображение:")
    label_image_url.pack()

    image_url_var = StringVar()
    image_url_entry = Entry(root, textvariable=image_url_var)
    image_url_entry.pack()

    button_search = tk.Button(root, text="Начать поиск", command=start_search)
    button_search.pack()

    root.mainloop()

def get_leak_info(query: str) -> str:
    try:
        url = f"https://api.proxynova.com/comb?query={query}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            count = data.get("count", 0)
            lines = data.get("lines", [])
            result = f"Количество утечек: {count}\n"
            result += "\n".join(lines)
            return result
        else:
            return "Не удалось получить информацию по утечкам."
    except Exception as e:
        logging.error(f"Ошибка при получении информации по утечкам для {query}: {e}")
        return f"Ошибка при получении информации по утечкам: {e}"

def get_metadata(file_path: str) -> str:
    try:
        with exiftool.ExifTool() as et:
            metadata = et.get_metadata(file_path)
            metadata_str = json.dumps(metadata, indent=4, ensure_ascii=False)
            return f"Метаданные файла:\n{metadata_str}"
    except Exception as e:
        logging.error(f"Ошибка при получении метаданных для файла {file_path}: {e}")
        return f"Ошибка при получении метаданных: {e}"

def open_file_dialog() -> str:
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def stress_test(target: str, duration: int):
    start_time = time.time()
    packets_sent = 0
    try:
        while time.time() - start_time < duration:
            packet = IP(dst=target) / ICMP()
            send(packet, verbose=False)
            packets_sent += 1
        print(f"Stress Test завершился. Кол-во пакетов отправленных на сервер: {packets_sent}.")
    except Exception as e:
        print(f"Stress Test завершился падением сервера. Кол-во пакетов отправленных на сервер: {packets_sent}.\nОшибка: {e}")

def save_api_key(api_key: str):
    with open("key.txt", "w") as file:
        file.write(api_key)

def load_api_key() -> str:
    if os.path.exists("key.txt"):
        with open("key.txt", "r") as file:
            return file.read().strip()
    return ""

def advanced_search(api_key: str, search_type: str, query: str) -> str:
    try:
        url = 'https://leak-lookup.com/api/search'
        data = {'key': api_key, 'type': search_type, 'query': query}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            result = response.json()
            return json.dumps(result, indent=4, ensure_ascii=False)
        else:
            return f"Не удалось выполнить поиск. Статус-код: {response.status_code}"
    except Exception as e:
        logging.error(f"Ошибка при выполнении расширенного поиска для {query}: {e}")
        return f"Ошибка при выполнении расширенного поиска: {e}"

def display_menu():
    print("SIMP-OSI версия Alpha 1.1 last")
    print("1. Поиск информации по номеру телефона")
    print("2. Поиск информации по домену или IP-адресу")
    print("3. Поиск информации по MAC-адресу")
    print("4. Поиск по фото")
    print("5. Поиск по утечкам")
    print("6. Поиск метаданных")
    print("7. Стресс-тест")
    print("8. Расширенный поиск Private")
    print("99. Закрыть программу")

def main():
    while True:
        display_menu()
        option = input("Введите номер опции: ")
        if option == "1":
            phone_number = input("Введите номер телефона в международном формате (например, +79876543210): ")
            info = get_phone_info(phone_number)
            print(info)
        elif option == "2":
            query = input("Введите домен или IP-адрес: ")
            info = get_domain_ip_info(query)
            print(info)
        elif option == "3":
            mac = input("Введите MAC-адрес (например, 00:1A:2B:3C:4D:5E): ")
            info = get_mac_info(mac)
            print(info)
        elif option == "4":
            open_image_search()
        elif option == "5":
            query = input("Введите email, ник или пароль для поиска утечек: ")
            info = get_leak_info(query)
            print(info)
        elif option == "6":
            file_path = open_file_dialog()
            if file_path:
                info = get_metadata(file_path)
                print(info)
        elif option == "7":
            target = input("Введите URL или IP-адрес для стресс-теста: ")
            duration = int(input("Введите продолжительность тестирования в секундах: "))
            stress_test(target, duration)
        elif option == "8":
            api_key = load_api_key()
            if not api_key:
                api_key = input("Введите ваш API ключ: ")
                save_api_key(api_key)

            print("Что будем искать? Выберите тип информации по которой будет сделано сканирование:")
            search_types = {
                "1": "userid", "2": "uid", "3": "memberid", "4": "email_address", "5": "address",
                "6": "username", "7": "salt", "8": "password", "9": "firstname", "10": "lastname",
                "11": "fullname", "12": "number", "13": "country", "14": "city", "15": "zip",
                "16": "breachname", "17": "fb_id"
            }
            options = [
                "1.UserID", "2.UID", "3.Member ID", "4.Почта", "5.Адрес", "6.Никнейм", "7.Соль Хеша",
                "8.Пароль", "9.Имя", "10.Фамилия", "11.Полное имя", "12.Номер телефона", "13.Страна",
                "14.Город", "15.Zip код", "16.Имя утечки", "17.FacebookID"
            ]
            for option in options:
                print(option)

            search_option = input("Введите номер типа поиска: ")
            search_type = search_types.get(search_option)
            if search_type:
                query = input(f"Введите значение для {options[int(search_option) - 1].split('.')[1]}: ")
                info = advanced_search(api_key, search_type, query)
                print(info)
            else:
                print("Неверный номер типа поиска.")
        elif option == "99":
            print("Закрытие программы...")
            break
        input("Нажмите Enter, чтобы вернуться в главное меню...")

if __name__ == "__main__":
    main()
