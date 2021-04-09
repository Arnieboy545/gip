
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar

    pan_servo = Servo.Servo(1)
    picar.setup()

    fw.offset = 0
    pan_servo.offset = 10

    fw.turn(45)
    pan_servo.write(45)

