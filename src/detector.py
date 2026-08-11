from collections import defaultdict

from config import (
    FAILED_ATTEMPT_THRESHOLD,
    USERNAME_ENUMERATION_THRESHOLD,
    SSH_START_HOUR,
    SSH_END_HOUR
)

from alerts import (
    alert_bruteforce,
    alert_enumeration,
    alert_time_restriction
)

from response import block_ip


class Detector:

    def __init__(self):

        self.failed_attempts = defaultdict(int)

        self.enumerated_users = defaultdict(set)

    def process_attempt(self, attempt):

        ip = attempt["ip"]
        username = attempt["username"]
        hour = attempt["hour"]
        attempt_type = attempt["type"]

        should_block = False

        

        if hour < SSH_START_HOUR or hour >= SSH_END_HOUR:

            alert_time_restriction(
                ip,
                username,
                hour
            )

            should_block = True

        
        if attempt_type == "bruteforce":

            self.failed_attempts[ip] += 1

            if self.failed_attempts[ip] >= FAILED_ATTEMPT_THRESHOLD:

                alert_bruteforce(
                    ip,
                    username,
                    self.failed_attempts[ip]
                )

                should_block = True

                self.failed_attempts[ip] = 0


        elif attempt_type == "enumeration":

            self.enumerated_users[ip].add(username)

            if len(self.enumerated_users[ip]) >= USERNAME_ENUMERATION_THRESHOLD:

                alert_enumeration(
                    ip,
                    self.enumerated_users[ip]
                )

                should_block = True

                self.enumerated_users[ip].clear()


        if should_block:

            block_ip(ip)
