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

# Banner
os.system("figlet BY UNKNOW23 ")
print(Fore.RED + "="*50)
slow_print("[+] Initializing modules...")
time.sleep(0.5)
slow_print("[+] Bypassing Illegal Control...")
time.sleep(0.5)
slow_print("[+] Loading Chromium engine...")
time.sleep(0.5)
slow_print("[+] Preparing application mode...")
time.sleep(0.5)
print(Fore.RED + "="*50)

# Fake loading
for i in range(0, 101, 10):
    sys.stdout.write(Fore.CYAN + f"\r[+] Progress: {i}%")
    sys.stdout.flush()
    time.sleep(0.2)

print("\n" + Fore.GREEN + "[✓] Launching Osint application...")

# OPEN WEBSITE IN APP MODE
url = "https://breach2bz.com"
os.system(f"chromium --app={url} >/dev/null 2>&1 &")

slow_print("[✓] Done. Enjoy you hacking by UNKNOW23.", 0.05, Fore.BLUE)
