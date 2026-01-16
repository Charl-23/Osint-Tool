import os
import sys
import time
from colorama import Fore, Style, init

init(autoreset=True)

def slow_print(text, speed=0.03, color=Fore.GREEN):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

os.system("clear")


os.system("figlet BY UNKNOW23 ")
print(Fore.RED + "="*50)
slow_print("[+] Take a human verification...")
time.sleep(0.5)
slow_print("[+] ignore the proceed (the phishing is not real)...")
time.sleep(0.5)
slow_print("[+] Create an account...")
time.sleep(0.5)
slow_print("[+] And enjoy your Osint activities...")
time.sleep(0.5)
slow_print("[+] And if you can follow and like my project and my github it's cool !")
time.sleep(0.5)
print(Fore.RED + "="*50)
