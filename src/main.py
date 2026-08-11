import time

from parser import parse_logs
from detector import Detector


detector = Detector()

processed = len(parse_logs())

print("Starting Log Defense System...")


while True:

    attempts = parse_logs()

    new_attempts = attempts[processed:]

    for attempt in new_attempts:

        detector.process_attempt(attempt)

    processed = len(attempts)

    time.sleep(2)
