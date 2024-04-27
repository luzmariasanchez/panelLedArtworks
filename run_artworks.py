import datetime
import os

current_date = datetime.datetime.now()


day_week = current_date.weekday()


days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
current_day = days[day_week]

if current_day == days[1] or current_day == days[3] or current_day == days[5]:
    print("Hoy es par")
    os.system("sudo python3 /home/pi/detritus/detritus.py")
elif current_day == days[2] or current_day == days[4] or current_day == days[6]:
    print("Hoy es inpar")
    os.system("python3 /home/pi/flag/flag.py")
    