# СЛИЛ И КУПИЛ СКРИПТ: t.me/@gd23c
# СЛИЛ И КУПИЛ СКРИПТ: t.me/@gd23c
# СЛИЛ И КУПИЛ СКРИПТ: t.me/@gd23c
# СЛИЛ И КУПИЛ СКРИПТ: t.me/@gd23c
import requests
import time
import random
from fake_useragent import UserAgent
from datetime import datetime
import platform
import socket
import datetime
from termcolor import colored


device_name = socket.gethostname()
ip_address = socket.gethostbyname(device_name)
current_time = datetime.datetime.now()

print(colored(f"Скрипт был запущен: Устройство: {device_name}", 'red'))
print(colored(f"Точное время: {current_time}", 'cyan'))
print(colored(f"IP-адрес: {ip_address}", 'blue'))

url = 'https://telegram.org/support'
ua = UserAgent()

yukino = 0

def send_complaint(text, contact):
    headers = {
        'User-Agent': ua.random
    }
    payload = {
        'text': text,
        'contact': contact
    }
    
    proxies = {
    'http': '62.33.207.202:80',
    'http': '5.189.184.147:27191',
    'http': '50.221.74.130:80',
    'http': '172.67.43.209:80',
}
    
    response = requests.post(url, data=payload, headers=headers, proxies=proxies)
    
    if response.status_code == 200:
        print(f"\33[92mЖалоба успешно отправлена\n Всего отправлено", yukino, "сообщений\33[0m")
    else:
        print(colored(f"Произошла ошибка при отправке жалобы", 'red'))

text = [
    "Dear telegram support, I want to complain about the user @сюда юзерку (id сюда айди), the fact is that he deals with deanonymization of telegram users and personality and swatting, which violates the rules and breaks the TOS of telegram!I ask you to change this circumstance and behavior towards this user",
]

contact = [
    "+79967285422",
    "+79269736273",
    "+79963668355",
    "+79661214909",
    "79254106650",
    "+22666228126",
    "+79269069196",
    "+79315894431",
    "+79621570718",
]

while True:
    yukino += 1
    chosen_text = random.choice(text)
    chosen_contact = random.choice(contact)
    send_complaint(chosen_text, chosen_contact)
    time.sleep(0)
