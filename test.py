from modules.pid import *

motor = LargeMotor('outA')
setup = (20, 35, 0)

pidA = PID(setup, motor)
pidA.set_wanted_rad(-math.pi / 2)

while True:
	pidA.proc()
	time.sleep(0.01)
