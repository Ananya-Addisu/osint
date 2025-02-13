from telethon import TelegramClient, errors, events
import asyncio
import os
from pystyle import Write, Colors
import subprocess
import re

api_id = '21826549'
api_hash = 'c1a19f792cfd9e397200d16c7e448160'

gog = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣴⣤⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡒⣂⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡞⡳⡏⣳⣶⡫⡷⢗⡦⣄⠀⠀⠀⠀⠀⠀⠀⠀⣤⢖⣛⣅⣗⣦⡠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣙⠽⢼⣶⡣⢽⢧⡧⣳⣟⡷⢶⣦⣀⠀⠀⣠⣾⣱⣭⣧⣟⢷⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠑⣄⠍⡘⣒⣓⠾⢱⣢⢼⣝⣾⣏⡿⢏⣕⣎⣭⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠢⠼⣀⣭⢱⡃⠜⣼⣾⣿⢹⣻⣿⢿⠝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢺⢟⡗⠴⣾⠙⠕⣾⠟⣤⢕⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢠⡤⠴⠒⢶⣖⣶⣶⡲⠶⡢⣢⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡐⡡⢤⡫⣲⡧⠦⣃⡯⣷⣧⢛⢺⡑⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣶⣚⣯⡷⠟⠩⡿⠯⠿⠿⠾⠛⠓⣛⢯⣥⡷⣮⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠄⣾⢞⣷⢻⡧⣟⠯⢙⡊⠄⠳⡗⡧⢳⣱⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡻⡿⣏⡟⢭⣞⠼⡫⠾⠗⠹⠹⠍⠋⠸⠇⡟⡿⣷⡷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣞⠥⣫⣋⡩⢖⢻⣾⠖⠛⠁⠀⠀⠀⠓⡍⡻⣓⣊⢇⠀⠀⠀⠀⠀⠀⠀⠀⡔⡞⣟⣷⢗⡣⡘⢂⠁⠁⠐⠐⠀⠀⠀⠀⠀⠀⠀⠈⠋⢽⡷⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠞⡑⠿⣶⡭⠵⠓⠙⠀⠀⠀⠀⠀⠀⠀⠀⢍⠶⡺⣳⢈⡆⠀⠀⠀⠀⠀⠀⠀⠈⣗⣛⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠘⠛⡛⠛⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢖⣈⡧⢤⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⢄⣴⡔⠚⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠘⢝⠵⣿⣟⣶⡚⠽⣇⣳⣲⣶⣆⠦⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡴⠟⠻⣿⡏⣻⠏⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⡗⠱⣼⡟⡁⠀⢘⣼⡣⢚⣮⡚⠴⠎⢾⣺⣚⡻⢷⣠⢿⡵⡾⣶⡲⣲⣲⢶⣲⣲⣶⢲⣶⡴⠶⡲⣔⣖⣲⣲⣶⢶⣾⡟⡹⡺⠁⠀⠀⢻⣜⡝⠀⡐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠳⠀⠈⠉⣅⡄⠈⢽⡷⡟⠁⠀⠀⠈⡾⢼⡽⣼⡘⣯⢟⣷⠓⢝⣽⣔⢨⡼⣷⣏⡸⣥⢷⣽⣇⣛⣡⡿⢿⣿⢵⣿⠿⣿⣭⠇⠀⣠⠀⠼⠁⠀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠑⣤⣶⡋⡇⠀⠘⠛⠁⠀⠠⡀⠀⠘⣧⠯⡺⣿⡫⠊⠹⡶⡸⣇⡿⢍⡿⢹⣔⡻⣟⠋⠳⡾⡿⢻⠃⠀⣻⡿⠃⠀⠥⡟⠀⢠⣾⡧⠀⣠⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠨⡼⡎⢷⠄⠀⠀⠀⠠⣚⡂⠀⠀⠸⡟⠛⠁⠀⠀⠀⠀⠉⠿⡽⠿⠁⠀⠹⡟⠃⠀⠀⠙⠏⣿⠀⠀⠈⠁⠀⠀⠈⠀⠀⣜⣿⡭⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢭⡞⣇⠀⢀⠲⡚⡵⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠉⠀⠀⠀⠀⠀⠁⠀⠀⠀⡟⠵⢦⠄⠀⠀⡻⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣷⡸⡻⡗⣿⡇⠀⠀⢀⡦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⢰⣲⠻⣊⡿⠖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⢍⡍⠭⡇⠀⣤⠟⣿⣇⠀⠀⠀⠀⡄⣤⡀⠀⠀⠀⠀⠀⡤⣤⠀⠀⢬⣞⣅⣀⡀⢿⡮⠜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠧⣼⣫⠩⣥⣃⠄⠀⠄⡠⡊⣹⠇⠀⠀⠀⠀⢐⣰⣧⠄⢰⢹⡺⡐⠷⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⠽⣮⠏⠄⢀⡎⡿⣅⡿⡮⠀⠀⢠⣾⣷⢷⢊⣆⢏⡻⠺⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠺⠭⢌⡢⡫⠿⠦⠀⣧⣿⡼⡼⠷⠂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

