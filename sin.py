from ev3dev.ev3 import *
from ev3dev.core import *
import time
import math

motor = LargeMotor('outA')
power = PowerSupply()

# A*sin(wt)

def func(a, omega, t):
    return a * math.sin(omega * t)

a = 0
omega = 0
launch_time = time.time()

#t [s] mp [rad] voltage [volts]

file_handle = open('log.txt', 'w')

while True:
    time = time.time()
    if time - launch_time >= 15:
        break
    value = func(a, omega, time - launch_time)
    motor.run_direct(duty_cycle_sp = value)
    volts = value / 100 * power.measured_volts
    pos = motor.position / 180 * math.pi
    file_handle.write(str(time) + " " + str(pos) + " " + str(volts) + "\n")

file.close()
