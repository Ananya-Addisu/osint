import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import colorama
from colorama import Fore, Style
import sys
import os
from fake_useragent import UserAgent
import requests
import random
import string

colorama.init()

# ASCII арт
ascii_art = """
░█▀▀░█░█░▀█▀░█▀▀░█▀█░█▀▄░█▀▀░█▀▄░█▀▀           
░█░█░█░█░░█░░█▀▀░█░█░█▀▄░█▀▀░█▀▄░█░█           
░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀           
@softwareppps // @gutenbergebet
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_password():
    clear_console()
    print(Fore.RED + ascii_art + Style.RESET_ALL)
    password = input(Fore.RED + Style.BRIGHT + "[×] Введите пароль: " + Style.RESET_ALL)
    
    if password != "@softwareppps":
        print(Fore.RED + Style.BRIGHT + "Неверный пароль!" + Style.RESET_ALL)
        sys.exit()
    
    clear_console()
    print(Fore.RED + ascii_art + Style.RESET_ALL)

def email_campaign():
    senders = {
        'carol_hxdjosp5@outlook.com': 'fCd7GPo5rZ4O',
        'mary_obevhiy6@outlook.com': 'cyoI#XUz2G',
        'patricia_zonqvyl5@outlook.com': 'IFjj0^fOrd',
        'michelle_nkirlnt7@outlook.com': 'mW1IZPu5tZz',
        'sandra_knjkxdi5@outlook.com': 'Ql1brxa2rhKDz',
        'linda_eknkohg7@outlook.com': 'JFZHuMMTQSbB',
        'deborah_ybjuwlz6@outlook.com': 'xrMr3FFciGeVo',
        'betty_gztwmsl5@outlook.com': 'mF0I#VU4Smh^8s',
        'ruth_bdalnvv7@outlook.com': 'xUSthIFMRxT',
        'kimberly_merpkra5@outlook.com': 'ssCbOpfXXd6OIvg',
        'karen_kgihdhk6@outlook.com': 'ITeTz^7yiYsu^Ru',
        'patricia_teitkyk6@outlook.com': 'nItrRO3T2ZuuHxV',
        'betty_dweenam6@outlook.com': 'Hr5Bt95xov3HiH7x',
        'helen_oswmpwn6@outlook.com': 'AT%pYVRa7pppslA',
        'tao_222222@hotmail.com': 'Charuwan0805612290',
        'elopezmor@outlook.com': 'Lalo2311',
        'huissenoliveira@hotmail.com': '8Pedaladas!',
        'ankitsinghbisen@outlook.com': 'Ujjain@123',
        'raulyon10@hotmail.com': 'Sniper10.',
        'djleozinhodf@hotmail.com': '83245652leo',
        'Ignaciomalig@outlook.com': 'Nachom12340',
        'osmair_123@hotmail.com': 'Ods*100487',
        'turgutuzala@hotmail.com': 'Turgut112799',
        'franma033@hotmail.com': 'Fmessi13##',
        'zipsgolddutch99@hotmail.com': 'Jjandsi99!!',
        'yare.verduzco@hotmail.com': 'Iloveyou2125$$$',
        'tedlin71@hotmail.com': 'Sm70000885!',
        'malu.maximo@hotmail.com': 'Cinderela',
        'cruni2011@hotmail.com': 'rendon711',
        'jaimeteesasi@hotmail.com': 'Jimi8039',
        'vellasophie@hotmail.fr': 'Pitou!1963',
        'owen9888@hotmail.com': 'owen11888'
    }

    recipients = [
        'dmca@telegram.org',
        'security@telegram.org',
        'sms@telegram.org',
        'abuse@telegram.org',
        'sticker@telegram.org',
        'stopCA@telegram.org',
        'recover@telegram.org',
        'support@telegram.org'
    ]

    smtp_server = 'smtp.outlook.com'
    smtp_port = 587
    interval = 2

    def calculate_total_time(senders, recipients, interval):
        total_emails = len(senders) * len(recipients)
        total_time_seconds = total_emails * interval
        return total_emails, total_time_seconds

    total_emails, total_time_seconds = calculate_total_time(senders, recipients, interval)
    print(Fore.RED + Style.BRIGHT + f'[×] Для отправки всех писем потребуется {total_time_seconds} секунд.' + Style.RESET_ALL)

    print() 

    while True:
        subject = input(Fore.RED + Style.BRIGHT + """[×] Введите тему письма: """ + Style.RESET_ALL)
        body = input(Fore.RED + Style.BRIGHT + """[×] Введите текст письма: """ + Style.RESET_ALL)
        
        print()

        if subject and body:
            break
        else:
            print(Fore.RED + "Введите корректную тему и текст письма!" + Style.RESET_ALL)
            print()

    for sender_email, sender_password in senders.items():
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  
                server.login(sender_email, sender_password)  

                for recipient_email in recipients:
                    try:
                        msg = MIMEMultipart()
                        msg['From'] = sender_email
                        msg['To'] = recipient_email
                        msg['Subject'] = subject

                        msg.attach(MIMEText(body, 'plain'))
                        
                        server.send_message(msg)
                        print(Fore.GREEN + f'Письмо отправлено {recipient_email} от {sender_email}' + Style.RESET_ALL)
                        
                        time.sleep(interval) 

                    except Exception:
                        break

        except Exception:
            continue

def generate_phone_number():
    country_codes = ['+7', '+380', '+375']
    country_code = random.choice(country_codes)
    phone_number = ''.join(random.choices('0123456789', k=10))
    formatted_phone_number = f'{country_code}{phone_number}'
    return formatted_phone_number

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "mail.ru"]
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))  
    domain = random.choice(domains)  
    email = f"{username}@{domain}"  
    return email

def send_complaint(number, email, text, proxies=None):
    url = 'https://telegram.org/support'
    user_agent = UserAgent().random
    headers = {'User-Agent': user_agent}
    payload = {'text': text, 'number': number, 'email': email}

    try:
        response = requests.post(url, headers=headers, data=payload, proxies=proxies)
        if response.status_code == 200:
            print(Fore.GREEN + f"Жалоба успешно отправлена | {email} | {number}" + Style.RESET_ALL)
        else:
            print("Не удалось отправить. code:", response.status_code)
    except Exception:
        pass  # Создатель @softwareppps

def complaint():
    while True:
        print()
        text = input(Fore.RED + Style.BRIGHT + """[×] Введите текст жалобы: """ + Style.RESET_ALL)
        
        print()
        
        if not text:
            print(Fore.RED + "Введите корректный текст жалобы!" + Style.RESET_ALL)
        else:
            break 

    proxies_list = [
        '20.111.54.16:8123',
        '35.185.196.38:3128',
        '20.206.106.192:8123',
        '160.86.242.23:8080',
        '20.24.43.214:80',
        '20.204.212.76:3129',
        '54.179.44.51:3128',
        '189.240.60.169:9090',
        '189.240.60.163:9090',
        '20.204.212.45:3129',
        '189.240.60.166:9090',
        '20.44.188.17:3129',
        '20.219.176.57:3129',
        '182.253.109.27:8080',
        '189.240.60.164:9090',
        '181.188.27.162:8080',
        '20.210.113.32:8123',
        '148.72.140.24:30127',
        '189.240.60.168:9090',
        '20.204.214.79:3129',
        '159.65.0.8:3128',
        '47.88.31.196:8080',
        '189.240.60.171:9090',
        '138.197.148.215:80',
        '175.139.233.76:80',
        '47.88.31.196:8080',
        '192.73.244.36:80',
        '82.67.23.158:80',
        '138.68.235.51:80',
        '41.173.24.38:80',
        '189.240.60.166:9090',
        '219.65.73.81:80',
        '160.86.242.23:8080',
        '181.41.194.186:80',
        '212.107.28.120:80',
        '46.47.197.210:3128',
        '23.247.136.245:80',
        '52.221.217.108:8080',
        '47.252.29.28:11222',
        '205.185.125.235:3128',
        '49.245.96.145:80',
        '182.253.109.27:8080',
        '5.161.103.41:88',
        '189.240.60.163:9090',
        '51.89.255.67:80',
        '20.204.212.45:3129',
        '116.125.141.115:80',
        '47.242.47.64:8888',
        '47.56.110.204:8989',
        '47.74.152.29:8888',
        '154.203.132.49:8080',
        '189.240.60.164:9090',
        '195.114.209.50:80',
        '159.65.244.233:80',
        '85.214.107.177:80',
        '20.204.212.76:3129',
        '116.203.28.43:80',
        '133.18.234.13:80',
        '189.240.60.169:9090',
        '144.126.216.57:80',
        '74.48.78.52:80',
        '35.185.196.38:3128'
    ]

    for _ in range(50): 
        number = generate_phone_number()
        email = generate_random_email()
        proxies = {'http': random.choice(proxies_list)}
        send_complaint(number, email, text, proxies)

def website_campaign():
    complaint()

def main():
    check_password()

    while True:
        clear_console()
       
        print(Fore.RED + ascii_art + Style.RESET_ALL) 
     
        print(Fore.RED + Style.BRIGHT + "[1] Снос через почты" + Style.RESET_ALL)
        print(Fore.RED + Style.BRIGHT + "[2] Снос через сайт" + Style.RESET_ALL)
        
        print()
        choice = input(Fore.RED + Style.BRIGHT + "Select an option -> " + Style.RESET_ALL).strip()

        if choice == "1":
            email_campaign()
            break 
            
        elif choice == "2":
            website_campaign()
            break 
            
        else:
            print()
            print(Fore.RED + "Некорректный выбор! Попробуйте снова." + Style.RESET_ALL)
            print()

if __name__ == "__main__":
    main()