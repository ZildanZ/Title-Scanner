import requests
from bs4 import BeautifulSoup
import colorama
from colorama import Fore, Style
import pyfiglet

def print_header():
    colorama.init(autoreset=True)
    title_text = pyfiglet.figlet_format("Title Scanner")
    author_text = "Dibuat oleh Zildan"
    
    print(Fore.CYAN + title_text)
    print(Fore.GREEN + author_text + "\n")
    print(Style.RESET_ALL)

print_header()
def scan_titles(websites):
    for website in websites:
        try:
            response = requests.get(website)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string.strip() if soup.title else 'Title not found'
            print(f"Website: {website}\nTitle: {title}\n")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while scanning {website}: {e}\n")

def read_website_list():
    file_path = input("Masukkan path file .txt yang berisi daftar website: ")
    with open(file_path, 'r') as file:
        websites = file.readlines()

    websites = [website.strip() for website in websites]
    return websites

websites = read_website_list()
scan_titles(websites)