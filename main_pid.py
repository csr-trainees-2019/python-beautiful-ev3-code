import time
import math
from ev3dev.ev3 import *

def cut_abs(value, max):
    return max * math.copysign(1, value) if abs(value) > max else value

motor = LargeMotor('outA')
motor.reset()

(kp, ki, kd) = (20 / 180 * 3.14, 35 / 180 * 3.14, 0)
(err_p, err_i, err_d) = (0, 0, 0)
state = {'last': 0, 'now': 0, 'wanted': 500}

upd_spd = 0.01
last_time = time.time()
windup = 0
operating = True

while operating:
    dt = (time.time() - last_time) / 1000
    last_time = time.time()
    err_p = state['wanted'] - state['now']
    err_d = (err_p - (state['wanted'] - state['last'])) / dt
    if windup != 0:
        err_i = err_i if abs(err_i) < windup else math.copysign(1, err_i) * windup
    err_i += err_p * dt
    new_state = motor.position
    (state['last'], state['now']) = (state['now'], new_state)
    Ut = kp * err_p + ki * err_i + kd * err_d
    value = cut_abs(Ut, 100)
    motor.run_direct(duty_cycle_sp = value)
    time.sleep(upd_spd);
    # expression for setting operation
    # to break the cycle

motor.stop(stop_action = 'brake')
