from pyPS4Controller.controller import Controller
from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar



class MyController(Controller):
    picar.setup()
    bw = back_wheels.Back_Wheels()
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
         print("Forward!")
         self.bw.speed = self.motor_speed
         self.bw.forward()

controller = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
# you can start listening before controller is paired, as long as you pair it within the timeout window
controller.listen(timeout=60)