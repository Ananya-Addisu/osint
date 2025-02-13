import requests
from bs4 import BeautifulSoup
import re
import webbrowser

def search_phone_number(phone_number):
    url = "https://www.google.com/search?q={}".format(phone_number)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('a')
        excluded_domains = ['google.com', 'maps.google.com', 'shop.grahamfield.com']
        phone_links = []
        for link in search_results:
            href = link.get('href')
            if href and not any(domain in href for domain in excluded_domains):
                cleaned_url = re.findall(r'(https?://\S+)', href)
                if cleaned_url:
                    phone_links.extend(cleaned_url)
        return phone_links
    else:
        return "Невозможно получить результаты поиска. Пожалуйста, попробуйте еще раз позже."

def save_links_to_html(links):
    css_styles = [
        "<style>",
        "* {",
        "    box-sizing: border-box;",
        "    margin: 0;",
        "    padding: 0;",
        "}",
        "body {",
        "    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;",
        "    background-color: #222;",
        "    color: #ddd;",
        "}",
        ".container {",
        "    max-width: 800px;",
        "    margin: 0 auto;",
        "    padding: 40px;",
        "    background-color: #333;",
        "    box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);",
        "    border-radius: 10px;",
        "}",
        "h1 {",
        "    text-align: center;",
        "    margin-bottom: 30px;",
        "    font-size: 36px;",
        "    color: #fff;",
        "    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);",
        "}",
        ".link-list {",
        "    list-style-type: none;",
        "}",
        ".link-item {",
        "    margin-bottom: 20px;",
        "    padding: 20px;",
        "    background-color: #444;",
        "    border-radius: 5px;",
        "    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);",
        "    transition: transform 0.3s ease, box-shadow 0.3s ease;",
        "}",
        ".link-item:hover {",
        "    transform: translateY(-5px);",
        "    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.7);",
        "}",
        ".link-item a {",
        "    display: block;",
        "    color: #0099ff;",
        "    text-decoration: none;",
        "    font-size: 18px;",
        "    font-weight: bold;",
        "    transition: color 0.3s ease;",
        "}",
        ".link-item a:hover {",
        "    color: #00ccff;",
        "}",
        "</style>"
    ]
    css_string = ''.join(css_styles)

    html = """<!DOCTYPE html>
<html>
<head>
    <title>Search Results</title>
    {}
</head>
<body>
    <div class="container">
        <h1>Search Results</h1>
        <ul class="link-list">
            {}
        </ul>
    </div>
</body>
</html>
""".format(css_string, ''.join(['<li class="link-item"><a href="{}">{}</a></li>'.format(link, link) for link in links]))

    with open("search_results.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Результаты сохранены в search_results.html")

def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
   _____ _________    ____  ________  ____________ 
  / ___// ____/   |  / __ \/ ____/ / / / ____/ __ \\
  \\__ \\/ __/ / /| | / /_/ / /   / /_/ / __/ / /_/ /
 ___/ / /___/ ___ |/ _, _/ /___/ __  / /___/ _, _/ 
/____/_____/_/  |_/_/ |_|\____/_/ /_/_____/_/ |_| 
              РАЗРАБОТЧИК: @KADICK1                         
"""
    print(banner)

def print_links_to_console(links):
    print("\nFound {} links:".format(len(links)))
    for link in links:
        print(link)

def main():
    while True:
        clear_console()
        print_banner()
        phone_number = input("Введите номер телефона: ")

        results = search_phone_number(phone_number)
        print_links_to_console(results)

        print("\n" * 2)

        save_links_to_html(results)

        input("Нажмите enter для продолжения...")

if __name__ == "__main__":
    main()