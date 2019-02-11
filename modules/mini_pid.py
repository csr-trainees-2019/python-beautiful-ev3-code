import time
import math
from ev3dev.ev3 import *

def cut_abs(value, max):
    return max * math.copysign(1, value) if abs(value) > max else value

class PID:
    def __init__(self, setup, motor, wdup):
        self.motor = motor
        (self.kp, self.ki, self.kd) = setup
        self.state = {'last': 0, 'now': 0, 'wanted': 0}
        (self.error_i, self.last_time, self.wdup) = (0, time.time(), 0)
        self.motor.reset()
        self.LIMIT_ERR = 0
        self.neg_lim = -math.pi
        self.pos_lim = math.pi
        self.wdup = wdup

    def set_limits(self, negative, positive):
        self.neg_lim = negative
        self.pos_lim = positive

    def set_wanted_rad(self, wanted):
        self.state['wanted'] = wanted
        self.LIMIT_ERR = 0

    def proc(self):
        dt = (time.time() - self.last_time)
        self.last_time = time.time()
        error = self.state['wanted'] - self.state['now']
        error_d = (error - (self.state['wanted'] - self.state['last'])) / dt
        if self.wdup != 0:
            error_i = error_i if abs(error_i) < self.wdup else math.copysign(1, error_i) * self.wdup
        self.error_i += error * dt

        new_state = self.motor.position / 180 * math.pi
        if new_state > self.pos_lim:
            self.LIMIT_ERR = 1
        elif new_state < self.neg_lim:
            self.LIMIT_ERR = -1
        else:
             self.LIMIT_ERR = 0

        (self.state['last'], self.state['now']) = (self.state['now'], new_state)
        Ut = self.kp * error + self.ki * self.error_i + self.kd * error_d
        value = cut_abs(Ut, 100)

        if self.LIMIT_ERR != 0:
            if math.copysign(1, self.LIMIT_ERR) == math.copysign(1, value):
                self.motor.stop(stop_action = 'brake')

        self.motor.run_direct(duty_cycle_sp = value)

    def get_state(self):
        return self.state['now']

    def is_competed(self, eps):
        if self.LIMIT_ERR != 0:
            return True
        if abs(self.state['now'] - self.state['wanted']) <= eps:
            return True
        return False

    def unreset(self):
        self.last_time = time.time()

    def reset(self):
        (self.last_time, self.error_i) = (time.time(), 0)
        self.motor.stop(stop_action = 'brake')
