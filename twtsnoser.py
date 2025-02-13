import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import pyfiglet
from termcolor import colored 
a=input(colored(f"Введите код:", 'red'))
if a!="TalisovSolo":
	print(colored(f"Пароль не правильный! Завершение работы программы! ", 'red'))
	print(colored(f"Уточни его у владельцев програмы", 'red'))
	exit()
else:
	print(colored(f"Пароль верный! Запускаю  программу!", 'red'))


ascii_banner = pyfiglet.figlet_format("TWT SNOSER")
colored_banner = colored(ascii_banner, color='red') 
print(colored_banner)
   
senders = {
    'korlithiobtennick@mail.ru': 'feDLSiueGT89APb81v74',
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
'colbycolb@cox.net': 'Signals@1',
'nicrey4@comcast.net': 'Dabears54',
'mordechai@mail.com': 'Mordechai',
'inemrzoya@mail.com': 'rLS1elaUrLS1elaU',
'tarabedford@comcast.net': 'Money4me',
'mycockneedsit@mail.com': 'benjamin3',
'saralaine@mail.com': 'sarlaine12!1',
'jonb2006@verizon.net': '1969Camaro',
'rjhssa1@verizon.net': 'Donna613*',
'cameron.doug@charter.net': 'Jake2122$',
'bridget.shappell@comcast.net': 'Brennan1',
'rugs8@comcast.net': 'baseball46',
'averyjacobs3@mail.com': '1960682644!',
'lstefanick@hotmail.com': 'Luv2dance2',
'bchavez123@mail.com': 'aadrianachavez',
'lukejamesjones@mail.com': 'tinkerbell1',
'emahoney123@comcast.net': 'Shieknmme3#',
'mandy10.mcevoy@btinternet.com': 'Tr1plets3',
'jet747@cox.net': 'Sadie@1234',
'landsgascareservices@mail.com': 'Alisha25@',
'samantha224@mail.com': 'Madden098!@',
'kbhamil@wowway.com': 'Carol1940',
'email@bjasper.com': 'Lhsnh4us123!',
'biggsbrian@cox.net': 'Trains@2247Trains@2247',
'dzzeblnd@aol.com': 'Geosgal@1',
'jtrego@indy.rr.com': 'Jackwill14!',
'chrisphonte.rj@comcast.net': 'Junior@3311',
'tvwifiguy@comcast.net': 'Bill#0101',
'defenestrador@mail.com': 'm0rb1d8ss',
'glangley@gmx.com': 'ironhide',
'charlotte2850@hotmail.com': 'kelalu2850',
}
receivers = ['sms@telegram.org', 'dmca@telegram.org', 'abuse@telegram.org', 'sticker@telegram.org', 'support@telegram.org', 'recover@telegram.org']


