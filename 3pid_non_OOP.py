CCimport time
import math
from ev3dev.ev3 import *

def cut_abs(value, max):
    return max * math.copysign(1, value) if abs(value) > max else value

motor_A = LargeMotor('outA')
motor_B = LargeMotor('outB')
motor_C = LargeMotor('outC')
motor_A.reset()
motor_B.reset()
motor_C.reset()

(kp_A, ki_A, kd_A) = (20, 35, 0)
(err_p_A, err_i_A, err_d_A) = (0, 0, 0)
state_A = {'last': 0, 'now': 0, 'wanted': 50}
windup_A = 0

(kp_B, ki_B, kd_B) = (20, 35, 0)
(err_p_B, err_i_B, err_d_B) = (0, 0, 0)
state_B = {'last': 0, 'now': 0, 'wanted': 50}
windup_B = 0

(kp_C, ki_C, kd_C) = (20, 35, 0)
(err_p_C, err_i_C, err_d_C) = (0, 0, 0)
state_C = {'last': 0, 'now': 0, 'wanted': 50}

windup_C = 0

last_time = time.time()
upd_spd = 0.01
operating = True

def set_assembly_state(wanted_for_A, wanted_for_B, wanted_for_C):
    stateA['wanted'] = wanted_for_A
    stateB['wanted'] = wanted_for_B
    stateC['wanted'] = wanted_for_C

while operating:
    dt = (time.time() - last_time) / 1000
    last_time = time.time()

    new_state_A = motor_A.position / 180 * math.pi
    new_state_B = motor_B.position / 180 * math.pi
    new_state_C = motor_C.position / 180 * math.pi

    err_p_A = state_A['wanted'] - state_A['now']
    err_d_A = (err_p_A - (state_A['wanted'] - state_A['last'])) / dt
    if windup_A != 0:
        err_i_A = err_i_A if abs(err_i_A) < windup_A else math.copysign(1, err_i_A) * windup_A
    err_i_A += err_p_A * dt
    (state_A['last'], state_A['now']) = (state_A['now'], new_state_A)
    Ut_A = kp_A * err_p_A + ki_A * err_i_A + kd_A * err_d_A
    value_A = cut_abs(Ut_A, 100)

    err_p_B = state_B['wanted'] - state_B['now']
    err_d_B = (err_p_B - (state_B['wanted'] - state_B['last'])) / dt
    if windup_B != 0:
        err_i_B = err_i_B if abs(err_i_B) < windup_B else math.copysign(1, err_i_B) * windup_B
    err_i_B += err_p_B * dt
    (state_B['last'], state_B['now']) = (state_B['now'], new_state_B)
    Ut_B = kp_B * err_p_B + ki_B * err_i_B + kd_B * err_d_B
    value_B = cut_abs(Ut_B, 100)

    err_p_C = state_C['wanted'] - state_C['now']
    err_d_C = (err_p_C - (state_C['wanted'] - state_C['last'])) / dt
    if windup_C != 0:
        err_i_C = err_i_C if abs(err_i_C) < windup_C else math.copysign(1, err_i_C) * windup_C
    err_i_C += err_p_C * dt
    (state_C['last'], state_C['now']) = (state_C['now'], new_state_C)
    Ut_C = kp_C * err_p_C + ki_C * err_i_C + kd_C * err_d_C
    value_C = cut_abs(Ut_C, 100)

    motor_A.run_direct(duty_cycle_sp = value_A)
    motor_B.run_direct(duty_cycle_sp = value_B)
    motor_C.run_direct(duty_cycle_sp = value_C)


    time.sleep(upd_spd);
    # expression for setting operation
    # to break the cycle

motorA.stop(stop_action = 'brake')
motorB.stop(stop_action = 'brake')
motorC.stop(stop_action = 'brake')
