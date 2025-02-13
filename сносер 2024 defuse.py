import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

# Список сгенерированных кодов доступа
access_codes = [
    'kryyaasoft', 'defuse'
]

# Отправители и их пароли
senders = {'lovedel.anisss@mail.ru': 'cJkiz18MAWS0L85DGW8n',
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
           'kloxc@mail.ru': 'FVUeii2MdbNcqEmZrq7N',
           'proto.dasha@mail.ru': 'LqJt4xXtqaAxUsd4D1HD',
           'dportq@mail.ru': 'CRUJZ7gi37VFn6a9mmYx',
           'dasha.port.06@mail.ru': 'Cnsy43cXqbAGVUswWdig',
           'portuyeye@mail.ru': 'y2jPgBkCxLuDBiHU2cAV',
           'dlegoyy@mail.ru': 'NtX9FmVJDi8fsBusv16Z',
           'portee05@mail.ru': '2eiDAier2n1MBrf1MZiX',
           'flipov.vlad@mail.ru': 'yePH6i1Sxw7XiYjR3E5K',
           'msolhov@mail.ru': 'RzQcdrRwYaJqycuxHzxM',
           'aslocv@mail.ru': 'i7n8zk8Dy0E9v7Sx2wLX',
           'kagbxz@mail.ru': 'vYkY8mrbqxGzpz8NqXe7',
           'mardjela@mail.ru': 'Cug2mXZ5d4c8aLNfnwCR',
           'egsdfdg@mail.ru': 'kCYudJg4P1KYF7iLkgcK',
           'ejofree@mail.ru': 'YKxiqwNwA87DEf8VftHF',
           'lina.fdfsfg@mail.ru': 'ts4JsHZhPf2vZ8rqxhmr',
           'abfdgs@mail.ru': 'vqdEDLtXpTU784KqLcvF',
           'pgkksdg@mail.ru': 'qfs6Nrg2zG2Zfudt8idz',
           'vadgadg@mail.ru': 'VkM3a1GpPaABr84PCztb',
           'jake.nod@mail.ru': '39uS26JTgKrBWJFdC16h',
           'noah.soli@mail.ru': 'xXvHn9usximafHmt4Rup',
           'jdlodd@mail.ru': 'rcAxee0FtnzL0wf4qUuX',
           'mmardjela@mail.ru': '3fhUwHBWipHasch29fv0',
           'andrea.aalto@mail.ru': 'XJrFhNwPamYaz6mjJ6yT',
           'luca.velde@mail.ru': 'cEeCv1mtP8Y2fsL4F1Xf',
           'esolhov@mail.ru': 'HB3zF1mz1H7EDEfinhdi',
           'fdfsfg04@mail.ru': 'hSrWxzjRWBLDYuPAB60F',
           'amardjela@mail.ru': 'rmyndAbyj7e5gjg3queN',
           'mrashni@mail.ru': 'Gukjw4sbwCrgAgFaZzx1',
           }

# Получатели
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']


def print_logo():
    print("░██                                ")
    print("░██        ██████  ██    ██  █████ ")
    print("░██       ██░░░░██░██   ░██ ██░░░██")
    print("░██      ░██   ░██░░██ ░██ ░███████")
    print("░██      ░██   ░██ ░░████  ░██░░░░ ")
    print("░████████░░██████   ░░██   ░░██████")
    print("░░░░░░░░  ░░░░░░     ░░     ░░░░░░ ")

    print(" ███████                ██               ██                     ")
    print("░██░░░░██              ░██              ░░                      ")
    print("░██    ░██    █████    ░██    ██████     ██   ███████     ██████")
    print("░██    ░██   ██░░░██   ░██   ░░░░░░██   ░██  ░░██░░░██   ██░░░░ ")
    print("░██    ░██  ░███████   ░██    ███████   ░██   ░██  ░██  ░░█████ ")
    print("░██    ██   ░██░░░░    ░██   ██░░░░██   ░██   ░██  ░██   ░░░░░██")
    print("░███████    ░░██████   ███  ░░████████  ░██   ███  ░██   ██████ ")
    print("░░░░░░░      ░░░░░░   ░░░    ░░░░░░░░   ░░   ░░░   ░░   ░░░░░░   ")


def print_menu():
    print("\033[92mCRACKED BY DEFUSE </>Меню:\033[0m")
    print("1. Снос аккаунта")
    print("2. Снос канала")
    print("3. Меню")
    print("4. Выход")


def send_email(receiver, sender_email, sender_password, subject, body):
    for sender_email, sender_password in senders.items():
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
            continue
    return False


