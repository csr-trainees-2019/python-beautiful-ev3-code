from modules.pid import *

motor = LargeMotor('outC')
setup = (12.463209, 30.791458, 0.0190441)

pidA = PID(setup, motor)
pidA.set_wanted_rad(math.pi)
pidA.set_limits(-math.pi * 100, math.pi * 100)
pidA.set_wdup(1)

launch = time.time()

while True:
	pidA.proc()

	if time.time() - launch >= 15:
		break

pidA.reset()
