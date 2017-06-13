#This file should be on your raspberry Pi

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


def check_distance():
    # setting GPIO pins
    TRIG = 38
    ECHO = 40

    # assign pin roles
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    # sets TRIG/ECHO to false. gives time for sensor to settle
    echo_state = 0
    GPIO.output(TRIG, False)
    time.sleep(0.5)

    # send sonic beam
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # starts time when no input
    while echo_state == 0:
        echo_state = GPIO.input(ECHO)
        pulse_start = time.time()

    # stops time when gets input
    while GPIO.input(ECHO) == 1:
        pass
    pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # calculates distance in cm
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    average = distance - 0.5
    if distance > 2 and distance < 400:
        print("Distance:", average, 'cm')
    else:
        print('out of range')
    return average
