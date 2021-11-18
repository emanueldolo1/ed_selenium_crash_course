import time
import random

def get_timestamp():
    return int(time.time()) + random.randint(111, 999)
