while True:

    import os
    import sys
    import subprocess
    import time

    RESET = "\033[0m"
    GREEN_TEXT = "\033[32m"
    BLACK_BG = "\033[40m"

    required_modules = [
        "pystyle",
        "urllib3",
        "phonenumbers",
        "colorama",
        "python-whois",
        "requests",
        "bs4",
        "faker",
        "datetime",
        "defusedxml",
        "qrcode",
        "speedtest",
        "ipwhois",
        "pillow",
        "PIL",
        "collections.abc",
        "collections",
        "ssl"
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


    def check_and_install_modules():
        print_with_delay(
            GREEN_TEXT + "Вас приветствует мастер установки Hunters Repack.\nСейчас мы проведем установку всех зависимостей для правильной работы программы\nУстановка не займет более 3-х минут.\n3\n2\n1\n" + RESET)
        for module in required_modules:
            try:
                __import__(module)
                print(GREEN_TEXT + f"{module} уже установлен." + RESET)
            except ImportError:
                print(f"Установка {module}...")
                install(module)
                print_with_delay(GREEN_TEXT + f"Установлен модуль {module}" + RESET)




    check_and_install_modules()

    import os
    import re
    import socket
    import whois
    import hashlib
    import requests
    import dns.resolver
    import speedtest
    from pystyle import Colors, Colorate, Center
    from PIL import Image
    from PIL.ExifTags import TAGS
    from datetime import datetime
    import ssl
    import time
    from bs4 import BeautifulSoup

    def clear_console():
        os.system('cls' if os.name == 'nt' else 'clear')

    def create_banner():
        ascii_art = """
                                                                                 
        ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ ███████╗
        ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗██╔════╝
        ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝███████╗
        ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗╚════██║
        ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║███████║
        ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝
                                                                    
                                                 
                                                                    
        ██████╗ ███████╗██████╗  █████╗  ██████╗██╗  ██╗            
        ██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝            
        ██████╔╝█████╗  ██████╔╝███████║██║     █████╔╝             
        ██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██║     ██╔═██╗             
        ██║  ██║███████╗██║     ██║  ██║╚██████╗██║  ██╗            
        ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝            
                                                                            
        """

        column1 = ["1. DNS Lookup", "2. WHOIS Lookup", "3. IP Lookup", "4. Image Metadata", "5. Data Breach Lookup"]
        column2 = ["6. Port Scan", "7. URL Availability Check", "8. SSL Certificate Check", "9. HTTP Headers Extraction", "10. Server Response Time Check"]
        column3 = ["11. HTML Parsing", "12. GitHub repository parsing", "13. Download video Youtube", "14. Scan VT", "15. Generated QR", "16. Convert PDF to Word", "17. Internet speedtest", "18. Exit"]

        # Проверяем, что все списки имеют одинаковую длину
        max_len = max(len(column1), len(column2), len(column3))
        column1.extend([""] * (max_len - len(column1)))
        column2.extend([""] * (max_len - len(column2)))
        column3.extend([""] * (max_len - len(column3)))

        max_width1 = max(len(item) for item in column1)
        max_width2 = max(len(item) for item in column2)
        max_width3 = max(len(item) for item in column3)

        menu = [
            f"{column1[i].ljust(max_width1)}    █  {column2[i].ljust(max_width2)}    █  {column3[i].ljust(max_width3)}"
            for i in range(max_len)
        ]

        developer_info = "Repack by @pr0xit | VERSION 1.2 BETA"
        price_info = "Price - Free"

        max_content_width = max(len(line) for line in ascii_art.split('\n'))
        max_menu_width = max(len(line) for line in menu)
        total_width = max(max_content_width, max_menu_width, len(developer_info), len(price_info)) + 4

        separator = "█" * (total_width - 2)

        combined = ascii_art.split('\n') + [separator] + menu + [separator, developer_info]

        border_line = "█" * total_width
        bordered_combined = [border_line]
        for line in combined:
            if line == separator:
                bordered_combined.append("█" + line + "█")
            elif line == developer_info:
                bordered_combined.append("█ " + line.center(total_width - 4) + " █")
            else:
                bordered_combined.append("█ " + line.center(total_width - 4) + " █")
        bordered_combined.append(border_line)

        price_separator = "█" * (len(price_info) + 4)
        price_box = [
            f"█ {price_info} █",
            price_separator
        ]

        price_box_centered = [line.center(total_width) for line in price_box]
        bordered_combined.extend(price_box_centered)

        bordered_combined_str = "\n".join(bordered_combined)
        centered_bordered_combined = Center.XCenter(bordered_combined_str)
        return Colorate.Diagonal(Colors.blue_to_cyan, centered_bordered_combined)

    def dns_lookup(domain):
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        try:
            result = resolver.resolve(domain, 'A')
            print(f"IP addresses for {domain}:")
            for ipval in result:
                print(f" - {ipval.to_text()}")
        except dns.resolver.NXDOMAIN:
            print(f"Could not resolve {domain}")
        except Exception as e:
            print(f"An error occurred: {e}")
        input("Press Enter to return to the menu...")

    def whois_lookup(domain):
        try:
            domain_info = whois.whois(domain)
            print(domain_info)
        except Exception as e:
            print(f"WHOIS lookup failed for {domain}: {e}")
        input("Press Enter to return to the menu...")

    def ip_lookup(ip):
        try:
            response = requests.get(f"https://ipinfo.io/{ip}/json")
            if response.status_code == 200:
                data = response.json()
                print(f"IP: {data.get('ip', 'N/A')}")
                print(f"Hostname: {data.get('hostname', 'N/A')}")
                print(f"City: {data.get('city', 'N/A')}")
                print(f"Region: {data.get('region', 'N/A')}")
                print(f"Country: {data.get('country', 'N/A')}")
                print(f"Location: {data.get('loc', 'N/A')}")
                print(f"Org: {data.get('org', 'N/A')}")
                print(f"Postal: {data.get('postal', 'N/A')}")
                print(f"Timezone: {data.get('timezone', 'N/A')}")
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"IP lookup failed for {ip}: {e}")
        input("Press Enter to return to the menu...")

    def image_metadata(image_path):
        try:
            image = Image.open(image_path)
            exif_data = image._getexif()

            if not exif_data:
                print(f"No EXIF metadata found in {image_path}")
                return

            metadata = {}
            for tag, value in exif_data.items():
                tag_name = TAGS.get(tag, tag)
                metadata[tag_name] = value

            for key, val in metadata.items():
                print(f"{key}: {val}")

        except Exception as e:
            print(f"Failed to extract metadata from {image_path}: {e}")

    def data_breach_lookup(email):
        try:
            url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
            headers = {"hibp-api-key": "YOUR_API_KEY"}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                breaches = response.json()
                if breaches:
                    print(f"Breaches found for {email}:")
                    for breach in breaches:
                        print(f"Name: {breach['Name']}, Domain: {breach['Domain']}, BreachDate: {breach['BreachDate']}")
                else:
                    print(f"No breaches found for {email}.")
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Data breach lookup failed for {email}: {e}")
        input("Press Enter to return to the menu...")

    def scan_port(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((ip, port))
            return True
        except:
            return False
        finally:
            s.close()


    def popi():

        import webbrowser
        import platform
        import os

        url = "https://t.me/pr0xit"
        if platform.system() == "Windows":
            webbrowser.open(url)
        elif platform.system() == "Linux":
            if 'termux' in os.getenv('PREFIX', ''):
                os.system(f'termux-open-url {url}')
            else:
                webbrowser.open(url)
        else:
            webbrowser.open(url)

    def port_scan(ip):
        print(Colorate.Horizontal(Colors.green_to_white, f"Scanning {ip} for open ports (expected time ~2 minutes)..."))
        start_time = datetime.now()
        open_ports = []

        for port in range(1, 1025):
            if scan_port(ip, port):
                open_ports.append(port)

        end_time = datetime.now()
        total_time = end_time - start_time

        print(Colorate.Horizontal(Colors.green_to_white, f"\nScan completed in {total_time}\n"))

        if open_ports:
            print(Colorate.Horizontal(Colors.green_to_white, "Open ports:"))
            for port in open_ports:
                print(Colorate.Horizontal(Colors.green_to_white, f"Port {port} is open"))
        else:
            print(Colorate.Horizontal(Colors.green_to_white, "No open ports found"))

        input(Colorate.Horizontal(Colors.green_to_white, "\nPress Enter to return to the menu..."))

    def url_availability_check(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"The URL {url} is reachable.")
            else:
                print(f"The URL {url} is not reachable. Status code: {response.status_code}")
        except requests.ConnectionError:
            print(f"The URL {url} is not reachable. Failed to establish a connection.")
        input("Press Enter to return to the menu...")

    def ssl_certificate_check(url):
        try:
            cert = ssl.get_server_certificate((url, 443))
            x509 = ssl.create_x509_from_der(ssl.PEM_cert_to_DER_cert(cert))
            subject = dict(x509.get_subject().get_components())
            issuer = dict(x509.get_issuer().get_components())
            print(f"Subject: {subject}")
            print(f"Issuer: {issuer}")
            print(f"Valid from: {x509.get_notBefore()}")
            print(f"Valid until: {x509.get_notAfter()}")
        except Exception as e:
            print(f"Failed to retrieve SSL certificate for {url}: {e}")
        input("Press Enter to return to the menu...")

    def http_headers_extraction(url):
        try:
            response = requests.head(url)
            print(f"HTTP headers for {url}:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Failed to retrieve HTTP headers for {url}: {e}")
        input("Press Enter to return to the menu...")

    def server_response_time_check(url):
        try:
            start_time = time.time()
            response = requests.get(url)
            end_time = time.time()
            response_time = end_time - start_time
            print(f"Server response time for {url}: {response_time} seconds")
        except Exception as e:
            print(f"Failed to measure server response time for {url}: {e}")
        input("Press Enter to return to the menu...")


    def html_parser(url):
        max_retries = 3
        retry_delay = 5


        def sanitize_filename(filename):
            return re.sub(r'[\\/*?:"<>|]', "_", filename)

        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                file_name = sanitize_filename(f"{url.replace('https://', '').replace('http://', '').replace('/', '_')}.html")
                with open(file_name, 'w', encoding='utf-8') as file:
                    file.write(soup.prettify())
                print(f"HTML content saved to {file_name}")
                break
            except requests.exceptions.Timeout:
                print(f"Failed to parse HTML for {url}: Request timed out.")
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:
                    if attempt < max_retries - 1:
                        print(f"Failed to parse HTML for {url}: {e}. Retrying in {retry_delay} seconds...")
                        time.sleep(retry_delay)
                    else:
                        print(f"Failed to parse HTML for {url}: {e}. Max retries reached.")
                else:
                    print(f"Failed to parse HTML for {url}: {e}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"Failed to parse HTML for {url}: {e}")
                break
            except OSError as e:
                print(f"Failed to save HTML for {url}: {e}")
                break
        input("Press Enter to return to the menu...")

    def github_repo_parser(url):
        try:

            repo_api_url = url.replace("github.com", "api.github.com/repos")
            response = requests.get(repo_api_url, timeout=10)
            response.raise_for_status()
            repo_info = response.json()


            repo_name = repo_info.get('name', 'Unknown')
            repo_owner = repo_info.get('owner', {}).get('login', 'Unknown')
            repo_description = repo_info.get('description', 'No description')
            repo_language = repo_info.get('language', 'No language specified')
            repo_stars = repo_info.get('stargazers_count', 0)
            repo_forks = repo_info.get('forks_count', 0)
            repo_update_date = repo_info.get('updated_at', 'No update date')


            repo_info_content = (
                f"Repository Name: {repo_name}\n"
                f"Owner: {repo_owner}\n"
                f"Description: {repo_description}\n"
                f"Language: {repo_language}\n"
                f"Stars: {repo_stars}\n"
                f"Forks: {repo_forks}\n"
                f"Last Updated: {repo_update_date}\n"
            )


            repo_info_file_name = f"{repo_name}_repo_info.txt"
            with open(repo_info_file_name, 'w', encoding='utf-8') as file:
                file.write(repo_info_content)

            print(f"Repository information saved to {repo_info_file_name}")


            contents_api_url = f"{repo_api_url}/contents"
            response = requests.get(contents_api_url, timeout=10)
            response.raise_for_status()
            contents = response.json()


            local_dir = repo_name
            if not os.path.exists(local_dir):
                os.makedirs(local_dir)


            for content in contents:
                if content['type'] == 'file':
                    file_url = content['download_url']
                    file_path = os.path.join(local_dir, content['name'])
                    file_response = requests.get(file_url, timeout=10)
                    with open(file_path, 'wb') as file:
                        file.write(file_response.content)
                    print(f"Saved {content['name']} to {file_path}")

        except requests.RequestException as e:
            print(f"Failed to retrieve repository information for {url}: {e}")
        except Exception as e:
            print(f"Failed to parse repository information for {url}: {e}")
        input("Press Enter to return to the menu...")

    def get_file_hash(file_path):
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def virus_total_scan():
        import webbrowser
        import platform
        import os

        url = "https://www.virustotal.com/gui/home/upload"
        if platform.system() == "Windows":
            webbrowser.open(url)
        elif platform.system() == "Linux":
            if 'termux' in os.getenv('PREFIX', ''):
                os.system(f'termux-open-url {url}')
            else:
                webbrowser.open(url)
        else:
            webbrowser.open(url)
        input("Нажмите Enter для возвращения")


    def choose_file_from_directory():
        current_directory = os.getcwd()
        files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]
        if not files:
            print("В текущем каталоге не найдено файлов.")
            return None

        print("Файлы в текущем каталоге:")
        for idx, file in enumerate(files, 1):
            print(f"[{idx}] {file}")

        while True:
            try:
                choice = int(input("Введите номер файла для сканирования: "))
                if 1 <= choice <= len(files):
                    return os.path.join(current_directory, files[choice - 1])
                else:
                    print("Неверный выбор. Пожалуйста, введите номер из списка.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите корректное число.")

    def virus_total_check(api_key):
        print("Выберите опцию:")
        print("[1] Указать путь к файлу")
        print("[2] Выбрать файл из текущего каталога")

        choice = input("Введите ваш выбор: ").strip()

        if choice == '1':
            file_path = input("Введите полный путь к файлу: ").strip()
            if os.path.isfile(file_path):
                virus_total_scan(file_path, api_key)
            else:
                print("Неверный путь к файлу.")
        elif choice == '2':
            file_path = choose_file_from_directory()
            if file_path:
                virus_total_scan(file_path, api_key)
        else:
            print("Неверная опция. Пожалуйста, выберите '1' или '2'.")

        input("Нажмите Enter, чтобы вернуться в меню...")

    import qrcode

    def generate_qr_code():
        data = input("Enter the data to encode in the QR code: ")
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        file_path = "qrcode.png"
        img.save(file_path)
        print(f"QR code saved as {file_path}")
        input("Press Enter to return to the menu...")


    def check_internet_speed():
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        st.results.share()

        results = st.results.dict()
        print(f"Download speed: {results['download'] / 1_000_000:.2f} Mbps")
        print(f"Upload speed: {results['upload'] / 1_000_000:.2f} Mbps")
        print(f"Ping: {results['ping']} ms")
        input("Press Enter to return to the menu...")


    def main():

        while True:
            popi()
            clear_console()
            print(create_banner())
            print()
            print("Select a function (1-18) or 'q' to quit:")

            choice = input("Enter your choice: ").strip()

            if choice == 'q':
                break

            if choice == '1':
                domain = input("Enter domain for DNS lookup: ")
                dns_lookup(domain)
            elif choice == '2':
                domain = input("Enter domain for WHOIS lookup: ")
                whois_lookup(domain)
            elif choice == '3':
                ip = input("Enter IP for IP lookup: ")
                ip_lookup(ip)
            elif choice == '4':
                image_path = input("Enter path to image for metadata extraction: ")
                image_metadata(image_path)
            elif choice == '5':
                email = input("Enter email for data breach lookup: ")
                data_breach_lookup(email)
            elif choice == '6':
                ip = input("Enter IP for port scan: ")
                port_scan(ip)
            elif choice == '7':
                url = input("Enter URL for availability check: ")
                url_availability_check(url)
            elif choice == '8':
                url = input("Enter URL for SSL certificate check: ")
                ssl_certificate_check(url)
            elif choice == '9':
                url = input("Enter URL for HTTP headers extraction: ")
                http_headers_extraction(url)
            elif choice == '10':
                url = input("Enter URL for server response time check: ")
                server_response_time_check(url)
            elif choice == '11':
                url = input("Enter URL for HTML parsing: ")
                html_parser(url)
            elif choice == '12':
                repo_url = input("Enter GitHub repository URL: ")
                github_repo_parser(repo_url)
            elif choice == '13':
                print("Удалено")
                input("Нажмите Enter что бы вернуться назад")
            elif choice == '14':
                import webbrowser
                import platform
                import os

                url = "https://www.virustotal.com/gui/home/upload"
                if platform.system() == "Windows":
                    webbrowser.open(url)
                elif platform.system() == "Linux":
                    if 'termux' in os.getenv('PREFIX', ''):
                        os.system(f'termux-open-url {url}')
                    else:
                        webbrowser.open(url)
                else:
                    webbrowser.open(url)
                input("Нажмите Enter для возвращения")
            elif choice == '15':
                generate_qr_code()
            elif choice == '16':
                print("Удалено")
                input("Нажмите Enter что бы вернуться назад")
            elif choice == '17':
                check_internet_speed()
            elif choice == '18':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

            input("Press Enter to continue...")

    if __name__ == "__main__":
        main()
