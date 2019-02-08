from ev3dev.ev3 import *
import time
import math

motor = LargeMotor('outA')

# A*sin(wt)

def func(a, omega, t):
    return a * math.sin(omega * t)

a = 0
omega = 0
ltime = time.time()

while True:
    ltime = time.time() - ltime
    value = func(a, omega, ltime)
    motor.run_direct(duty_cycle_sp = value)
