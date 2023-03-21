#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

RoAPin = 11
RoBPin = 12
BtnPin = 13
ServoPin = 7

globalCounter = 0
flag = 0
Last_RoB_Status = 0
Current_RoB_Status = 0

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(RoAPin, GPIO.IN)
    GPIO.setup(RoBPin, GPIO.IN)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ServoPin, GPIO.OUT)

    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=btnISR)

def set_servo_position(globalCounter):
    pwm = GPIO.PWM(ServoPin, 50)
    pwm.start(7.5)
    position = 7.5 + (globalCounter * 0.1)
    if position < 0:
        position = 0
    if position > 180:
        position = 180
    pwm.ChangeDutyCycle(position)
    time.sleep(0.01)

def rotaryDeal():
    global flag, Last_RoB_Status, Current_RoB_Status, globalCounter
    Last_RoB_Status = GPIO.input(RoBPin)
    while (not GPIO.input(RoAPin)):
        Current_RoB_Status = GPIO.input(RoBPin)
        flag = 1
    if flag == 1:
        flag = 0
        if (Last_RoB_Status == 0) and (Current_RoB_Status == 1):
            globalCounter = globalCounter - 1
        if (Last_RoB_Status == 1) and (Current_RoB_Status == 0):
            globalCounter = globalCounter + 1

def btnISR(channel):
    global globalCounter
    globalCounter = 0

def loop():
    global globalCounter
    tmp = 0

    while True:
        rotaryDeal()
        if tmp != globalCounter:
            print('globalCounter = %d' % globalCounter)
            set_servo_position(globalCounter)
            tmp = globalCounter

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