def menu():
    print(colored(f"Меню: ", 'red'))
    print(colored("1. Снос аккаунтов ",'red'),colored("[work]", "green"))
    print(colored("2. Снос каналов ", 'red'),colored("[work]", "green"))
    print(colored("3. Снос групп ", 'red'),colored("[work]", "green"))
    print(colored("4. Снос ботов", "red"), colored("[work]", "green"))
    print(colored("5. Снос сессий ", 'red'),colored("[work]", "green"))
    print(colored("6. Разбан аккаунта ", 'red'),colored("[work]", "green"))
    print(colored("7. Создатели софта", 'red'), colored("[2 человека]", "green"))
    
    choice = input(colored("Введите номер:",'red'))                              
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
        print(colored(f"1. Спам", 'red'),colored("[work]", "green"))
        print(colored(f"2. Личные данные (докс)", 'red'),colored("[work]", "green"))
        print(colored(f"3. Троллинг", 'red'),colored("[work]", "green"))
        print(colored(f"4. Взломаный акк", 'red'),colored("[work]", "green"))
        print(colored(f"5. Виртуальный номер", 'red'),colored("[work]", "green"))
        print(colored(f"6. Премиум", 'red'),colored("[work]", "green"))
        print(colored(f"7. Сватинг (сват)", 'red'),colored("[work]", "green"))
        print(colored(f"8. Неуместный контент ", 'red'),colored("[work]", "green"))
        print(colored(f"9. Мошеничество (скам)", 'red'),colored("[work]", "green"))
        print(colored(f"10. Без причины", 'red'),colored("[work]", "green"))
        comp_choice = input(colored(f"Выберите способ:",'red'))
        if comp_choice in ["1", "2", "3"]:
            username = input(colored(f"@username:",'red'))
            id = input(colored(f"Telegram ID:",'red'))
            violation_link = input(colored(f"Ссылка на нарушение:",'red'))
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка. На вашей платформе я нашел пользователя который отправляет много ненужных сообщений - СПАМ. Его юзернейм - {username}, его айди - {id}, ссылка на нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю.",
                "2": f"Здравствуйте, уважаемая поддержка, на вашей платформе я нашел пользователя, который распространяет чужие данные без их согласия.Тоесть занимается доксом. Его юзернейм - {username}, его айди - {id}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта.",
                "3": f"Здравствуйте, уважаемая поддержка телеграм. Я нашел пользователя который открыто выражается нецензурной лексикой и спамит в чатах. его юзернейм - {username}, его айди - {id}, ссылка на нарушение/нарушения - {violation_link}. Пожалуйста примите меры по отношению к данному пользователю путем блокировки его акккаунта."
            }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip(),                                 violation_link=violation_link.strip())
                    
                    send_email(receiver, sender_email, sender_password, 'Жалоба на аккаунт телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 9999
                    time.sleep(5)
        
        elif comp_choice == "4":
            username = input(colored(f"@username:",'red'))
            id = input(colored(f"Telegram ID:",'red'))
            comp_texts = {
                "4": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 9999
                    time.sleep(5)

        elif comp_choice in ["5", "6"]:
            username = input(colored(f"@username:",'red'))
            id = input(colored(f"Telegram ID:",'red'))
            comp_texts = {
                "5": f"Добрый день поддержка Telegram!Аккаунт {username} , {id} использует виртуальный номер купленный на сайте по активации номеров. Отношения к номеру он не имеет, номер никак к нему не относиться.Прошу разберитесь с этим. Заранее спасибо!",
                "6": f"Добрый день поддержка Telegram! Аккаунт {username} {id} приобрёл премиум в вашем мессенджере чтобы рассылать спам-сообщения и обходить ограничения Telegram.Прошу проверить данную жалобу и принять меры!"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 9999
                    time.sleep(5)
                   
        elif comp_choice in ["7", "8"]:
            username = input(colored(f"@username:",'red'))
            id = input(colored(f"Telegram ID:",'red'))
            comp_texts = {
                "7": f"Добрый день поддержка Telegram аккаунт {username} , {id} продает услуги деанонизации личности, докса и сваттинга , свата , угрожает минированием зданий. Прошу Вас заблокировать данный аккаунт, за нарушение правил!",
                "8": f"Добрый день поддержка Telegram! Пользователь: {username} {id} распрастраняет неуместный контент, расправы и контект порнографического характера. Прошу вас заблокировать данный телеграм аккаунт за нарушение правил!"
             }
             
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 9999
                    time.sleep(5)
                
        elif comp_choice == "10":
            username = input(colored(f"@username:",'red'))
            id = input(colored(f"Telegram ID:",'red'))
            comp_texts = {
                "10": f"Здравствуйте, уважаемая поддержка Telegram акаунт: {username} / {id} нарушает правила площадки Telegram. Прошу вас заблокировать данный аккаунт"
            }
            
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[comp_choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на пользователя телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 9999
                    time.sleep(5)


    elif choice == "2":            
        print(colored(f"1. Личные данные (докс)", 'red'),colored("[work]", "green"))
        print(colored(f"2. Живодерство", 'red'),colored("[work]", "green"))
        print(colored(f"3. ЦП", 'red'),colored("[work]", "green"))
        print(colored(f"4. Прайс", 'red'),colored("[work]", "green"))
        print(colored(f"5. Сватинг (сват)", 'red'),colored("[work]", "green"))
        print(colored(f"6. Порно", 'red'),colored("[work]", "green"))
        print(colored(f"7. Мошеничество (скам)", 'red'),colored("[work]", "green"))
        print(colored(f"8. Наркотики", 'red'),colored("[work]", "green"))
        print(colored(f"9. Расчленëнка", 'red'),colored("[work]", "green"))
        print(colored(f"10. Накрутка", 'red'),colored("[work]", "green"))
        ch_choice = input(colored(f"Выберите способ:", 'red'))
        if ch_choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            channel_link = input(colored(f"Ссылка на канал:",'red'))
            channel_violation = input(colored(f"Ссылка на нарушение:",'red'))
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет личные данные невинных людей. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет жестокое обращение с животными. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел канал который распространяет порнографию с участием несовершеннолетних. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "4": f"Здравствуйте,уважаемый модератор телеграмм,хочу пожаловаться вам на канал,который продает услуги доксинга, сваттинга. Ссылка на телеграмм канал:{channel_link} Ссылка на нарушение:{channel_violation} Просьба заблокировать данный канал.",
                "5": f"Здравствуйте, уважаемая поддержка Telegram. Я бы хотел вам сообщить о канале, нарушающем правила площадки. Канал:{channel_link} .Нарушения: Данные администраторы канала занимаються Сватингом людей в Интернете, лжеменированием зданий. Ниже прикрепляю доказательства: {channel_violation}",
                 "6": f"Здравствуйте, уважаемая поддержка Telegram. Я бы хотел вам сообщить о канале, нарушающем правила площадки. Ссылка на канал - {channel_link} .Нарушения: Порнография, контент 18+Ниже прикрепляю доказательства: {channel_violation}",
                  "7": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет мошеничество (скам) и обманывает своих покупателей на деньги. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                  "8": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел канал, который распространяет тематику Наркотиков и ищит рабочих на должность закладчика. Ссылка на канал - {channel_link}, сслыки на нарушения - {channel_violation}. Пожалуйста заблокируйте данный канал.",
                "9": f"Здравствуйте, уважаемая поддержка Telegram. Я бы хотел вам сообщить о канале, нарушающем правила площадки Telegram. Канал - {channel_link} .Нарушения: Рапсправы, Расчленëнка. Ниже прикрепляю доказательства: {channel_violation}",
                "10": f"Здравствуйте, уважаемая поддержка Telegram. Я бы хотел вам сообщить о канале, нарушающем правила площадки. Тег канала: {channel_link} .Нарушения: Владелец канала сделал себе не настоящих подпичиков, что называется накруткой людей. Ниже прикрепляю доказательства: {channel_violation}",
                 }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[ch_choice]
                    comp_body = comp_text.format(channel_link=channel_link.strip(), channel_violation=channel_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм канал', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 100000
                    time.sleep(5)

    elif choice == "7":
        print(colored(f"Владельцем софта является @TALISOV_ONE, софт писал @A1eksandrSaD0w",'red'))
        

    elif choice == "4":
        print(colored(f"1. Докс бот",'red'),colored("[work]", "green"))
        print(colored(f"2. Сват бот",'red'),colored("[work]", "green"))
        print(colored(f"3. Порно бот",'red'),colored("[work]", "green"))
        print(colored(f"4. Скам бот",'red'),colored("[work]", "green"))
        print(colored(f"5. Незаконный бот",'red'),colored("[work]", "green"))
        bot_ch = input(colored(f"Выберите способ:",'red'))

        if bot_ch in ["1", "2", "3", "4", "5"]:
            bot_user = input(colored(f"@username:",'red'))
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет поиск по личным данным ваших пользователей. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                 "2": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет лжеменирования (сват) и минирование зданий. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                  "3": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который использует материалы 18+ контента, порнографического характера. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                   "4": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который осуществляет обман , скам своих пользователей на деньги. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                   "5": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел бота, который является незаконным и этот бот нарушает законы. Ссылка на бота - {bot_user}. Пожалуйста разберитесь и заблокируйте данного бота.",
                       }
            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[bot_ch]
                    comp_body = comp_text.format(bot_user=bot_user.strip())
                    send_email(receiver, sender_email, sender_password, 'Жалоба на бота телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 1
                    time.sleep(5)
                  
    elif choice == '3':
        print(colored(f"1. Докс", 'red'),colored("[work]", "green"))
        print(colored(f"2. Сливы 18+", 'red'),colored("[work]", "green"))
        print(colored(f"3. Слив расчленëнки", 'red'),colored("[work]", "green"))
        print(colored(f"4. Слив живодëрства", 'red'),colored("[work]", "green"))
        print(colored(f"5. Слив ДП", 'red'),colored("[work]", "green"))
        print(colored(f"6. Угрозы", 'red'),colored("[work]", "green"))
        print(colored(f"7. Сват", 'red'),colored("[work]", "green"))
        comp_choice = input(colored(f"Выберите способ:",'red'))
        
        if choice in ["1", "2", "3", "4", "5", "6", "7"]:
            chat_link = input(colored(f"Ссылка на группу:",'red'))
            chat_violation = input(colored(f"Ссылка на нарушение:",'red'))
            comp_texts = {
                "1": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел группу, в которой распространяют личные данные невинных людей. Ссылка на грппу - {chat_link}, сслыки на нарушения - {chat_violation}. Пожалуйста заблокируйте данную группу.",
                "2": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел группу в  которой распространяют материалы порнографического характера. Ссылка на группу - {chat_link}, сслыки на нарушения - {chat_violation}. Пожалуйста заблокируйте данную группу.",
                "3": f"Здравствуйте, уважаемая поддержка телеграма. На вашей платформе я нашел группу в  которой распространяют расчленëнку, расправы. Ссылка на группу - {chat_link}, сслыки на нарушения - {chat_violation}. Пожалуйста заблокируйте данную группу.",
                "4": f"Здравствуйте,уважаемая поддержка телеграмм,хочу пожаловаться вам на группу в которой сливают Жестокое обращеение с живоотными (живодëрство). Ссылка на телеграмм группу:{chat_link} Ссылка на нарушение:{chat_violation} Просьба заблокировать данную группу.",
                "5": f"Здравствуйте, уважаемая поддержка Telegram. Я бы хотел вам сообщить о группе, нарушающей правила площадки. Группа :{chat_link} .Нарушения: В данной группе сливают ДП (детскую порнографию). Ниже прикрепляю доказательства: {chat_violation}",
                 "6": f"Здравствуйте, уважаемая поддержка Telegram. Я бы хотел вам сообщить о группе, нарушающей правила площадки. Ссылка на группу - {chat_link} .Нарушения: Угрозы, доксом , сватом .Ниже прикрепляю доказательства: {chat_violation}",
                  "7": f"Здравствуйте, уважаемая поддержка телеграм. На вашей платформе я нашел группу в которой распространяют Сват - лжеминирование зданий ,сватинг .Ссылка на группу - {chat_link}, сслыки на нарушения - {chat_violation}. Пожалуйста заблокируйте данную группу."
                 }        
        for sender_email, sender_password in senders.items():
               for receiver in receivers:
                    comp_text = comp_texts[choice]
                    comp_body = comp_text.format(chat_link=chat_link.strip(), chat_violation=chat_violation.strip)
                    send_email(receiver, sender_email, sender_password, 'Жалоба на телеграм группу', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 100000
                    time.sleep(5)
                    
    elif choice == "5":
            username = input(colored(f"@username:",'red'))
            id = input(colored(f"Telegram ID:",'red'))
            comp_texts = {
                "5": f"Здравствуйте, уважаемая поддержка. Я случайно перешел по фишинговой ссылке и утерял доступ к своему аккаунту. Его юзернейм - {username}, его айди - {id}. Пожалуйста удалите аккаунт или обнулите сессии"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[choice]
                    comp_body = comp_text.format(username=username.strip(), id=id.strip())
                    send_email(receiver, sender_email, sender_password, 'Я утерял свой аккаунт в телеграм', comp_body)
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 9999
                    time.sleep(5)
                    
    elif choice == "6":
            number = input(colored(f"Номер | без +:",'red'))
            applicationVersion = input(colored(f"Версия приложения | Пример - 10.14.5 (49452):",'red'))
            operatingSystemVersion = input(colored(f"Версия операционной системы | Пример - SDK 33:",'red'))
            deviceName = input(colored(f"Название устройства | Пример - Xiaomi22041216G:",'red'))
            locale = input(colored(f"Регион | Пример - ru:",'red'))
            comp_texts = {
                "6": f"I'm trying to use my mobile phone number: {number}  But Telegram says it's banned. Please help.\n\nApp version: {applicationVersion}\nOS version: \nDevice Name: {deviceName}\nLocale: {locale}"
            }

            for sender_email, sender_password in senders.items():
                for receiver in receivers:
                    comp_text = comp_texts[choice]
                    comp_body = comp_text.format(number=number.strip(), applicationVersion=applicationVersion.strip(), operatingSystemVersion=operatingSystemVersion.strip(),  deviceName=deviceName.strip(),  locale=locale.strip())
                    
                    send_email(receiver, sender_email, sender_password, 'Banned phone numbers', comp_body) 
                    print(colored(f"Отправлено на {receiver} от {sender_email}!", 'red'))
                    sent_emails += 9999
                    time.sleep(0.001)
                    
                    
if __name__ == "__main__":
     main()

