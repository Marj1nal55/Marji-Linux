#!/usr/bin/env python3
import os
import platform
import shutil

def get_distro_name():
    """/etc/os-release içinden PRETTY_NAME değerini döndürür."""
    with open("/etc/os-release") as f:
         for line in f:
             if line.startswith("PRETTY_NAME="):
                 return line.split("=", 1)[1].strip('"\n')
    return None

def get_system_info():
    total, used, free = shutil.disk_usage("/")
    cpu = os.cpu_count() or "unknown"

    return {
        "Distro": get_distro_name() or "Unknown",
        "Kernel": platform.release(),
        "Arch": platform.machine(),
        "CPU": cpu,
        "Disk": f"{free // (1024 ** 3)} GB free",
        "Python": platform.python_version(),
    }

def show_info():
    os.system("clear")
    info = get_system_info()

    rows = list(info.items())
    width = max(len(str(v)) for _, v in rows) + 10

    print("╔" + "═" * width + "╗")
    print("║" + "MARJI-LINUX".center(width) + "║")
    print("╠" + "═" * width + "╣")

    for name, value in rows:
        line = f"{name}: {value}"
        print("║ " + line.ljust(width - 1) + "║")

    print("╚" + "═" * width + "╝")

if __name__ == "__main__":
    show_info()
