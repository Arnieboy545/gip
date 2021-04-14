
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep
import cv2
import numpy as np
import picar
import os

fw = front_wheels.Front_Wheels()
pan_servo = Servo.Servo(1)
num1 = 0
picar.setup()

fw.offset = 0
pan_servo.offset = 0
while num1 < 190:
    num1 = int(input())
    fw.turn(num1)
    pan_servo.write(0)

