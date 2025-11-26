# alarm set as "para.mp3"

from playsound import playsound
import time

CLEAR = "\033[2J"
CLEAR_COMEBACK = "\033[H"

def alarm(seconds):
    time_passed = 0
    print(CLEAR)
    while time_passed < seconds:
        time.sleep(1)
        time_passed += 1
        
        hours_left = ((seconds - time_passed) // 60) // 60
        minutes_left = ((seconds - time_passed) // 60) % 60
        seconds_left = (seconds - time_passed) % 60
        print(f"{CLEAR_COMEBACK}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}", end="")
    playsound.playsound("para.mp3")

while True:
    n = input("Set your timer (format -> Hours[<99]:Minutes[<60]:Seconds[<60]): ")
    hours, minutes, seconds = n.split(":")
    if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        if hours < 99 and minutes < 60 and seconds < 60:
            seconds += minutes * 60 + hours * 3600
            alarm(seconds)
    else:
        print("Wrong format. Please try again.\n")