def handle_complaint(senders, receivers):
    total_emails = len(senders) * len(receivers)
    sent_emails = 0

    while sent_emails < total_emails:
        print_logo()
        print_menu()
        choice = input("Выбор: ")

        if choice == "1":
            print("Выберите тип жалобы:")
            print("1.1 Обычный")
            print("1.2 Снос сессий")
            complaint_choice = input("Ваш выбор: ")
            
            if complaint_choice == "1.1":
                print("Введите причину, юзернейм, telegram ID, затем ссылки на канал/чат и на нарушение")
                reason = input("Причина: ")
                username = input("Юзернейм: ")
                telegram_ID = input("Telegram ID: ")
                chat_link = input("Ссылка на чат: ")
                violation_chat_link = input("Ссылка на нарушение: ")

                complaint_texts = {
                    "1.1": f"Здравствуйте, уважаемая поддержка, в вашей сети я нашел телеграм аккаунт, который нарушает ваши правила, такие как {reason}. Его юзернейм - {username}, так же его контактный ID - {telegram_ID}. Ссылка на чат с нарушениями - {chat_link}, ссылки на нарушения - {violation_chat_link}. Спасибо за помощь."
                }

                for sender_email, sender_password in senders.items():
                    for receiver_email in receivers:
                        complaint_text = complaint_texts[complaint_choice]
                        complaint_body = complaint_text.format(reason=reason.strip(), username=username.strip(), telegram_ID=telegram_ID.strip(), chat_link=chat_link.strip(), violation_chat_link=violation_chat_link.strip())
                        send_email(receiver_email, sender_email, sender_password, "Жалоба на Telegram аккаунт", complaint_body)
                        print(f"Отправлено на {receiver_email} от {sender_email}!")
                        sent_emails += 1

            elif complaint_choice == "1.2":
                print("Введите юзернейм и Telegram ID") 
                account_username = input("Юзернейм: ")
                Telegram_account_ID = input("Telegram ID: ")

                complaint_texts = {
                    "1.2": f"Здравствуйте, я утерял свой телеграм-аккаунт путем взлома. Я попался на фишинговую ссылку, и теперь на моем аккаунте сидит какой-то человек. Он установил облачный пароль, так что я не могу зайти в свой аккаунт и прошу о помощи. Мой юзернейм — {account_username}, а мой айди, если злоумышленник поменял юзернейм — {Telegram_account_ID}. Пожалуйста, перезагрузите сессии или удалите этот аккаунт, так как у меня там очень много важных данных."
                }

                for sender_email, sender_password in senders.items():
                    for receiver_email in receivers:
                        complaint_text = complaint_texts[complaint_choice]
                        complaint_body = complaint_text.format(account_username=account_username.strip(), Telegram_account_ID=Telegram_account_ID.strip())
                        send_email(receiver_email, sender_email, sender_password, "Я утерял свой телеграм-аккаунт", complaint_body)
                        print(f"Отправлено на {receiver_email} от {sender_email}!")

        elif choice == "2":
            print("Выберите тип жалобы:")
            print("8. Личные данные")
            print("9. Для прайсов")
            print("10. Для геймов")
            print("11. ЦП")
            print("12. Скам")
            print("13. Продажа вирт номеров")
            print("14. Расчлененка")
            print("15. Живодерство")
            complaint_type = input("Выбор: ")

            complaint_types = {
                "8": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются личные данные невинных людей. Ссылка на канал - {channel_link} . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support team! I have found a channel on your social network where personal data of innocent people is being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform"],
        "9": ["Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{violation_link} Просьба заблокировать данный канал.", "Hello, dear Telegram moderator,I would like to file a complaint regarding a channel on your platform that is selling doxxing and swatting services. Here are the details: Telegram channel link: {channel_link} Violation link: {violation_link} Please block this channel."],
        "10": ["Hello dear Telegram support! Please block the {channel_link} channel The channel threatens to shoot children in schools and commit terrorist attacks, you can see it here {violation_link} Thank you in advance", "Здравствуйте, уважаемая поддержка Telegram! Пожалуйста, заблокируйте канал {channel_link}. В этом канале угрожают расстрелом детей в школах и совершением террористических актов, вы можете увидеть это здесь {violation_link}. Заранее спасибо."],
        "11": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуется порнография с несовершеннолетними детьми. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support! In your social network, I found a channel posting pornography videos with children. Channel link - {channel_link} violation link - {violation_link} , please block this channel"],
        "12": ["Здравствуйте, поддержка Телеграм! В вашей социальной сети я нашел канал, в котором публикуются посты с целью обмана и мошенничества. Ссылка на канал - {channel_link}  . Ссылка на нарушение - {violation_link} . Просьба удалить данный канал с вашей площадки", "Hello, Telegram support! In your social network, I found a channel where posts aimed at deception and fraud are being published. The link to the channel is {channel_link}. The link to the violation is {violation_link}. Please remove this channel from your platform."],
        "13": ["Здравствуйте, поддержка telegram. Я бы хотел пожаловаться на телеграм канал продающий виртуальные номера, насколько я знаю это запрещено правилами вашей площадки. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link} . Спасибо что очищаете свою площадку от подобных каналов!", "Hello, Telegram support. I would like to report a Telegram channel selling virtual phone numbers, which as far as I know, is prohibited by your platform's rules. Here are the details:Channel link: {channel_link} Violation link: {violation_link} Thank you for cleansing your platform from such channels!"],
        "14": ["Доброго времени суток, уважаемая поддержка. На просторах вашей платформы мне попался канал, распространяющий шок контент с убийствами людей. Ссылка на канал - {channel_link} , ссылка на нарушение - {violation_link} . Просьба удалить данный канал, спасибо за внимание.", "Good day, esteemed support team. I came across a channel on your platform that disseminates shocking content involving human fatalities. Here is the link to the channel - {channel_link}, along withthe violation link - {violation_link}. Kindly remove this channel. Thank you for your attention."],
        "15": ["Здравствуйте, уважаемая поддержка. На вашей платформе я нашел канал который выкладывает жестокое обращение с животными. Ссылка на канал - {channel_link} ссылка на нарушение - {violation_link}. Спасибо за то что делаете телеграм чище.", "Hello, dear support. I found a channel postingcruelty to animals. Channel link - {channel_link} , violation links - {violation_link} Thank you"],

            }

            if complaint_type not in complaint_types:
                print("Некорректный выбор.")
            else:
                complaint_texts = complaint_types[complaint_type]
                channel_link = input("Ссылка на канал: ")
                violation_link = input("Ссылка на нарушение: ")

                for sender_email, sender_password in senders.items():
                    for receiver_email in random.sample(receivers, min(2, len(receivers))):
                        complaint_body = complaint_texts[0].format(channel_link=channel_link.strip(), violation_link=violation_link.strip())
                        send_email(receiver_email, sender_email, sender_password, "Жалоба на канал в Telegram", complaint_body)
                        print(f"Отправлено на {receiver_email}!")
                        sent_emails += 1
                # Отправка писем на английском
                if len(complaint_texts) > 1:
                    for sender_email, sender_password in senders.items():
                        for receiver_email in random.sample(receivers, min(2, len(receivers))):
                            complaint_body = complaint_texts[1].format(channel_link=channel_link.strip(), violation_link=violation_link.strip())
                            send_email(receiver_email, sender_email, sender_password, "Complaint about a channel in Telegram", complaint_body)
                            print(f"Sent to {receiver_email}!")
                            sent_emails += 1
                print("Отправлено!")

        elif choice == "5":
            print("Укажите свою почту для проверки работоспособности почт")
            test_email = input("Ваша почта: ")
            complaint_types = {
                "Тест": ["Сейчас я отправлю на почту {test_email} письма с моих почт в качестве теста"]
            }
            successfully_sent_emails = 0  # Переменная для отслеживания успешно отправленных писем
            for sender_email, sender_password in senders.items():
                for receiver_email in receivers:
                    for complaint_choice, complaint_texts in complaint_types.items():
                        complaint_text = complaint_texts[0]
                        complaint_body = complaint_text.format(test_email=test_email.strip())
                        if send_email(receiver_email, sender_email, sender_password, "ТЕСТОВОЕ ПИСЬМО LOVE DELAINS", complaint_body):
                            successfully_sent_emails += 1
                            print(f"Отправлено на {receiver_email} от {sender_email}!")
                        else:
                            print(f"Ошибка при отправке на {receiver_email} от {sender_email}!")
            print(f"Успешно отправлено {successfully_sent_emails} писем.")

def check_access_code():
    user_input = input("Введите код доступа: ")
    if user_input in access_codes:
        print("Код доступа верный. Программа запущена.")
        return True
    else:
        print("Неверный код доступа. Программа завершает работу.")
        return False


if __name__ == "__main__":
    if check_access_code():
        handle_complaint(senders, receivers)
