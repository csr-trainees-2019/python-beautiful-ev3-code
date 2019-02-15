from modules.pi_by_speed_old import *
from ev3dev import *
import math
import time

pi = PI((8.5720833, 706.67361), LargeMotor('outC'), 0)
pi.set_wanted_spd(1)

processing = True
while processing:
    pi.proc()
    if time.time() - pi.launch_time >= 10:
        break

pi.reset()
