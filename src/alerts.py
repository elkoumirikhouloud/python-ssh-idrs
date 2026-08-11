import time

from config import ALERT_LOG_FILE


def alert_bruteforce(ip, username, attempts):

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
-----------------------------------------
[BRUTE FORCE DETECTED]
-----------------------------------------
Time: {current_time}
IP Address: {ip}
Username: {username}
Failed Attempts: {attempts}
-----------------------------------------
"""

    print(message)

    with open(ALERT_LOG_FILE, "a") as file:
        file.write(message)


def alert_enumeration(ip, usernames):

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
------------------------------------------------
[USERNAME ENUMERATION DETECTED]
------------------------------------------------
Time: {current_time}
IP Address: {ip}
Usernames Tried: {", ".join(sorted(usernames))}
Total Usernames: {len(usernames)}
------------------------------------------------
"""

    print(message)

    with open(ALERT_LOG_FILE, "a") as file:
        file.write(message) 

def alert_time_restriction(ip, username, hour):

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    message = f"""
-----------------------------------------------------------------------
[TIME-BASED SSH ACCESS VIOLATION]
-----------------------------------------------------------------------
Time: {current_time}
Authentication Hour: {hour}:00
IP Address: {ip}
Username: {username}

SSH authentication attempt detected outside the allowed access period.
-----------------------------------------------------------------------
"""

    print(message)

    with open(ALERT_LOG_FILE, "a") as file:
        file.write(message)
