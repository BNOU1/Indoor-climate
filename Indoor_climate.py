# First check temperature

import os
import time

def measure_temp():
    temp = os.open("cat /sys/class/thermal/thermal_zone0/temp").readline()
    return (float(temp)/1000)

while True:
    tm = measure_temp()
    f = open("/var/www/html/temp.txt", "w")
    f.write(str(tm) + '\n')
    print(tm)
    time.sleep(1)

