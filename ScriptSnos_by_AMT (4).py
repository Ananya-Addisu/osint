import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import random
import string

senders = {
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
 'lovedel.anisss@mail.ru': 'cJkiz18MAWS0L85DGW8n',
           'love.efs@mail.ru': 'vzw5bwePbzeXhYhDeeA1',
           'fsadfsaf.sdfasdfas@mail.ru': 'KUN0wpJbViwpFXFPkHb4',
           'fkjvfmdsof@mail.ru': 'CxM2JUT0vx03aSyD53Ns',
           'sawage.dasha@mail.ru': 'SyfStmkgK29KUB0BQVAy',
           'opunm.sdaww@mail.ru': 'Y1BjSZCHeLTxmvaW49FH',
           'fall.gall@mail.ru': 'tFqTgMUqkidcBbw91hD7',
           'wzxcvd@mail.ru': 'vwPUnRUGW75MUKaFzhVc',
           'masha.mashala@mail.ru': 'rtM0rCSHZstDVQpxmEkh',
           'wwagege@mail.ru': 'ZZNkRLrZseLN57phVeEQ',
           'irigjfodjdkdkk@mail.ru': 'n8r0TKCygC5xqaWxStr1',
           'sdfghafdhg@mail.ru': 'Kag0fefn6mFWMzQ17PGb',
           'dasha.goat@mail.ru': '3bkf9iHyuFUfEfKzXYLm',
           'dasha.sasaas@mail.ru': 'UAVwCgpFXaD2zcQ9gVSE',
           'dasha.lovely.02@mail.ru': 'paUrCHANKWWxefzaQvQm',
           'dasha.butifull@mail.ru': '0bAbKQUfpVRDcrLtc0Ya',
           'firirotifigj@gmail.com': 'RQCgW8vb127AGRZ5Kvf1',
           'dasha.mdaaa@gmail.com': 'HXNg0M0bvyaEs1tbMjTB',
           'lfwgdg@mail.ru': 'h6hAUvp3KNPqqcmmduU3',
           'dasha.holle@mail.ru': '0g5g6kwEtkKw2hYCaSTj',
           'darya.holly@mail.ru': 'he02duEXu4iiDambB6ZG',
           'dasha.vonk@mail.ru': 'AayKrKyfEDyeubmRqKRm',
           'kloxc@mail.ru': 'FVUeii2MdbNcqEmZr'
           
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']
             
def logo():
  """Печатает логотип при запуске."""
  print("  _____        _             _     _    ")
  print(" |_   _|      (_)           | |   | |   ")
  print("   | | ___  _ _ _ __   __ _| |__ | | __")
  print("   | |/ _ \| | | '_ \ / _` | '_ \| |/ /")
  print("   | | (_) | | | | | | (_| | | | |   < ")
  print("   |_|\___/|_|_|_| |_|\__,_|_| |_|_|\_\ ")
  print("      by @AlternativeHospital   ")
  """Пидор,хули разшифровал"""
  
def menu():
    print("\033[92mМеню:\033[0m")
    print("1.Account")
    print("2.Channel")
    print("3.Bots.")
    choice = input("Выбирай:  ")
    return choice
def send_email(receiver, sender_email, sender_password, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver, msg.as_string())
        time.sleep(3)
        server.quit()
        return True
    except Exception as e:
        return False

def main():
    sent_emails = 0
    logo()
    choice = menu()

    if choice == '1':
        print("1.Spam")
        print("2.Личная информация.")
        print("3.Буллинг")
        print("4.Сессия")
        print("5.Premium Account")
        print("6.Virt Account")
        comp_choice = input("Выбирай: ")

        if comp_choice in ["1", "2", "3"]:
            print("Следуй тому что тут написано и вставляй.")
            username = input("юзер: ")
            id = input("айди: ")
            chat_link = input("ссылку на чат/канал: ")
            violation_link = input("ссылку на нарушение: ")
            print("Погоди чу-чуть.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на чат - {chat_link}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(), chat_link=chat_link.strip(),
                                                 violation_link=violation_link.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)

        elif comp_choice == "4":
            print("Укажи всё что нужно ниже.")
            username = input("юзернейм: ")
            id = input("айди: ")
            print("Погоди чу-чуть.")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print("следуй указаниям и вводи что просят.")
            username = input("юзернейм: ")
            id = input("айди: ")
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)


    elif choice == "2":
        
        print("1.Личные данные")
        print("2.Жив0деры")
        print("3.Цп каналы")
        print("4.Прайс каналы.")
        ch_choice = input("выбор: ")

        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input("ссылка на канал: ")
            channel_violation = input("ссылка на нарушение (в канале): ")
            print("Погоди чу-чуть.")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал."
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)

    elif choice == "3":
        print("1.Порно боты")
        print("2.Посхалко.")
        bot_ch = input("Выбирай что то из этого: ")

        if bot_ch == "1":
            bot_user = input("юз бота: ")
            print("Погоди чу-чуть")
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который выдает цп/дп/18+. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота."
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(f"Отправлено на {receiver} от {sender_email}!")
                    sent_emails += 1
                    time.sleep(5)
        elif bot == "2":
            print("1488")
            
        
if __name__ == "__main__":
    main()