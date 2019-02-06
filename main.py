from pid import *
from ev3dev.ev3 import *

motor = LargeMotor('outA')
setup = (1, 0, 0)

pidA = PID(setup, motor)
pidA.set_wanted(500)

while True:
	pidA.proc()
