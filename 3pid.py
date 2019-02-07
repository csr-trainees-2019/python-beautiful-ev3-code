from modules.pid import *

setupA = setupB = setupC = (20, 35, 0)

pidA = PID(setupA, LargeMotor('outA'))
pidB = PID(setupB, LargeMotor('outB'))
pidC = PID(setupC, LargeMotor('outC'))

def set_assembly_state(wanted_for_A, wanted_for_B, wanted_for_C):
    pidA.set_wanted_rad(wanted_for_A)
    pidB.set_wanted_rad(wanted_for_B)
    pidC.set_wanted_rad(wanted_for_C)

def assembly_proc():
    pidA.proc()
    pidB.proc()
    pidC.proc()

while True:
	assembly_proc()
    time.sleep(0.01)
