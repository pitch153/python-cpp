import datetime
from playsound import playsound

def set_alarm(alarm_time):
    while True:
        time_now = datetime.datetime.now().strftime('%H:%M:%S')
        if time_now == alarm_time:
            print('Time to wake up!')
            playsound('alarm_sound.mp3') # replace 'alarm_sound.mp3' with the filename of your alarm sound
            break

alarm_time = input('Enter the time to set the alarm (in HH:MM:SS format): ')
set_alarm(alarm_time)
