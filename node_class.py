from datetime import date
import time
import os

class Node:

    state = 'offline'

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def check_state(self, path):
        r = two_symbols(2)
        print(r)
        today = day_log()
        filepath = path + '\\logs\\' + today + '.txt'
        size1 = get_size(filepath)
        time.sleep(5)
        size2 = get_size(filepath)
        if size1 == size2:
            state = 'offline'
        else:
            state = 'online'
        return state


def two_symbols(n):
    if len(str(n)) == 1:
        n = '0' + str(n)
    return n

def day_log():
    today = date.today()
    log_of_the_day = ('%s-%s-%s'% (two_symbols(today.day), two_symbols(today.month), str(today.year)))
    print(log_of_the_day)
    return log_of_the_day

def get_size(filepath):
    size = os.path.getsize(filepath)
    print(size)
    return size