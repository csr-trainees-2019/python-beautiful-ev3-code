from pid import *

motor = LargeMotor('outA')
setup = (20 / 180 * 3.14, 35 / 180 * 3.14, 0)

pidA = PID(setup, motor)
pidA.set_wanted_deg(500)

while True:
	pidA.proc()
