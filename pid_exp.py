from modules.pid import *

motor = LargeMotor('outC')
setup = (10.67284, 0, 0.0180556)

pidA = PID(setup, motor)
pidA.set_wanted_rad(math.pi)
pidA.set_limits(-math.pi * 100, math.pi * 100)
#pidA.set_wdup(0.1)

launch = time.time()

while True:
	pidA.proc()

	if time.time() - launch >= 10:
		break

pidA.reset()
