from datetime import date
import time
import os

class Node:
    """ An object <Node> is a PrintNode.exe app
    """
    state = 'offline' # PrintNode app state

    def __init__(self, name: str, path: str):
        self.name = name # name of the PrintNode
        self.path = path # path to the PrintNode dir

    def check_state(self, path: str) -> str:
        """ Such check fits to the situations when PrintNode app gets stuck or just turns off

        Logs of the PrintNode app writes all the time, so the size of the logfile is always gets bigger
        """
        today = day_log()
        try:
            filepath = path + '\\logs\\' + today + '.txt' # path to the log of the current day
            size1 = get_size(filepath) # size of the logfile 
            time.sleep(5)
            size2 = get_size(filepath) # size of the logfile after 5 secs
            if size1 == size2:
                state = 'offline' # state of the PrintNode app
            else:
                state = 'online'
        except FileNotFoundError: # if there is no logfile for today - node state is offline automatically
            state = 'offline'
        return state


def two_symbols(n: int) -> str:
    # a function helps to format date
    if len(str(n)) == 1:
        n = '0' + str(n)
    return n

def day_log() -> str:
    # formated date
    today = date.today()
    log_of_the_day = ('%s-%s-%s'% (two_symbols(today.day), two_symbols(today.month), str(today.year)))
    return log_of_the_day

def get_size(filepath: str) -> int:
    # size of the log file
    size = os.path.getsize(filepath)
    return size