from modules.pi_by_speed_old import *
from ev3dev import *
import math
import time

pi = PI((0.0432639, 19.629823), LargeMotor('outC'), 12)

pi.set_wanted_spd(1)

processing = True
while processing:
    pi.proc()
    if time.time() - pi.launch_time >= 10:
        break

pi.reset()
