
from colorama import init, Fore, Style
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import platform
import os
os.system("pip install pystyle phonenumbers requests whois python-whois py-whois pywhois pythonwhois colorama")
import socket
import pystyle
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
import requests
import whois
import random
import colorama
import threading
import string
import faker
import bs4
import urllib.parse
import colorama
import concurrent.futures
import csv
if platform.system() == "Windows":
    import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)
    enter = pystyle.Colorate.Horizontal(pystyle.Colors.green_to_black, (""))
    pystyle.Anime.Fade(
    pystyle.Center.Center('''  


              ▄████████    ▄████████  ▄███████▄   ▄██████▄     ▄████████ 
             ███    ███   ███    ███ ██▀     ▄██ ███    ███   ███    ███ 
             ███    ███   ███    ███       ▄███▀ ███    ███   ███    ███ 
            ▄███▄▄▄▄██▀   ███    ███  ▀█▀▄███▀▄▄ ███    ███  ▄███▄▄▄▄██▀ 
          ▀▀███▀▀▀▀▀   ▀███████████   ▄███▀   ▀ ███    ███ ▀▀███▀▀▀▀▀   
           ▀███████████   ███    ███ ▄███▀       ███    ███ ▀███████████ 
             ███    ███   ███    ███ ███▄     ▄█ ███    ███   ███    ███ 
             ███    ███   ███    █▀   ▀████████▀  ▀██████▀    ███    ███ 
             ███    ███                                       ███    ███ 
                          
                            
                            Нажмите Enter'''), pystyle.Colors.purple_to_blue, pystyle.Colorate.Vertical, enter=True)
