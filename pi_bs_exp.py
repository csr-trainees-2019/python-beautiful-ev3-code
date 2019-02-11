from modules.pi_by_speed import *
from ev3dev import *
import math
import time

pi = PI((1.395, 210.25), LargeMotor('outC'), 0)
pi.set_wanted_spd(5.5)

processing = True
while processing:
    pi.proc()

    if time.time() - pi.launch_time >= 20:
        break

pi.reset()
