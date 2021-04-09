
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
picar.setup()

fw.offset = 10
pan_servo.offset = 10

fw.turn(90)
pan_servo.write(90)