def Main():
    if platform.system() == "Windows":
        os.system("cls")
        pystyle.Write.Print(pystyle.Center.XCenter('''\n

 \n'''), pystyle.Colors.purple_to_blue, interval = 0.001)
    else:
        os.system("clear")
        pystyle.Write.Print(pystyle.Center.XCenter('''\n  
                    
 \n'''), pystyle.Colors.purple_to_red, interval = 0.001)
    pystyle.Write.Print(pystyle.Center.XCenter('''\n

                    ▄████████    ▄████████  ▄███████▄   ▄██████▄     ▄████████ 
                   ███    ███   ███    ███ ██▀     ▄██ ███    ███   ███    ███ 
                   ███    ███   ███    ███       ▄███▀ ███    ███   ███    ███ 
                  ▄███▄▄▄▄██▀   ███    ███  ▀█▀▄███▀▄▄ ███    ███  ▄███▄▄▄▄██▀ 
                 ▀▀███▀▀▀▀▀   ▀███████████   ▄███▀   ▀ ███    ███ ▀▀███▀▀▀▀▀   
                 ▀███████████   ███    ███ ▄███▀       ███    ███ ▀███████████ 
                   ███    ███   ███    ███ ███▄     ▄█ ███    ███   ███    ███ 
                   ███    ███   ███    █▀   ▀████████▀  ▀██████▀    ███    ███ 
                   ███    ███                                       ███    ███ 
                                          Канал - @ReaperSoft                                  
                                      ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
                                      ┃      [1] Информация о номере    ┃ 
                                      ┃      [2] Информация о сайте     ┃
                                      ┃      [3] Информация о нике      ┃
                                      ┃      [4] Информация об IP       ┃
                                      ┃      [5] Поиск по Базе Данных   ┃    
                                      ┃      [99] Выход                 ┃
                                      ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛          
'''), pystyle.Colors.purple_to_blue, interval = 0.001)
Main()
while True:
    select = pystyle.Write.Input("\n\n[?] Выберите пункт меню: ", pystyle.Colors.purple_to_blue, interval = 0.001)
    if select == "1":
        phone = pystyle.Write.Input("\n[?] Введите номер телефона -> ", pystyle.Colors.green, interval = 0.001)
        def phoneinfo(phone):
            try:
                parsed_phone = phonenumbers.parse(phone, None)
                if not phonenumbers.is_valid_number(parsed_phone):
                    return pystyle.Write.Print(f"\n[!] Произошла ошибка -> Недействительный номер телефона\n", pystyle.Colors.green, interval=0.005)
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
                pystyle.Write.Print(print_phone_info, pystyle.Colors.green, interval=0.005)
            except Exception as e:
                pystyle.Write.Print(f"\n[!] Произошла ошибка -> {str(e)}\n", pystyle.Colors.green, interval=0.005)
        phoneinfo(phone)
    if select == "2":
        domain = pystyle.Write.Input("\n[?] Введите сайт -> ", pystyle.Colors.green, interval = 0.005)
        def get_website_info(domain):
            domain_info = whois.whois(domain)
            print_string = f"""
[+] Домен: {domain_info.domain_name}
[+] Зарегистрирован: {domain_info.creation_date}
[+] Истекает: {domain_info.expiration_date}  
[+] Владелец: {domain_info.registrant_name}
[+] Организация: {domain_info.registrant_organization}
[+] Адрес: {domain_info.registrant_address}
[+] Город: {domain_info.registrant_city}
[+] Штат: {domain_info.registrant_state}
[+] Почтовый индекс: {domain_info.registrant_postal_code}
[+] Страна: {domain_info.registrant_country}
[+] IP-адрес: {domain_info.name_servers}
"""
            pystyle.Write.Print(print_string, pystyle.Colors.green, interval=0.005)
        get_website_info(domain)
    if select == "3":
        nick = pystyle.Write.Input(f"\n[?] Введите никнейм -> ", pystyle.Colors.green, interval=0.005)
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
                    pystyle.Write.Print(f"\n{url} - аккаунт найден", pystyle.Colors.green, interval=0.005)
                elif response.status_code == 404:
                    pystyle.Write.Print(f"\n{url} - аккаунт не найден", pystyle.Colors.green, interval=0.005)
                else:
                    pystyle.Write.Print(f"\n{url} - ошибка {response.status_code}", pystyle.Colors.green, interval=0.005)
            except:
                pystyle.Write.Print(f"\n{url} - ошибка при проверке", pystyle.Colors.green, interval=0.005)
        print()
    if select == "4":
        ip = pystyle.Write.Input("\n[?] Введите IP-адрес -> ", pystyle.Colors.green, interval = 0.005)
        def ip_lookup(ip):
            url = f"http://ip-api.com/json/{ip}"
            try:
                response = requests.get(url)
                data = response.json()
                if data.get("status") == "fail":
                    pystyle.Write.Print(f"[!] Произошла ошибка: {data['message']}\n", pystyle.Colors.green, interval=0.005)
                info = ""
                for key, value in data.items():
                    info += f"[+] {key}: {value}\n"
                return info
            except Exception as e:
                pystyle.Write.Print(f"[!] Произошла ошибка: {str(e)}\n", pystyle.Colors.green, interval=0.005)
        print()
        pystyle.Write.Print(ip_lookup(ip), pystyle.Colors.green, interval=0.005)
    if select == "5":
        path = pystyle.Write.Input("\n[?] Введите путь к БД: ", pystyle.Colors.green, interval=0.005)
        search_text = pystyle.Write.Input("\n[?] Введите текст:  ", pystyle.Colors.green, interval=0.005)
        print()
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    if search_text in line:
                        pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.green, interval=0.005)
                        print()
                        break
                else:
                    pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.green, interval=0.005)
        except:
            try:
                with open(path, "r", encoding="cp1251") as f:
                    for line in f:
                        if search_text in line:
                            pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.green, interval=0.005)
                            print()
                            break
                    else:
                        pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.green, interval=0.005)
            except:
                try:
                    with open(path, "r", encoding="cp1252") as f:
                        for line in f:
                            if search_text in line:
                                pystyle.Write.Print("[+] Результат: " + line.strip(), pystyle.Colors.green, interval=0.005)
                                print()
                                break
                        else:
                            pystyle.Write.Print("[!] Текст не найден.\n", pystyle.Colors.green, interval=0.005)
                except:
                    pystyle.Write.Print(f"[!] Произошла ошибка, проверьте ввод данных\n", pystyle.Colors.green, interval=0.005)
    if select == "99":
        sure = pystyle.Write.Input("Вы действительно хотите выйти? Y/N")
        if sure.lower() == "y" or sure.lower() == "yes" or sure.lower() == "н" or sure.lower() == "нуы" or sure.lower() == "да" or sure.lower() == "lf":
            exit()
        else:
            continue
    pystyle.Write.Input("\n[?] Нажмите Enter для продолжения", pystyle.Colors.green, interval = 0.005)
    Main()
    
    