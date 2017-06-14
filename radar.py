# This file should be on Your raspberry PI

import RPi.GPIO as GPIO
import time
import numpy as np

from distance import check_distance
from database import data_entry, create_table

# sets up GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
p = GPIO.PWM(12, 50)

# defines robot starting position and gives 0.5s for robot to achieve it
p.start(2.5)
time.sleep(0.5)

create_table()

cycle = []
# provides range of motion. In this case its 180 degrees
vision = np.arange(2.5, 12.5, 0.5)


try:
    while True:
        # gives sensor time to settle
        time.sleep(0.5)
        print(cycle)
        for i in vision:
            time.sleep(0.01)
            # moves robot
            p.ChangeDutyCycle(i)
            # takes measurement
            average = check_distance()
            # populates cycle list with measurement
            cycle.append(average)
        # saves full cycle to database
        data_entry(cycle)
        # clears cycle for new loop
        cycle = []

except KeyboardInterrupt:

    p.stop()
    GPIO.cleanup()
