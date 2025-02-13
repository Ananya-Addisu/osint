import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Цвета для вывода в консоль
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Баннер
banner = f"""
{bcolors.FAIL}
========================================
         Mail Sender v1.0
========================================
{bcolors.ENDC}
"""

print(banner)

def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        print(f"{bcolors.FAIL}Ошибка при отправке письма: {e}{bcolors.ENDC}")
        return False

sender_email = input(f"{bcolors.OKBLUE}Введите ваш mail: {bcolors.ENDC}")
sender_password = input(f"{bcolors.OKBLUE}Введите ваш пароль приложения: {bcolors.ENDC}")
subject = input(f"{bcolors.OKBLUE}Введите тему письма: {bcolors.ENDC}")
body = input(f"{bcolors.OKBLUE}Введите текст письма: {bcolors.ENDC}")

receivers = [
    "sms@telegram.org", "dmca@telegram.org", "abuse@telegram.org", 
    "sticker@telegram.org", "support@telegram.org", "stopca@telegram.org", 
    "security@telegram.org"
]

for receiver in receivers:
    if send_email(receiver, sender_email, sender_password, subject, body):
        print(f"{bcolors.OKGREEN}Письмо успешно отправлено на {receiver}{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Не удалось отправить письмо на {receiver}{bcolors.ENDC}")

input(f"{bcolors.WARNING}Нажмите Enter для выхода...{bcolors.ENDC}")