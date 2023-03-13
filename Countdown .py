import time

def countdown(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up!")

def timer(seconds):
    start_time = time.time()
    elapsed_time = 0
    while elapsed_time < seconds:
        mins, secs = divmod(int(seconds - elapsed_time), 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        elapsed_time = time.time() - start_time
    print("Time's up!")

countdown(60) # countdown for 60 seconds
timer(60) # timer for 60 seconds
