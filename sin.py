from ev3dev.ev3 import *
from ev3dev.core import *
import time
import math

motor = LargeMotor('outC')
power = PowerSupply()

motor.reset()

def func(a, omega, t):
    return a * math.sin(omega * t)

a = power.measured_volts
omega = 10
file_handle = open('log.txt', 'w')
launch_time = time.time()
now = launch_time
volts = value / 100 * power.measured_volts
pos = motor.position / 180 * math.pi
file_handle.write(str(pos) + " " + str(volts) + " " + str(now - launch_time) + "\n")
while True:
    now = time.time()
    value = func(a, omega, now - launch_time) / a * 100
    motor.run_direct(duty_cycle_sp = value)
    volts = value / 100 * power.measured_volts
    pos = motor.position / 180 * math.pi
    file_handle.write(str(pos) + " " + str(volts) + " " + str(now - launch_time) + "\n")
    if now - launch_time >= 15:
        break

file_handle.close()
motor.stop(stop_action = 'brake')
