from ev3dev.ev3 import *
from ev3dev.core import *
import time
import math

motor = LargeMotor('outC')
power = PowerSupply()

motor.reset()

def func(a, omega, t):
    return a * math.sin(omega * t)


exp_w = [1, 1, 1, 2, 2, 5]
exp_v = [100, 50, 25, 100, 50, 100]

for i in range(6):

    omega = exp_w[i]
    a = exp_v[i] / 100 * power.measured_volts
    file_handle = open('log' + str(i + 1) + '.txt', 'w')
    launch_time = time.time()
    motor.reset()

    while True:
        now = time.time()
        value = func(a, omega, now - launch_time) / power.measured_volts * 100
        motor.run_direct(duty_cycle_sp = value)
        volts = value / 100 * power.measured_volts
        pos = motor.position / 180 * math.pi
        file_handle.write(str(pos) + " " + str(volts) + " " + str(now - launch_time) + "\n")
        if now - launch_time >= 10:
            break

    file_handle.close()
    motor.stop(stop_action = 'brake')

    time.sleep(2)

exp2_v = [100, 50, 25, -50, -100, 69]

for j in range(6):
    launch_time = time.time()

    file_handle = open('log' + str(j + 7) + '.txt', 'w')
    motor.reset()

    while True:
        now = time.time()
        value = exp2_v[j]
        motor.run_direct(duty_cycle_sp = value)
        volts = value / 100 * power.measured_volts
        pos = motor.position / 180 * math.pi
        file_handle.write(str(pos) + " " + str(volts) + " " + str(now - launch_time) + "\n")
        if now - launch_time >= 5:
            break

    file_handle.close()
    motor.stop(stop_action = 'brake')

    time.sleep(2)
