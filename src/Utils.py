import sys
import time

def slow_print(text, interval=0.001):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(interval)
    print ()