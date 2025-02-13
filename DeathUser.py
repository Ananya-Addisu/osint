import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import shutil
import os
from colorama import Fore, Style, init
import random

init(autoreset=True)

senders = {
    'topzone6400@gmail.com': 'laum lkuc thvi lsol',
    'volkborz2022@gmail.com': 'cdzp ghoo xhaj gegd',
    'veterovseverov@gmail.com': 'jubm pkhe udpr gkze',
    'ghostchat2023@gmail.com': 'dezs aqvy mouq lfja',
    'hujnadadada@gmail.com': 'ydwe writ tlyf dxnl',
    'borzghost2024@gmail.com': 'tmnx xtka nsas soqb',
    'sanyaravanov@gmail.com ': 'xqvh vmmh omcy oata ',
    'leravladimir237@gmail.com': 'ndon fzio vskk bidt ',
    'vladimireputinka@gmail.com': ' npcs hurj xojs suey',
    'vladlord444@gmail.com': 'edsl kboc pgoc yzib ',
    '01020304pyu@gmail.com': 'ervb hrcn snvc lvrx '
}

receivers = [
    "sms@telegram.org", "dmca@telegram.org", "abuse@telegram.org", 
    "sticker@telegram.org", "support@telegram.org", "stopca@telegram.org", 
    "security@telegram.org"
]

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

def send_complaints(subject, body, count):
    for _ in range(count):
        receiver = random.choice(receivers)
        sender_email, sender_password = random.choice(list(senders.items()))
        if send_email(receiver, sender_email, sender_password, subject, body):
            print(f"{Fore.GREEN}Жалоба отправлена на {receiver} от {sender_email}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Не удалось отправить жалобу на {receiver} от {sender_email}{Style.RESET_ALL}")

def main():
    terminal_width = shutil.get_terminal_size().columns
    terminal_height = shutil.get_terminal_size().lines

    Banner1 = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢯⣿⣲⣄⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⣽⢟⣕⢄⠀⠀⠀⠀⠀⠀⣧⠀⡀⠀⠀⠀⠀⢠⢮⡾⣽⡻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣮⣟⡼⡌⡆⠀⠀⠀⠀⡰⡵⠰⡃⠀⠀⠀⢠⢃⡻⣜⢯⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣮⡵⣫⡵⢹⠀⠀⠀⠻⡄⡧⣈⠚⠀⠀⠀⢸⢺⡗⣭⣛⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡿⡵⢞⣫⡆⡹⠀⠀⠀⢑⠥⡨⡐⠫⣢⠀⠀⢸⢺⣽⢚⡭⣯⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣶⣻⡭⣷⢣⠇⠄⠤⢀⠼⣄⣸⡌⡆⢠⡧⠀⠈⡷⣮⢯⣛⣶⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀
