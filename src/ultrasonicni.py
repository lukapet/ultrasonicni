__author__ = 'Luka'

import RPi.GPIO as GPIO
import time

us_trig = 28
us_echo = 30
distance_opt = 15.5

# proemniti pinove
segments = {'a': 26, 'b': 22, 'c': 15, 'd': 11,
            'e': 7, 'f': 24, 'g': 13}

digits = [19, 21, 23, 18]

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(us_trig, GPIO.OUT)
GPIO.setup(us_echo, GPIO.IN)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)  # We put segments output in zero

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)  # We put digit output in zero


def prikazi(distance):
    num = {' ': [],
           '0': ['a', 'b', 'c', 'd', 'e', 'f'],
           '1': ['b', 'c', 'd'],
           '2': ['a', 'b', 'd', 'e', 'g'],
           '3': ['a', 'b', 'c', 'd', 'e', 'g'],
           '4': ['b', 'c', 'f', 'g'],
           '5': ['a', 'c', 'd', 'f', 'g'],
           '6': ['a', 'c', 'd', 'e', 'f', 'g'],
           '7': ['a', 'b', 'c'],
           '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
           '9': ['a', 'b', 'c', 'd', 'f', 'g']}


    s = str(distance).rjust(4)

    for digit in range(4):
        GPIO.output(digit, 0)  # Turn on the digit

        digitSegments = num[s[digit]]
        for segment in digitSegments:
            GPIO.output(segments[segment], 1)  # Turn on segments

        time.sleep(2)

        GPIO.output(digit, 1)  # Turn off the digit
        for segment in digitSegments:
            GPIO.output(segments[segment], 0)  # Turn off segments


def pisi(poruka):


def izmeri():
    GPIO.output(us_trig, 0)
    time.sleep(0.5)

    GPIO.output(us_trig, 1)
    time.sleep(0.00001)

    while GPIO.input(us_echo) == 0:
        start = time.time()

    while GPIO.input(us_echo) == 1:
        stop = time.time()

    elapsed = stop - start
    distance = elapsed * 17150
    distance = round(distance, 0)
    return distance


def main():
    while True:
        distance = izmeri()
        prikazi(distance)
        if (distance == distance_opt):
            poruka = 1
        else:
            poruka = 0
        pisi(poruka)
