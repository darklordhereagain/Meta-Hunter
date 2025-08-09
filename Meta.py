import os
import sys
import time
import random
import platform
import importlib.util

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def type_line(text, delay=0.02, end="\n"):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def matrix_rain(duration=2):
    chars = "01░▒▓█▌▐▍▊▎▕⎺⎽⎼⎻⎯⎾⎿"
    end_time = time.time() + duration
    while time.time() < end_time:
        line = ''.join(random.choice(chars) for _ in range(70))
        print(f"\033[1;32m{line}\033[0m")
        time.sleep(0.03)

def show_fbi_warning():
    clear()
    warning = """
\033[1;31m
███████╗██████╗ ██╗    ██╗    ██╗    ██╗ ██████╗ ██████╗ ██╗███╗   ██╗ ██████╗ 
██╔════╝██╔══██╗██║    ██║    ██║    ██║██╔═══██╗██╔══██╗██║████╗  ██║██╔════╝ 
█████╗  ██████╔╝██║ █╗ ██║    ██║ █╗ ██║██║   ██║██████╔╝██║██╔██╗ ██║██║  ███╗
██╔══╝  ██╔═══╝ ██║███╗██║    ██║███╗██║██║   ██║██╔══██╗██║██║╚██╗██║██║   ██║
███████╗██║     ╚███╔███╔╝    ╚███╔███╔╝╚██████╔╝██║  ██║██║██║ ╚████║╚██████╔╝
╚══════╝╚═╝      ╚══╝╚══╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                             
       WARNING! UNAUTHORIZED ACCESS TO THIS SYSTEM IS PROHIBITED.
        This system is monitored by the FBI and cyber division.
          Violators will be prosecuted to the full extent.
\033[0m
"""
    print(warning)
    time.sleep(3)

def fake_root_login():
    print("\033[1;34m[~] Attempting root access...\033[0m")
    time.sleep(0.1)
    fake_passwords = [
        "root", "admin123", "toor", "pass@123", "hunter2", "letmein", "shadow", "123456", "nasa007"
    ]
    for pwd in fake_passwords:
        type_line(f"\033[1;31m[!] root@localhost:~$ su\nPassword: {pwd} - ACCESS DENIED\033[0m", 0.01)
        time.sleep(0.1)
    print("\033[1;32m[+] Access token brute-forced successfully!\033[0m")
    time.sleep(0.2)

def hollywood_logs():
    logs = [
        "[+] Bypassing secure bootloader...",
        "[+] Spoofing biometric data...",
        "[+] Injecting malware into virtual memory...",
        "[+] Overriding DNS cache...",
        "[+] Locating encryption key vault...",
        "[+] Dumping crypto wallet...",
        "[+] Extracting passwords..."
    ]
    for log in logs:
        type_line(f"\033[1;32m{log}\033[0m", 0.015)
        time.sleep(0.1)

def hollywood_banner():
    print("\n\033[1;32m")
    print("█░█ █▀█ █▄▀ █ █░░ █░█ █▀ ▀█▀")
    print("█▄█ █▄█ █░█ █ █▄▄ █▄█ ▄█ ░█░")
    print("    H O L L Y W O O D   H A C K E R")
    print("\033[0m")

def get_arch():
    machine = platform.machine()
    if machine in ["aarch64", "arm64"]: return "64"
    elif machine in ["armv7l", "armeabi", "arm"]: return "32"
    else:
        print(f"\033[1;31mUnsupported arch: {machine}\033[0m")
        sys.exit(1)

def load_module(arch):
    so_file = f"final_{arch}.cpython-312.so"
    if not os.path.exists(so_file):
        print(f"\033[1;31m[-] Encrypted module '{so_file}' not found.\033[0m")
        return

    type_line(f"\033[1;34m[~] Loading encrypted module: {so_file}\033[0m", 0.02)
    time.sleep(0.5)

    try:
        spec = importlib.util.spec_from_file_location("final", so_file)
        final = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(final)
        print("\033[1;32m[+] Module executed.\033[0m")
        if hasattr(final, 'main'):
            final.main()
        else:
            print("\033[1;31m[-] No main() found.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[0m")

if __name__ == "__main__":
    clear()
    show_fbi_warning()
    matrix_rain()
    hollywood_banner()
    fake_root_login()
    hollywood_logs()
    arch = get_arch()
    load_module(arch)