⠀⠀⠈⠢⡀⠠⡒⠀⠂⠐⠀⠂⠀⣀⣴⢾⣿⣿⣿⣷⣚⣷⡿⣳⠛⠒⠒⠒⢇⠏⡚⠓⠈⢀⢬⠓⠒⠒⠚⢞⡯⣟⣶⣛⣿⣿⣿⣿⡦⣖⠀⠀⠀⠀⠂⠐⠀⡄⠀⠐⠁⠀⠀⠀
⠀⠀⠀⠀⠘⡄⠈⠢⡀⢀⣠⡴⣟⢿⣹⢿⣺⣿⣟⣶⣛⡭⠛⠁⠀⠀⠀⠀⠈⣑⣜⡆⢔⣕⣁⠀⠀⠀⠀⠀⠙⢯⡞⣛⣾⣿⣿⣸⣿⣹⣿⠶⣤⡀⠀⡠⠊⢀⠎⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣦⡴⣾⢯⡽⢾⡹⣾⣝⣾⣟⠫⠞⠋⡁⠤⠀⠒⠀⠉⠁⠀⠀⠀⢈⣷⣁⠀⠀⠀⠀⠉⠁⠐⠂⠤⢈⡙⠛⠯⣻⣾⣷⣏⢾⣻⢫⡽⣻⠶⣤⡂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣯⣷⣯⣻⣿⣧⣿⣟⡕⢋⢠⠐⠊⠁⠀⡀⣤⢀⣲⣦⣭⣥⣤⣴⣶⣤⣴⣦⣤⣬⣭⣥⣖⣂⣤⣄⡀⠀⠁⠂⡄⡉⢪⣟⣿⣵⣯⣾⣭⣟⣏⣿⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⢿⣿⣿⣿⣯⣿⣿⢳⣾⠇⠋⢀⢠⠰⠘⢃⣡⣾⣿⣿⢿⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣷⣮⣁⠃⠶⡄⡀⠁⠳⢹⣏⣿⣟⣿⣿⣾⣿⣿⣇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣟⢟⢿⣝⣟⣻⢻⢿⠁⢀⠜⠋⠀⠀⣠⣿⣿⠏⣿⣧⡇⣸⣿⣟⣯⡿⣽⣻⡿⣽⣿⣏⢈⣼⣿⡟⣧⣝⢧⡀⠀⠁⠃⡄⠀⡏⡿⣻⣻⣻⡽⣫⢻⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⢼⣱⢬⣙⡻⠭⣯⣦⣀⠑⠄⣀⣼⣿⣿⣮⠃⢿⣻⡿⣿⠟⣾⢷⣻⢯⣷⣟⣿⡻⣿⣿⣟⣿⠃⡾⣿⣷⡵⣄⢀⠔⢁⣠⣷⠿⢝⡚⡭⢮⣹⢿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⣾⣹⢾⡱⣺⠭⣽⣱⢞⡿⣩⢿⣟⣳⣿⢿⣿⣿⣿⡽⡍⢸⣟⣯⣟⣿⢾⡽⣾⡇⠙⣺⣽⣿⣷⣿⣿⣷⢻⣷⣭⢻⣗⢦⣻⡱⣽⢚⣟⣦⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡸⢿⣿⣟⣧⣷⣹⢥⠷⣞⣱⢏⡾⣱⣎⠧⣽⡱⠯⣟⢿⡡⠈⣿⣳⢿⡾⣿⡽⣷⠃⢄⡧⣟⡝⡧⢿⣲⣙⣧⢳⡞⣧⠺⡭⣖⢿⣸⣏⣷⣿⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⠜⠀⠠⠛⠿⣿⣿⣿⣿⣿⣵⣯⣾⢾⡳⣌⣿⢣⣝⣟⢣⠗⣝⢷⣿⣟⣯⣟⡷⣿⣿⡶⣫⣚⢖⡻⣵⣋⠷⣞⠼⣯⣳⣽⣯⣿⣿⣿⣿⣿⠿⠛⢅⠀⠑⡀⠀⠀⠀⠀
⠀⠀⢀⠎⠀⡰⠁⠀⠀⠀⠈⠉⠛⣿⣿⣿⣿⣷⣿⣋⣮⢷⡹⣌⣧⢿⢫⢵⣻⣟⣾⣽⣻⢷⡿⡽⣜⢻⢮⣕⢫⢷⣽⣎⣿⣿⣿⣿⣿⡿⡟⠉⠉⠀⠀⠀⠀⢢⠀⠘⠄⠀⠀⠀
⠀⢀⠊⠀⡐⠀⠀⢀⣀⠀⠀⠀⢸⣿⣾⣿⣿⣿⣿⣿⣾⡷⢻⡹⣜⣣⣿⢫⢧⣿⣟⣾⣽⣿⢻⣞⣧⣏⡳⢯⣛⢾⣶⣿⣿⣿⣿⣿⣿⡇⢻⠀⠀⠀⢀⣀⠀⠀⠡⠀⠈⡄⠀⠀
⠀⠌⠀⡰⠀⠀⠀⢸⣿⣷⣤⣀⠘⣿⣿⣿⣿⣿⣿⣽⣷⣿⣿⣿⣭⣷⣼⣟⣾⣻⣿⣯⢿⣏⣿⣿⣶⣾⣽⣻⣟⣿⣻⣿⣽⣿⣿⣿⣿⣇⡏⢀⣤⣴⡿⡝⠀⠀⠀⢣⠀⠘⡀⠀
⠐⠀⢠⠁⠀⠀⠀⠀⠙⣷⣿⣻⣷⣿⣿⣿⣻⣟⣿⣯⣿⣿⣽⣯⣟⣭⣷⣿⣾⡿⣯⣿⢿⣿⣷⣿⣿⣼⣹⣿⣻⣿⣿⣽⣿⢿⣻⣽⣿⣿⢳⣿⣟⣟⠟⠀⠀⠀⠀⠀⠆⠀⢡⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣟⣿⣽⣿⣯⣷⣿⡾⣿⣶⣯⣟⠿⣟⣿⣻⣽⢿⣽⣻⣿⣻⣾⣳⢯⣟⣿⣻⣿⣿⣟⣿⣭⣛⣿⣳⣯⣿⣏⣾⣟⣾⣿⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢿⣿⣿⣟⣿⢿⣯⣟⣷⣻⣾⣽⣻⣾⡿⣷⣿⣻⣾⢿⣷⣿⢿⣻⣿⣻⣿⢿⣻⣾⣽⣾⣽⣻⣽⡿⣿⢷⣽⣿⣿⣿⢹⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣟⣿⣿⣿⣯⣿⣟⣿⣿⣿⣷⣿⣻⣾⣽⢿⣽⣻⢾⡿⣯⢿⣻⣽⢯⡿⣽⡻⣫⣵⣾⣾⣿⣟⣿⣿⢿⡟⣾⣿⣟⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣻⣽⣿⣯⣟⣿⣿⣿⡿⠟⢻⠟⡿⣾⣭⣽⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠟⢛⠿⣿⣿⣿⣿⣿⢸⣿⡿⣿⡞⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⢿⣿⣟⣿⣿⣿⣿⠀⠀⢼⠠⠌⠘⣿⣿⣿⣿⡿⣿⣟⢿⣿⣿⣿⡋⠀⠄⡤⠄⠈⣿⣿⣿⣿⣼⢸⣿⣿⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣻⣿⣿⣿⣿⣶⣶⣶⣶⣿⣿⣿⣿⣿⢿⣻⣯⣸⣷⣿⣿⣿⣷⣶⣷⣶⣾⣿⣿⣿⣿⢿⣾⣿⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⣿⢷⣿⣿⣿⣯⡿⢷⣿⣿⣿⣿⣿⣻⣷⣿⣿⣿⣿⣞⣿⣻⣽⢿⣿⣿⣷⣿⣟⣫⣿⣿⣿⣿⣷⡌⣻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣯⣿⣳⣿⣽⣻⣿⣻⡽⣟⣾⣳⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⣻⢾⣻⣟⡿⣿⡯⢿⣾⣿⣵⣿⡣⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿⣯⣷⡿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣟⣯⣯⣴⣿⣿⣿⣿⣿⣿⣿⠎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀
⠀⠀⠈⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⣿⣿⣿⣿⣿⣿⣿⡾⣟⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠄⠀
⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠊⠠⠈⠈⣿⣷⣿⢻⣷⣿⣿⢿⣻⣿⡿⣿⣿⢿⣿⣻⣷⣿⡻⣿⡿⡏⣿⣷⣿⠃⠑⢄⠐⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⡰⠀⠀
⠀⠀⢢⠀⠘⡀⠀⠀⠀⠀⠀⠀⡠⠐⢀⠔⠁⠀⠀⢸⣿⣿⣼⠂⢻⠃⣿⢻⣷⣿⣿⣾⣿⡟⣿⡟⢿⠋⣿⠁⣸⣿⣿⣿⠀⠀⠀⠑⠄⠑⢄⠀⠀⠀⠀⠀⠀⢀⠎⠀⡰⠁⠀⠀
⠀⠀⠀⠡⡀⠈⢄⠀⢀⡠⠔⠊⠀⠀⠆⠀⠀⠀⠀⢸⣿⣿⣿⣷⣿⠀⣯⠀⡿⢹⠛⣿⠟⣷⣿⠃⣾⡄⠙⣶⣿⣿⣽⣿⠀⠀⠀⠀⠈⡄⠀⠈⠂⠄⣀⠀⢠⠊⠀⡐⠁⠀⠀⠀
⠀⠀⠀⠀⠑⡀⠀⠪⡉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠘⣿⣿⢿⣿⢧⡚⣿⣤⡇⡸⠀⢿⠀⢹⣿⣦⣿⡇⣿⣿⣿⣿⣾⠇⠀⠀⠀⡀⠈⠉⠉⠉⠉⠉⠉⡙⠁⢀⠜⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⢆⠀⠘⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⢿⣿⣿⣿⣿⣷⣦⣿⣤⣾⣿⣿⣿⣿⡿⡜⣿⣷⡟⠀⠀⣴⣿⣿⣿⣶⡄⠀⠀⣠⠞⠀⣠⠆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠳⡄⠈⠃⠀⠀⣤⣤⡄⢠⠀⢠⡄⢨⣿⡿⣿⣯⠹⠻⣿⣿⣿⣿⣿⣿⢿⡿⣿⡿⣿⣽⣾⣿⢻⢧⣤⣼⣿⣵⣦⢨⣿⣿⣤⠞⠁⠀⠞⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠐⢌⡉⠐⠢⡀⠀⠀⢰⠹⢿⣻⢿⣸⣄⢹⡻⢿⣿⣿⣿⡿⣿⣜⢿⣞⣿⣿⣳⠏⠉⠀⠀⠙⣿⠟⠀⣹⡇⡇⢀⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⡀⠈⠂⠄⡀⠑⠄⠘⠴⠉⣿⣟⣿⣧⣼⣧⣸⡆⣼⢀⣿⣿⣟⣧⡻⣿⣿⣷⣦⡰⠀⡠⠊⡠⡶⠈⣾⣿⠗⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠄⡀⠀⠁⠂⠆⠀⢌⠈⣿⣯⢿⡽⣯⣿⢿⡿⣾⣟⣿⣿⢿⣻⣮⣿⣾⡿⣦⣘⠂⠁⠀⣠⣾⡿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⢀⡀⠀⠀⠀⠀⠁⠂⡄⢀⡀⠀⠁⠐⠛⠻⢽⣳⣟⣯⣟⣷⣻⣾⣽⠿⢿⣿⣞⣯⢿⡿⣿⣻⣿⢿⣟⢿⡿⠁⣀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠈⡆⠀⠀⠀⢀⠎⢠⠂⠈⠑⡀⠠⡀⠤⠤⠀⠀⠀⠀⠀⠀⠀⠠⠤⠄⢘⠙⠻⠯⢿⣟⣷⣯⡿⠾⠋⢀⠊⠀⠀⠀⠈⢢⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠁⠀⢠⠊⠀⠈⠃⠀⠀⢀⠂⡠⠁⠀⠀⠀⠈⢄⠐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠁⡰⠁⠀⠀⠀⢢⠈⢄⠀⠀⠈⠊⠀⠁⠂⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⡄⠀⠘⢄⠀⠀⠀⢀⠠⠁⡐⠁⠀⠀⠀⠀⠀⠈⢂⠈⢄⠀⠀⠀⠀⠀⠀⠀⠀⡐⠁⠔⠀⠀⠀⠀⠀⠀⠡⡀⠢⡀⠀⠀⠀⢀⠄⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⢄⠀⠀⠉⠐⠂⠁⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠀⠢⠀⠀⠀⠀⠀⢀⠌⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠁⠒⠈⠀⠀⢀⠌⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠠⠄⠐⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠡⡀⠀⠀⢠⠊⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠒⠀⠄⠀⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠄⠐⠄⡠⠁⡠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠈⠀⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

