import subprocess
import time

from config import BLOCK_DURATION


def block_ip(ip):

    print(f"Blocking IP {ip} for {BLOCK_DURATION} seconds")

    subprocess.run([
        "sudo",
        "iptables",
        "-I",
        "INPUT",
        "-s",
        ip,
        "-j",
        "DROP"
    ])

    time.sleep(BLOCK_DURATION)

    print(f"Unblocking IP {ip}")

    subprocess.run([
        "sudo",
        "iptables",
        "-D",
        "INPUT",
        "-s",
        ip,
        "-j",
        "DROP"
    ])
