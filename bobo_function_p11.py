
from datetime import datetime



def timer(t, start, finished):
    t_start = datetime.now()
    if start:
        start()
    while True:
        t_end = datetime.now()
        dalta_t = t_end - t_start
        if dalta_t.seconds >= t:
            break
    if finished:
        finished()

def s():
    print("start:..")

def f():
    print('end:...')

timer(3 , None, f)