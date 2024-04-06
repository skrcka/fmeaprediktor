from time import time


def get_timestamp_ms():
    return round(time() * 1000)
