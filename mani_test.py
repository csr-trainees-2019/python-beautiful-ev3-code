from modules.manipulator import *
from ev3dev import *
import math

pi = math.pi

motors = [LargeMotor('outA'), LargeMotor('outB'), LargeMotor('outC')]
setup = [
    (20, 35, 0),
    (20, 35, 0),
    (20, 35, 0)
]

neg_lims = [-pi, -pi/4, -pi]
pos_lims = [pi, pi, pi]

man = Mani(3, motors, setup, [7, 5.5, 5.5])
man.set_state([0, -pi / 2, -pi / 2])
man.set_limits(neg_lims, pos_lims)

processing = True
while processing:
    print("<>")
    man.proc()
    if man.is_competed(0.5):
        break


man.set_state([0, pi / 2, 0])

processing = True
while processing:
    man.proc()
    if man.is_competed(0.5):
        break


print('finish2')
'''
pi = math.pi

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

set_assembly_state(pi / 2 * 7, pi / 2 * 5.5, pi / 2 * 5.5)

while True:
	assembly_proc()
'''
