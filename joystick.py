from pyPS4Controller.controller import Controller
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar



class MyController(Controller):
    picar.setup()
    bw = back_wheels.Back_Wheels()
    fw = front_wheels.Front_Wheels()
    pan_servo = Servo.Servo(1)
    bw.speed = 0
    motor_speed = 60


    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        print("Hello world")

    def on_x_release(self):
        print("Goodbye world")
        self.bw.speed = 0

    def on_L3_up(self, value):
        speed = int((value/400)*-1)
        print("forward:" + str(speed))
        self.bw.speed = speed
        self.bw.backward()
    def on_L3_down(self, value):
        speed = int(value/400)
        print("backward:" + str(speed))
        self.bw.speed = speed
        self.bw.forward()
    def on_L3_left(self, value):
        print("value1:" + str(value))
        angleL = int((75-(-25/32767) * value))
        print("angle1:" + str(angleL))
        self.fw.turn(angleL)
    def on_L3_Right(self, value):
        print("value2:" + str(value))
        angleR = int(((60/32767) * value + 75))
        print("angle2:" + str(angleR))




controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)
