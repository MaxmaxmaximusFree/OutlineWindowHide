import pygetwindow as gw
import threading
from threading import Timer

# SETTINGS
TRY_TO_HIDE_INTERVAL = 0.1 #sec
PROGRAM_TIME_LIVE = 10 #sec


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.daemon = True
    t.start()
    return t

def set_timeout(func, sec):
    t = Timer(sec, func)
    t.start()
    return t



def minimize_outline():
    windows = gw.getAllWindows()
    print('Try to minimize Outline')

    for window in windows:
        if window.title == 'Outline':
            print('Minimize Outline')
            window.close()
    return


interval = set_interval(minimize_outline, TRY_TO_HIDE_INTERVAL)
def func():
    print('EXIT')
    exit()

set_timeout(func, PROGRAM_TIME_LIVE)


