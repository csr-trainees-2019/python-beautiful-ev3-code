from pid import *

motor = LargeMotor('outA')
setup = (20, 35, 0)

pidA = PID(setup, motor)
pidA.set_wanted_rad(50)

while True:
	pidA.proc()