def clear_screen():
    subprocess.call('clear' if os.name == 'posix' else 'cls', shell=True)

async def create_account():
    phone = Write.Input("Введите ваш номер телефона: ", Colors.black_to_green, interval=0.0001)
    session_name = f"session_{phone}"
    client = TelegramClient(session_name, api_id, api_hash)
    
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(phone)
        code = Write.Input("Введите код подтверждения: ", Colors.black_to_green, interval=0.0001)
        try:
            await client.sign_in(phone, code)
        except errors.SessionPasswordNeededError:
            password = Write.Input("Введите пароль от 2fa: ", Colors.black_to_green, interval=0.0001)
            await client.sign_in(password=password)
    
    Write.Print(f"Аккаунт успешно создан и сохранен как {session_name}.session", Colors.black_to_green, interval=0.0001)
    await client.disconnect()
    input("\nНажмите Enter для возвращения в меню...")

async def auto_click_links(session_name):
    client = TelegramClient(session_name, api_id, api_hash)
    
    try:
        await client.connect()
        if not await client.is_user_authorized():
            Write.Print(f"Сессия {session_name} не авторизована. Пропускаем.\n", Colors.black_to_green, interval=0.0001)
            await client.disconnect()
            return
        
        dialogs = await client.get_dialogs()
        if '@send' not in [dialog.name for dialog in dialogs]:
            await client.send_message('send', '/start')
            Write.Print(f"Отправлена команда /start боту @send для сессии {session_name}\n", Colors.black_to_green, interval=0.0001)
        
        @client.on(events.NewMessage(incoming=True, pattern=r'http://t\.me/send\?start=.*'))
        async def handler(event):
            link = event.message.message
            Write.Print(f"Найдена ссылка в сессии {session_name}: {link}\n", Colors.black_to_green, interval=0.0001)
            start_param = link.split('=')[1]
            await client.send_message('send', f'/start {start_param}')
            Write.Print(f"Отправлена команда /start {start_param} боту @send в сессии {session_name}\n", Colors.black_to_green, interval=0.0001)
        
        @client.on(events.NewMessage(incoming=True, from_users='send'))
        async def bot_response_handler(event):
            if 'Вы получили' in event.message.message:
                match = re.search(r'Вы получили 🪙 ([\d.]+) (USDT) \(([\d.]+) RUB\)', event.message.message)
                if match:
                    amount_crypto = match.group(1)
                    crypto_type = match.group(2)
                    amount_rub = match.group(3)
                    Write.Print(f"Ссылка активирована в сессии {session_name}, получили {amount_crypto} {crypto_type} ({amount_rub} RUB)\n", Colors.black_to_green, interval=0.0001)
                else:
                    Write.Print(f"Не удалось получить сумму в сессии {session_name}\n", Colors.black_to_green, interval=0.0001)
            elif 'Введите пароль от чека' in event.message.message:
                Write.Print(f"Ошибка в сессии {session_name}: чек под паролем\n", Colors.black_to_red, interval=0.0001)
            elif 'Этот чек уже активирован' in event.message.message:
                Write.Print(f"Ошибка в сессии {session_name}: чек оказался просрочен\n", Colors.black_to_red, interval=0.0001)
            else:
                Write.Print(f"Неизвестный ответ от бота в сессии {session_name}: {event.message.message}\n", Colors.black_to_red, interval=0.0001)
        
        await client.run_until_disconnected()
    except Exception as e:
        Write.Print(f"Ошибка при запуске сессии {session_name}: {e}\n", Colors.black_to_red, interval=0.0001)
    finally:
        await client.disconnect()

async def main_async():
    while True:
        clear_screen()
        Write.Print(gog, Colors.black_to_green, interval=0.0001)        
        Write.Print("\n  Меню:", Colors.black_to_green, interval=0.0001)
        Write.Print("\n  1. Создать аккаунт", Colors.black_to_green, interval=0.0001)
        Write.Print("\n  2. Авто крипта", Colors.black_to_green, interval=0.0001)
        Write.Print("\n  3. Выход", Colors.black_to_green, interval=0.0001)
        choice = Write.Input("\n  Выберите опцию: ", Colors.black_to_green, interval=0.0001)
        
        if choice == '1':
            await create_account()
        elif choice == '2':
            session_files = [f for f in os.listdir() if f.endswith('.session')]
            if not session_files:
                Write.Print("Нет доступных сессий. Пожалуйста, создайте аккаунт сначала.\n", Colors.black_to_green, interval=0.0001)
                input("\nНажмите Enter для возвращения в меню...")
                continue
            
            tasks = [auto_click_links(session_file.replace('.session', '')) for session_file in session_files]
            await asyncio.gather(*tasks)
            input("\nНажмите Enter для возвращения в меню...")
        elif choice == '3':
            break
        else:
            Write.Print("Неверный выбор. Пожалуйста, попробуйте снова.", Colors.black_to_green, interval=0.0001)

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_async())

if __name__ == "__main__":
    main()