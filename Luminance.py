#спиздишь код все 32 в ряд вылетят
while True:
    try:

        import sys
        import os
        import time
        import subprocess
        import webbrowser

        RESET = "\033[0m"
        GREEN_TEXT = "\033[32m"
        BLACK_BG = "\033[40m"

        required_modules = [
            "pystyle",
            "urllib3",
            "beautifulsoup4",
            "phonenumbers",
            "faker",
            "python-whois",
            "requests"
        ]


        def clear_console():
            os.system('cls' if os.name == 'nt' else 'clear')


        def print_with_delay(text, delay=0.1):
            for char in text:
                print(char, end='', flush=True)
                time.sleep(delay)
            print()


        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])


        def install_modules():
            print_with_delay(
                GREEN_TEXT + "Вас приветствует мастер установки Luminance Repack.\nСейчас мы проведем установку всех зависимостей для правильной работы программы.\nУстановка не займет более 3х минут.\n3\n2\n1\n" + RESET)
            for module in required_modules:
                try:
                    __import__(module)
                    print(GREEN_TEXT + f"{module} уже установлен.")
                except ImportError:
                    print(f"Установка {module}...")
                    install(module)
                    print_with_delay(GREEN_TEXT + f"Установлен модуль {module}" + RESET)

            print_with_delay(GREEN_TEXT + "Запускаем программу Luminance Repack..." + RESET)
            time.sleep(4)
            os.system('cls' if os.name == 'nt' else 'clear')
    except EOFError:
        print("Установка отменена.")

    import urllib
    import bs4
    import faker
    from pystyle import Anime, Colors, Colorate, Box, Write, Center
    import whois
    import string
    import platform
    import requests
    import pystyle
    import os
    import time
    import random
    import socket
    import urllib3

    urllib3.disable_warnings()

    def getwebsiteinfo(website):
            whoisdata = whois.whois(website)
            info = f"""
      |Информация о сайте: 
      |Домен: {whoisdata.domainname}
      |Зарегистрирован: {whoisdata.creationdate}
      |Истекает: {whoisdata.expirationdate}  
      |Владелец: {whoisdata.registrantname}
      |Организация: {whoisdata.registrantorganization}
      |Адрес: {whoisdata.registrantaddress}
      |Город: {whoisdata.registrantcity}
      |Штат: {whoisdata.registrantstate}
      |Почтовый индекс: {whoisdata.registrantpostalcode}
      |Страна: {whoisdata.registrantcountry}
      |IP-адрес: {whoisdata.nameservers}
        """
            Write.Print(info + "\n", Colors.red_to_yellow, interval=0.005)


    def Search(Data):
        try:
            global last_search_time
            current_time = time.time()
            if current_time - last_search_time < 60:
                pystyle.Write.Print("\n[!] Подождите минуту перед следующим запросом\n", pystyle.Colors.red, interval=0.0001)
                return
            for database, info in requests.post("https://server.leakosint.com/", json={"token":"6652134584:OGYRHDIr", "request":Data, "limit":100, "lang":"ru"}).json()['List'].items():
                if "No results found" in database:
                    pystyle.Write.Print("\n[!] Ничего не найдено\n", pystyle.Colors.red_to_yellow, interval = 0.0001)
                    break
                pystyle.Write.Print("\n[@] База данных -> ", pystyle.Colors.red_to_yellow, interval = 0.0001)
                pystyle.Write.Print(database, pystyle.Colors.white, interval = 0.0001)
                pystyle.Write.Print("\n\n[@] Описание -> ", pystyle.Colors.red_to_yellow, interval = 0.0001)
                pystyle.Write.Print(f"{info['InfoLeak']}\n", pystyle.Colors.white, interval = 0.0001)
                for record in info['Data']:
                    for key, value in record.items():
                        pystyle.Write.Print(f"\n[@] {key} -> ", pystyle.Colors.red_to_yellow, interval = 0.0001)
                        pystyle.Write.Print({value}, pystyle.Colors.white, interval = 0.0001)
                print()
            last_search_time = current_time
        except:
            pystyle.Write.Print("\n[!] Произошла ошибка\n", pystyle.Colors.red, interval = 0.0001)


    def propen():
        url = "https://t.me/pr0xit"
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
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    install_modules()
    propen()
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    Write.Print(Center.XCenter('''
    ███████╗██╗  ██╗██████╗ ██╗██████╗ ███████╗██████╗ 
    ██╔════╝╚██╗██╔╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
    █████╗   ╚███╔╝ ██████╔╝██║██████╔╝█████╗  ██║  ██║
    ██╔══╝   ██╔██╗ ██╔═══╝ ██║██╔══██╗██╔══╝  ██║  ██║
    ███████╗██╔╝ ██╗██║     ██║██║  ██║███████╗██████╔╝
    ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ 
    |𝐏𝐫𝐞𝐦𝐢𝐮𝐦 𝐄𝐝𝐢𝐭𝐢𝐨𝐧|                |𝔟𝔶 @thiasoft|
    
                     ↓ REPACK BY ↓
             Telegram > https://t.me/pr0xit                          
    ╔═════════════════════════════════════════════════════════════════════════╗
    ║[1] Поиск по почте   [7] Поиск по авто       [13]Инфа о сайте            ║
    ║                                                                         ║ 
    ║[2] Поиск по ФИ      [8] Поиск по VIN        [14]Сложный пароль          ║
    ║                                                                         ║
    ║[3] Поиск по ФИО     [9] Поиск по Telegram   [15]Порт сканер             ║
    ║                                                                         ║
    ║[4] Поиск по нику    [10] Поиск по Facebook  [16]Странный текст          ║
    ║                                                                         ║
    ║[5] Поиск по номеру  [11] Поиск по Instagram [17]Выдать прокси           ║
    ║                                                                         ║
    ║[6] Поиск по паролю  [12] Поиск по IP        [18]Web-crawler             ║
    ║                                                                         ║
    ║[19]Поиск по MAC-адр                         [21]Вымышленная личность    ║
    ║                                                                         ║
    ║[22]ВымышленнаяКарта [23]Поиск по БД         [24]Генератор номеров тел   ║
    ║                                                                         ║    
    ║               [77] Инфо                    [99] Выход                   ║
    ╚═════════════════════════════════════════════════════════════════════════╝'''), Colors.blue_to_green, interval=0.000001)
    print()
    print()

    while True:
        choice = pystyle.Write.Input("[$] Введите номер функции -> ", pystyle.Colors.blue_to_green, interval = 0.005)
        print()
        if choice == "1":
            Data = pystyle.Write.Input("[$] Введите почту -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "2":
            Data = pystyle.Write.Input("[$] Введите ФИ -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "3":
            Data = pystyle.Write.Input("[$] Введите ФИО -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "4":
            Data = pystyle.Write.Input("[$] Введите ник -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "5":
            Data = pystyle.Write.Input("[$] Введите номер -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "6":
            Data = pystyle.Write.Input("[$] Введите пароль -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "7":
            Data = pystyle.Write.Input("[$] Введите номер авто -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "8":
            Data = pystyle.Write.Input("[$] Введите VIN -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "9":
            Data = pystyle.Write.Input("[$] Введите Telegram ID -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "10":
            Data = pystyle.Write.Input("[$] Введите Facebook ID -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "11":
            Data = pystyle.Write.Input("[$] Введите Instagram ID -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "12":
            Data = pystyle.Write.Input("[$] Введите IP -> ", pystyle.Colors.blue_to_green, interval = 0.005)
            Search(Data)
            print()
        if choice == "77":
            pystyle.Write.Print("[$] Владелец и его команда не несет ответственности за ваши действия\n Репак кряка, вырезан мусор, не рабочие функции", pystyle.Colors.red, interval = 0.005)
            print()
            print()
        if choice == '13':
            domain = Write.Input("Введите домен сайта: ", Colors.red_to_yellow, interval=0.005)
            getwebsiteinfo(domain)

        if choice == '14':
            def get_characters(strength):
                characters = string.ascii_letters + string.digits
                if strength == "medium":
                    characters += "!@#$%^&*()qwertyuiopasdfghjklzxcvbnm,./;[]йцукенгшщзхъфывапролдячсмить"
                elif strength == "high":
                    characters += string.punctuation
                return characters
            def generate_password(length, strength):
                characters = get_characters(strength)
                password = ''.join(random.choice(characters) for i in range(length))
                return password
            password_length = int(Write.Input('Введите длину пароля: ', Colors.red_to_yellow, interval=0.005))
            complexity = Write.Input('Выберите сложность (low, medium, high): ', Colors.red_to_yellow, interval=0.005)
            complex_password = generate_password(password_length, complexity)
            Write.Print(complex_password + "\n", Colors.red_to_yellow, interval=0.005)

        if choice == '15':
                    pystyle.Write.Print("\n[$] Выберите режим: ", pystyle.Colors.red_to_yellow, interval=0.005)
                    pystyle.Write.Print("\n\n[$] 1 - проверить часто используемые порты", pystyle.Colors.red_to_yellow, interval=0.005)
                    pystyle.Write.Print("\n\n[$] 2 - проверить указанный порт", pystyle.Colors.red_to_yellow, interval=0.005)
                    mode = pystyle.Write.Input("\n\n[$] Ваш выбор: ", pystyle.Colors.red_to_yellow, interval=0.005)
                    if mode == "1":
                        print()
                        ports = [
                            20,
                            26,
                            28,
                            29,
                            55,
                            53,
                            80,
                            110,
                            443,
                            8080,
                            1111,
                            1388,
                            2222,
                            1020,
                            4040,
                            6035,
                        ]
                        for port in ports:
                            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            result = sock.connect_ex(("127.0.0.1", port))
                            if result == 0:
                                pystyle.Write.Print(f"[$] Порт {port} открыт", pystyle.Colors.red_to_yellow, interval=0.005)
                            else:
                                pystyle.Write.Print(f"[$] Порт {port} закрыт", pystyle.Colors.red_to_yellow, interval=0.005)
                            sock.close()
                            print()
                    elif mode == "2":
                        port = pystyle.Write.Input("\n[$] Введите номер порта: ", pystyle.Colors.red_to_yellow, interval=0.005)
                        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        result = sock.connect_ex(("127.0.0.1", int(port)))
                        print()
                        if result == 0:
                            pystyle.Write.Print(f"[$] Порт {port} открыт", pystyle.Colors.red_to_yellow, interval=0.005)
                        else:
                            pystyle.Write.Print(f"[$] Порт {port} закрыт", pystyle.Colors.red_to_yellow, interval=0.005)
                        sock.close()
                        print()
                    else:
                        pystyle.Write.Print("\n[$] Неизвестный режим", pystyle.Colors.red_to_yellow, interval=0.005)
                        print()
        if choice == "16":
                    def transform_text(input_text):
                        translit_dict = {
                            "а": "@",
                            "б": "Б",
                            "в": "B",
                            "г": "г",
                            "д": "д",
                            "е": "е",
                            "ё": "ё",
                            "ж": "ж",
                            "з": "3",
                            "и": "u",
                            "й": "й",
                            "к": "K",
                            "л": "л",
                            "м": "M",
                            "н": "H",
                            "о": "0",
                            "п": "п",
                            "р": "P",
                            "с": "c",
                            "т": "T",
                            "у": "y",
                            "ф": "ф",
                            "х": "X",
                            "ц": "ц",
                            "ч": "4",
                            "ш": "ш",
                            "щ": "щ",
                            "ъ": "ъ",
                            "ы": "ы",
                            "ь": "ь",
                            "э": "э",
                            "ю": "ю",
                            "я": "я",
                            "А": "A",
                            "Б": "6",
                            "В": "V",
                            "Г": "r",
                            "Д": "D",
                            "Е": "E",
                            "Ё": "Ё",
                            "Ж": "Ж",
                            "З": "2",
                            "И": "I",
                            "Й": "Й",
                            "К": "K",
                            "Л": "Л",
                            "М": "M",
                            "Н": "H",
                            "О": "O",
                            "П": "П",
                            "Р": "P",
                            "С": "C",
                            "Т": "T",
                            "У": "Y",
                            "Ф": "Ф",
                            "Х": "X",
                            "Ц": "Ц",
                            "Ч": "Ч",
                            "Ш": "Ш",
                            "Щ": "Щ",
                            "Ъ": "Ъ",
                            "Ы": "bl",
                            "Ь": "b",
                            "Э": "Э",
                            "Ю": "9Y",
                            "Я": "9A",
                        }
                        transformed_text = []
                        for char in input_text:
                            if char in translit_dict:
                                transformed_text.append(translit_dict[char])
                            else:
                                transformed_text.append(char)
                        return "".join(transformed_text)
                    input_text = pystyle.Write.Input("\n[$] Введите текст -> ", pystyle.Colors.red_to_yellow, interval=0.005)
                    transformed_text = transform_text(input_text)
                    print()
                    pystyle.Write.Print("[$] Результат -> " + transformed_text + "\n", pystyle.Colors.red_to_yellow, interval=0.005)

        if choice == "17":
                    def get_proxy():
                        proxy_api_url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all"

                        try:
                            response = requests.get(proxy_api_url)
                            if response.status_code == 200:
                                proxy_list = response.text.strip().split("\r\n")
                                return proxy_list
                            else:
                                pystyle.Write.Print(f"\nПроизошла ошибка -> {response.status_code}", pystyle.Colors.red_to_yellow, interval=0.005)
                        except Exception as e:
                            pystyle.Write.Print(f"\nПроизошла ошибка -> {str(e)}", pystyle.Colors.red_to_yellow, interval=0.005)

                        return None

                    proxies = get_proxy()
                    if proxies:
                        pystyle.Write.Print("\nПрокси:\n", pystyle.Colors.red_to_yellow, interval=0.005)
                        for proxy in proxies:
                            pystyle.Write.Print("\n" + proxy, pystyle.Colors.red_to_yellow, interval=0.005)
                        print()
                    else:
                        pystyle.Write.Print("Прокси недоступно.", pystyle.Colors.red_to_yellow, interval=0.005)

        if choice == "18":
            start_url = pystyle.Write.Input("[$] Введите ссылку -> ", pystyle.Colors.red_to_yellow, interval=0.005)
            max_depth = 2
            visited = set()


            def crawl(url, depth=0):
                if depth > max_depth:
                    return
                parsed = urllib.parse.urlparse(url)
                domain = f"{parsed.scheme}://{parsed.netloc}"
                if url in visited:
                    return
                try:
                    response = requests.get(url)
                    html = response.text
                    soup = bs4.BeautifulSoup(html, "html.parser")
                except Exception as e:
                    print(f"Ошибка при обработке {url}: {e}")
                    return
                visited.add(url)
                pystyle.Write.Print("[$] " + url + "\n", pystyle.Colors.red_to_yellow, interval=0.005)
                for link in soup.find_all("a"):
                    href = link.get("href")
                    if not href:
                        continue
                    href = href.split("#")[0].rstrip("/")
                    if href.startswith("http"):
                        href_parsed = urllib.parse.urlparse(href)
                        if href_parsed.netloc != parsed.netloc:
                            continue
                    else:
                        href = domain + href
                    crawl(href, depth + 1)


            print()
            crawl(start_url)

        if choice == "19":
                    def mac_lookup(mac_address):
                        api_url = f"https://api.macvendors.com/{mac_address}"
                        try:
                            response = requests.get(api_url)
                            if response.status_code == 200:
                                return response.text.strip()
                            else:
                                return f"Error: {response.status_code} - {response.text}"
                        except Exception as e:
                            return f"Error: {str(e)}"
                    mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.red_to_yellow, interval = 0.005)
                    vendor = mac_lookup(mac_address)
                    pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.red_to_yellow, interval = 0.005)


        if choice == "21":
            fake = faker.Faker(locale="ru_RU")
            gender = pystyle.Write.Input("\n[$] Введите пол (М - мужской, Ж - женский): ", pystyle.Colors.red_to_yellow,
                                         interval=0.005)
            print()

            if gender not in ["М", "Ж"]:
                gender = random.choice(["М", "Ж"])
                pystyle.Write.Print(f"[$] Вы ввели неверное значение, будет выбрано случайным образом: {gender}\n\n",
                                    pystyle.Colors.red_to_yellow, interval=0.005)

            if gender == "М":
                first_name = fake.first_name_male()
                middle_name = fake.middle_name_male()
            else:
                first_name = fake.first_name_female()
                middle_name = fake.middle_name_female()

            last_name = fake.last_name()
            full_name = f"{last_name} {first_name} {middle_name}"
            birthdate = fake.date_of_birth()
            age = fake.random_int(min=18, max=80)
            street_address = fake.street_address()
            city = fake.city()
            region = fake.region()
            postcode = fake.postcode()
            address = f"{street_address}, {city}, {region} {postcode}"
            email = fake.email()
            phone_number = fake.phone_number()
            inn = str(fake.random_number(digits=12, fix_len=True))
            snils = str(fake.random_number(digits=11, fix_len=True))
            passport_num = str(fake.random_number(digits=10, fix_len=True))
            passport_series = fake.random_int(min=1000, max=9999)

            pystyle.Write.Print(f"[$] ФИО: {full_name}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] Пол: {gender}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] Дата рождения: {birthdate.strftime('%d %B %Y')}\n", pystyle.Colors.red_to_yellow,
                                interval=0.005)
            pystyle.Write.Print(f"[$] Возраст: {age} лет\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] Адрес: {address}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] Email: {email}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] Телефон: {phone_number}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] ИНН: {inn}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] СНИЛС: {snils}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print(f"[$] Паспорт серия: {passport_series} номер: {passport_num}\n",
                                pystyle.Colors.red_to_yellow, interval=0.005)

        if choice == "22":
                    pystyle.Write.Print("\n[$] Выберите страну:\n", pystyle.Colors.red_to_yellow, interval=0.005)
                    pystyle.Write.Print("[$] 1: Украина\n", pystyle.Colors.red_to_yellow, interval=0.005)
                    pystyle.Write.Print("[$] 2: Россия\n", pystyle.Colors.red_to_yellow, interval=0.005)
                    pystyle.Write.Print("[$] 3: Казахстан\n", pystyle.Colors.red_to_yellow, interval=0.005)
                    country_choice = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.red_to_yellow, interval=0.005)

                    if country_choice == "1":
                        country = "Украина"
                    elif country_choice == "2":
                        country = "Россия"
                    elif country_choice == "3":
                        country = "Казахстан"
                    else:
                        pystyle.Write.Print("\n[$] Неправильный ввод.\n", pystyle.Colors.red_to_yellow, interval=0.005)

        if choice == "23":
            query = pystyle.Write.Input("[$] Введите запрос для поиска: ", pystyle.Colors.red_to_yellow, interval=0.005)
            Search(query)
            print()

        if choice == "24":
            def generate_phone_number(country):
                if country == "Россия":
                    return "+7" + ''.join([str(random.randint(0, 9)) for _ in range(10)])
                elif country == "Украина":
                    return "+380" + ''.join([str(random.randint(0, 9)) for _ in range(9)])
                elif country == "Казахстан":
                    return "+7" + ''.join([str(random.randint(0, 9)) for _ in range(10)])
                else:
                    return "Неизвестная страна"

            pystyle.Write.Print("\n[$] Выберите страну:\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print("[$] 1: Россия\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print("[$] 2: Украина\n", pystyle.Colors.red_to_yellow, interval=0.005)
            pystyle.Write.Print("[$] 3: Казахстан\n", pystyle.Colors.red_to_yellow, interval=0.005)

            country_choice = pystyle.Write.Input("\n[?] Ваш выбор: ", pystyle.Colors.red_to_yellow, interval=0.005)

            if country_choice == "1":
                country = "Россия"
            elif country_choice == "2":
                country = "Украина"
            elif country_choice == "3":
                country = "Казахстан"
            else:
                pystyle.Write.Print("\n[$] Неправильный ввод.\n", pystyle.Colors.red_to_yellow, interval=0.005)
                continue

            num_phones = int(pystyle.Write.Input("\n[$] Сколько номеров сгенерировать? ", pystyle.Colors.red_to_yellow, interval=0.005))

            pystyle.Write.Print("\n[$] Сгенерированные номера:\n", pystyle.Colors.red_to_yellow, interval=0.005)
            for _ in range(num_phones):
                phone_number = generate_phone_number(country)
                pystyle.Write.Print(f"[$] {phone_number}\n", pystyle.Colors.red_to_yellow, interval=0.005)
            print()

        if choice == "99":
            pystyle.Write.Print("\n[$] Выход из программы...\n", pystyle.Colors.red_to_yellow, interval=0.005)
            break