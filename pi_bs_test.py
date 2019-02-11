from modules.pi_by_speed import *
from ev3dev import *
import math

pi = PI((2, 100), LargeMotor('outC'), 0)
pi.set_wanted_spd(10)

processing = True
while processing:
    pi.proc()