[@MUPAHOB]
"""

    Banner2 = """
 .S_sSSs      sSSs   .S_SSSs    sdSS_SSSSSSbs   .S    S.    .S       S.     sSSs    sSSs   .S_sSSs    
.SS~YS%%b    d%%SP  .SS~SSSSS   YSSS~S%SSSSSP  .SS    SS.  .SS       SS.   d%%SP   d%%SP  .SS~YS%%b   
S%S   `S%b  d%S'    S%S   SSSS       S%S       S%S    S%S  S%S       S%S  d%S'    d%S'    S%S   `S%b  
S%S    S%S  S%S     S%S    S%S       S%S       S%S    S%S  S%S       S%S  S%|     S%S     S%S    S%S  
S%S    S&S  S&S     S%S SSSS%S       S&S       S%S SSSS%S  S&S       S&S  S&S     S&S     S%S    d*S  
S&S    S&S  S&S_Ss  S&S  SSS%S       S&S       S&S  SSS&S  S&S       S&S  Y&Ss    S&S_Ss  S&S   .S*S  
S&S    S&S  S&S~SP  S&S    S&S       S&S       S&S    S&S  S&S       S&S  `S&&S   S&S~SP  S&S_sdSSS   
S&S    S&S  S&S     S&S    S&S       S&S       S&S    S&S  S&S       S&S    `S*S  S&S     S&S~YSY%b   
S*S    d*S  S*b     S*S    S&S       S*S       S*S    S*S  S*b       d*S     l*S  S*b     S*S   `S%b  
S*S   .S*S  S*S.    S*S    S*S       S*S       S*S    S*S  S*S.     .S*S    .S*P  S*S.    S*S    S%S  
S*S_sdSSS    SSSbs  S*S    S*S       S*S       S*S    S*S   SSSbs_sdSSS   sSS*S    SSSbs  S*S    S&S  
SSS~YSSY      YSSP  SSS    S*S       S*S       SSS    S*S    YSSP~YSSY    YSS'      YSSP  S*S    SSS  
                           SP        SP               SP                                  SP          
                           Y         Y                Y                                   Y           
                                                                                                      
"""

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * (terminal_height // 2 - 3))
    for line in Banner1.split('\n'):
        print(Fore.RED + line.center(terminal_width))
    print("\n" * 2)
    print(f"{Fore.YELLOW}Нажмите Enter, чтобы продолжить...{Style.RESET_ALL}".center(terminal_width))
    input()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * (terminal_height // 2 - 25))
    for line in Banner2.split('\n'):
        print(Fore.BLUE + line.center(terminal_width))
    print("\n" * 2)

    subject = input("    Введите тему жалобы: ")
    body = input("    Введите текст жалобы: ")
    count = int(input("    Введите количество жалоб: "))

    send_complaints(subject, body, count)

    print(f"{Fore.YELLOW}Нажмите Enter для выхода...{Style.RESET_ALL}".center(terminal_width))
    input()

if __name__ == "__main__":
    main()