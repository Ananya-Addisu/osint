from telethon.sync import TelegramClient
from telethon import functions, types
import datetime
from telethon.sync import TelegramClient
from telethon import functions, types
print('Bot started')
print("By Casty")
api_id = '23091712'
api_hash = '457430328238f46adedc51c232ce' 
#по желанию ставьте while True
i = 0
with TelegramClient('session_name', api_id, api_hash) as client:
    while True:
     result = client(functions.account.ReportPeerRequest(
     peer='autowin_ct',
          reason=types.InputReportReasonSpam(), 
     message='\n'
     
     
     
     
     
     ))
     print(result)
     
     i += 1
     
     now = datetime.datetime.now()
     print(now.strftime("%H:%M:%S"))
     print("Жалоба отправлена\n Всего отправлено", i, "жалоб")