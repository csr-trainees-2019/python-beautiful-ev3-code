from modules.pid import *

motor = LargeMotor('outC')
setup = (5, 0, 0)

pidA = PID(setup, motor)
pidA.set_wanted_rad(math.pi * 5.5)
pidA.set_limits(-math.pi * 10, math.pi * 10)
pidA.set_wdup(6)

while True:
	pidA.proc()
