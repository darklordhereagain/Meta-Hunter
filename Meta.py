import os
import sys
import platform
import importlib.util
import time
import traceback
import random

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def matrix_intro(lines=18, delay=0.03):
    chars = "⣿⠿⣾⣷⡿⢿⣿⡇⠁⠂⠒⠛⠓⠒⠂⠄⠅⠆⠤⠶⠿"
    for _ in range(lines):
        line = "".join(random.choice(chars) for _ in range(70))
        print(f"\033[1;32m{line}\033[0m")
        time.sleep(delay)

def banner():
    clear_screen()
    matrix_intro()

    print("\033[1;36m")
    print("╔═════════════════════════════════════╗")
    print("║ ███╗░░░███╗███████╗████████╗░█████╗░ ║")
    print("║ ████╗░████║██╔════╝╚══██╔══╝██╔══██╗ ║")
    print("║ ██╔████╔██║█████╗░░░░░██║░░░███████║ ║")
    print("║ ██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║ ║")
    print("║ ██║░╚═╝░██║███████╗░░░██║░░░██║░░██║ ║")
    print("║ ╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝ ║")
    print("║           🚀 META HUNTER                            ║")
    print("╚═════════════════════════════════════╝")
    print("\033[0m")
    time.sleep(0.5)
    fake_ai_loading()

def fake_ai_loading():
    steps = [
        "🧠 Initializing memory modules",
        "🔍 Scanning device architecture",
        "📦 Preparing encrypted payload",
        "⚡ Injecting core",
        "🔐 Securing runtime environment",
        "🧬 Launching main process"
    ]
    for step in steps:
        loading_anim(step, delay=0.07)

def get_architecture():
    arch = platform.machine()
    if arch in ["aarch64", "arm64"]:
        return "64"
    elif arch in ["armv7l", "armeabi", "arm"]:
        return "32"
    else:
        print(f"❌ Unsupported architecture: {arch}")
        sys.exit(1)

def load_cython_module(arch):
    so_file = f"final_{arch}.cpython-312.so"

    if not os.path.exists(so_file):
        print(f"❌ Required file {so_file} not found.")
        sys.exit(1)

    print(f"\n📁 Encrypted Core Module: \033[1;33m{so_file}\033[0m")
    loading_anim("☣️ Injecting secure module", delay=0.1)

    try:
        spec = importlib.util.spec_from_file_location("final", so_file)
        final = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(final)

        print("\n✅ Module loaded successfully.")
        time.sleep(0.5)
        if hasattr(final, 'main'):
            print("🚀 Running main()...\n")
            time.sleep(0.5)
            final.main()
        else:
            print("❌ main() function not found in module.")
    except Exception as e:
        print(f"❌ Failed to load module: {e}")
        traceback.print_exc()
        sys.exit(1)

def loading_anim(message, delay=0.1):
    print(message, end="", flush=True)
    for _ in range(10):
        time.sleep(delay)
        print(".", end="", flush=True)
    print(" ✔️")

if __name__ == "__main__":
    banner()
    arch = get_architecture()
    load_cython_module(arch)
