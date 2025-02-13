import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import datetime
from tqdm import tqdm
from time import sleep
import random
import socks
import socket
from fake_useragent import UserAgent
import random

count = 0

ua = UserAgent()

def my_function():
    global count
    count += 1

def sendemail(senderemail, senderpassword, recipientemail, subject, messagetext):
    try:
        headers = {'User-Agent': ua.random}
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()

        server.login(senderemail, senderpassword)

        message = MIMEMultipart()
        message['From'] = senderemail
        message['To'] = recipientemail
        message['Subject'] = subject

        body = messagetext
        message.attach(MIMEText(body, 'plain'))

        server.send_message(message)
        now = datetime.datetime.now()
        print(now.strftime("%H:%M:%S"))
        my_function()
        print(f"Письмо от {senderemail} успешно отправлено на {recipientemail}\n Всего Отправлено", count, "сообщений")

        server.quit()
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")

senders = [ 
("baklakovarsenii93@rambler.ru", "JgsXE1QD"),
("garikpyatyjkin88@rambler.ru", "DvIn72F4y"),
("anatoliisavkin1994@rambler.ru", "JxL39BgBvRd"),
("barilkinasara@rambler.ru", "WDy2j4kRK"),
("dmitriifidelskii@rambler.ru", "cBBCMK06Q"),
("boryasigalin1998@rambler.ru", "4a5dVodAQ"),
("muravyhsvetlana@rambler.ru", "5WLEF0jltlJ"),
("ekaterinastruchkova1994@rambler.ru" "2zLvDlmHejS"),
("tarusovgleb1991@rambler.ru", "98vJ7a8Q"),
("kseniyateregulova@rambler.ru", "F1EWeAJDz"),
("jidenkovanina@rambler.ru", "hD8a9oRIGuK"),
("chichernikovaevgeniya@rambler.ru", "c2STlnHL"),
("dulimovkirill97@rambler.ru", "1NXtYjIXLS"),
("halilulinbogdan99@rambler.ru", "rPCLdMxTu9f"),
("aleksandramelichkina1993@rambler.ru", "Sj60kFtS"),
("lyubomirzyurnyaev1989@rambler.ru", "04nLMoKv5j"),
("arturfilchkov93@rambler.ru", "ZEa7UpylAOH"),
]

recipients = [
"support@telegram.org", 
"dmca@telegram.org", 
"security@telegram.org", 
"sms@telegram.org", 
"info@telegram.org", 
"marta@telegram.org", 
"spam@telegram.org", 
"alex@telegram.org", 
"abuse@telegram.org", 
"pavel@telegram.org", 
"durov@telegram.org", 
"elies@telegram.org", 
"ceo@telegram.org", 
"mr@telegram.org", 
"levlam@telegram.org", 
"perekopsky@telegram.org", 
"recover@telegram.org", 
"germany@telegram.org", 
"hyman@telegram.org", 
"qa@telegram.org", 
"Stickers@telegram.org", 
"ir@telegram.org", 
"vadim@telegram.org", 
"shyam@telegram.org", 
"stopca@telegram.org", 
"u003esupport@telegram.org", 
"ask@telegram.org", 
"125support@telegram.org", 
"me@telegram.org", 
"enquiries@telegram.org", 
"api_support@telegram.org", 
"marketing@telegram.org", 
"ca@telegram.org", 
"recovery@telegram.org", 
"http@telegram.org", 
"corp@telegram.org", 
"corona@telegram.org", 
"ton@telegram.org", 
"sticker@telegram.org",
]

messages = [ # можешь написать и больше сообщений по аналогии
    "Hello, I want to complain about the user (@vlow55), he uses a virtual number, threatens with deanonymization and false feminization, there are also violations in his channel https://t.me/vlow58"
    "hello, I want to complain about a user who clearly violates the telegram rules, his account @vlow55 - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual numberthere are also violations in his channel https://t.me/vlow58",
    "hello, I want to complain about a user who clearly violates the telegram rules, his account @vlow55 - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual number, there are also violations in his channel https://t.me/vlow58",
        "hello, @vlow55 - this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action! Please! He also has his channel in his bio where he posts it all (violations), and he use virtual number, https://t.me/vlow58",
            "hello,help me, I want to complain about a user who clearly violates the telegram rules, his account @vlow55 this user uses a virtual number, threatens with false feminization and deanonymization and throws elements of child abuse into chats, please take action!",
]

subjects = [ # можешь написать и больше тем по аналогии
    "Report for User",
    "Reporting",
    "Help pls",
    "Report User",
    "Report",
]

for senderemail, senderpassword in senders:
    for recipientemail in recipients:
        subject = random.choice(subjects)
        messagetext = random.choice(messages)
        sendemail(senderemail, senderpassword, recipientemail, subject, messagetext)
        time.sleep(30) # время задержки между сообщ в секундах