import re

from config import LOG_FILE


def parse_logs():

    attempts = []

    with open(LOG_FILE, "r") as file:

        for line in file:

            if "sshd" not in line:
                continue


            time_match = re.search(
                r"T(\d{2}):(\d{2}):(\d{2})",
                line
            )

            if not time_match:
                continue

            hour = int(time_match.group(1))


            ip_match = re.search(
                r"from (\d{1,3}(?:\.\d{1,3}){3})",
                line
            )

            if not ip_match:
                continue

            ip = ip_match.group(1)


            if "Failed password for " in line and "invalid user" not in line:

                user_match = re.search(
                    r"Failed password for ([^\s]+)",
                    line
                )

                if user_match:

                    attempts.append({

                        "type": "bruteforce",

                        "hour": hour,

                        "ip": ip,

                        "username": user_match.group(1)

                    })


            elif "Invalid user" in line:

                user_match = re.search(
                    r"Invalid user ([^\s]+)",
                    line
                )

                if user_match:

                    attempts.append({

                        "type": "enumeration",

                        "hour": hour,

                        "ip": ip,

                        "username": user_match.group(1)

                    })


            elif "Accepted password for " in line:

                user_match = re.search(
                    r"Accepted password for ([^\s]+)",
                    line
                )

                if user_match:

                    attempts.append({

                        "type": "login",

                        "hour": hour,

                        "ip": ip,

                        "username": user_match.group(1)

                    })

    return attempts
