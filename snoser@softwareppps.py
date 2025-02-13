import requests
from faker import Faker
from fake_useragent import UserAgent
from time import sleep
import colorama
from colorama import Fore, Style
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import os

colorama.init()

logging.basicConfig(filename='logging@softwareppps.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def display_ascii_art():
    print(Fore.RED + ascii_art + Style.RESET_ALL)

def check_password():
    display_ascii_art()
    print(Fore.RED + Style.BRIGHT + "Введите пароль для запуска скрипта: " + Style.RESET_ALL, end='')
    password = input()
    correct_password = '@softwareppps' 

    if password != correct_password:
        print(Fore.RED + "Неверный пароль!" + Style.RESET_ALL)
        return False
    return True

ascii_art = """
░█▀▀░█░█░▀█▀░█▀▀░█▀█░█▀▄░█▀▀░█▀▄░█▀▀      
░█░█░█░█░░█░░█▀▀░█░█░█▀▄░█▀▀░█▀▄░█░█      
░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░▀▀▀      
@softwareppps // @gutenbergebet
"""

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    if not check_password():
        return

    clear_console()
    display_ascii_art()

    fake = Faker()
    ua = UserAgent()

    proxies_list = [
        "http://username1:password1@proxy:port",
        "http://username2:password2@proxy:port",
    ]

    def generate_random_data():
        phone = '+7992' + ''.join(str(fake.random_number(digits=7, fix_len=True)))
        email = f"{fake.user_name()}@rambler.ru"
        return {
            "email": email,
            "phone": phone
        }

    def send_complaint(complaint_choice, repeats=200):
        url = 'https://telegram.org/support'
        complaints_sent = 0

        for _ in range(repeats):
            user_agent = ua.random
            headers = {'User-Agent': user_agent}
            random_data = generate_random_data()
            email = random_data["email"]
            phone = random_data["phone"]
            working_proxy = fake.random_element(elements=proxies_list)
            proxies = {
                "http": f"http://{working_proxy}",
                "https": f"https://{working_proxy}"
            }
            try:
                data = {
                    "email": email,
                    "phone": phone,
                    "message": complaint_choice
                }
                response = requests.post(url, data=data, headers=headers, proxies=proxies, timeout=10, verify=False)
                if response.status_code == 200:
                    complaints_sent += 1
            except requests.RequestException as e:
                logging.error(f"Ошибка запроса: {e}")
            sleep(2)
        
        return complaints_sent

    def send_email(sender_email, sender_password, recipient_emails, subject, body):
        sent_count = 0 #создатель скрипта @softwareppps/@gutenbergebet
        try:
            server = smtplib.SMTP('smtp-mail.outlook.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)

            for recipient_email in recipient_emails:
                try:
                    msg = MIMEMultipart()
                    msg['From'] = sender_email
                    msg['To'] = recipient_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(body, 'plain'))
                    server.sendmail(sender_email, recipient_email, msg.as_string())
                    sent_count += 1
                    print(Fore.GREEN + f"Жалоба отправлена на почту {recipient_email}" + Style.RESET_ALL)

                except Exception as e:
                    logging.error(f"Ошибка отправки письма: {e}")

        finally:
            server.quit()
        
        return sent_count

    print(Fore.RED + Style.BRIGHT + "Напишите тему письма:" + Style.RESET_ALL)
    subject = input()

    print(Fore.RED + Style.BRIGHT + "Напишите текст жалобы:" + Style.RESET_ALL)
    complaint_message = input()

    complaints_sent = send_complaint(complaint_choice=complaint_message)
    print(Fore.GREEN + Style.BRIGHT + f"Жалоба отправлена на сайт https://telegram.org/support" + Style.RESET_ALL)

    sender_emails = [
        ('your_outlook_email@outlook.com', 'your_outlook_password'),
        ('your_hotmail_email@hotmail.com', 'your_hotmail_password')
    ]
    recipient_emails = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org', 'sticker@telegram.org', 'support@telegram.org', 'me@telegram.rog', 'recover@telegram.org', 'info@telegram.org', 'marta@telegram.org', 'spam@telegram.org', 'alex@telegram.org', 'pavel@telegram.org', 'durov@telegram.org', 'elies@telegram.org', 'ceo@telegram.org', 'mr@telegram.org', 'levlam@telegram.org', 'perekopsky@telegram.org', 'germany@telegram.org', 'hyman@telegram.org', 'qa@telegram.org','ir@telegram.org', 'vadim@telegram.org', 'shyam@telegram.org', 'stopca@telegram.org', 'u003esupport@telegram.org', 'ask@telegram.org', '125support@telegram.org', 'me@telegram.org', 'enquiries@telegram.org', 'api_support@telegram.org', 'marketing@telegram.org', 'ca@telegram.org', 'recovery@telegram.org', 'http@telegram.org', 'corp@telegram.org', 'corona@telegram.org', 'ton@telegram.org', 'admin@telegram.org', 'telegram@telegram.org', 'official@telegram.org', 'durovpavel@telegram.org', 'russia@telegram.org', 'paveldurov@telegram.org', 'messenger@telegram.org', 'message@telegram.org', 'telegraph@telegram.org', 'durovs@telegram.org', 'org@telegram.org', 'authorized@telegram.org', 'helper@telegram.org', 'help@telegram.org', 'original@telegram.org', 'organization@telegram.org', 'administration@telegram.org'] * 50

    num_emails_to_send = 100
    sender_count = len(sender_emails)
    total_sent = 0

    for i in range(num_emails_to_send):
        sender_email, sender_password = sender_emails[i % sender_count]
        sent_count = send_email(sender_email, sender_password, recipient_emails, subject, complaint_message)
        total_sent += sent_count

    print(Fore.YELLOW + Style.BRIGHT + f"Отправлено {complaints_sent}/200 жалоб на сайт" + Style.RESET_ALL)
    print(Fore.YELLOW + Style.BRIGHT + f"Отправлено {total_sent}/100 писем через почту" + Style.RESET_ALL)

if __name__ == "__main__":
    main()