import time
import math
from ev3dev.ev3 import *

def cut_abs(value, max):
    return max * math.copysign(1, value) if abs(value) > max else value

class PI:
    def __init__(self, setup, motor, wdup):
        self.motor = motor
        (self.kp, self.ki) = setup
        self.state = {
            'last_pos': 0, 'now_pos': 0, 'wanted_pos': 0,
            'last_spd': 0, 'now_spd': 0, 'wanted_spd': 0
        }
        (self.error_i, self.last_time, self.wdup) = (0, time.time(), 0)
        self.motor.reset()
        self.wdup = new

    def set_wanted_spd(self, wanted_spd):
        self.state['wanted_spd'] = wanted_spd

    def proc(self):
        dt = (time.time() - self.last_time) / 1000
        self.last_time = time.time()
        error = self.state['wanted_spd'] - self.state['now_spd']
        error_d = (error - (self.state['wanted_spd'] - self.state['last_spd'])) / dt
        if self.wdup != 0:
            error_i = error_i if abs(error_i) < self.wdup else math.copysign(1, error_i) * self.wdup
        self.error_i += error * dt

        new_state_spd = getSpeed

        (self.state['last_spd'], self.state['now_spd']) = (self.state['now_spd'], new_state_spd)
        derivative = (self.state['now_spd'] - self.state['last_spd']) / dt
        Ut = self.kp * error + self.ki * self.error_i
        value = cut_abs(Ut, 100)
        self.motor.run_direct(duty_cycle_sp = value)

    def get_state_spd(self):
        return self.state['now_spd']

    def unreset(self):
        self.last_time = time.time()

    def reset(self):
        (self.last_time, self.error_i) = (time.time(), 0)
        self.motor.stop(stop_action = 'brake')
