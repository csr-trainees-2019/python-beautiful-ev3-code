import time
import math
from ev3dev.ev3 import *

def cut_abs(value, max):
    return max * math.copysign(1, value) if abs(value) > max else value

class PID:
    def __init__(self, setup, motor):
        self.motor = motor
        (self.kp, self.ki, self.kd) = setup
        self.state = {'last': 0, 'now': 0, 'wanted': 0}
        (self.error_i, self.last_time, self.wdup) = (0, time.time(), 0)
        self.motor.reset()
        self.LIMIT_ERR = 0
        self.neg_lim = -math.pi
        self.pos_lim = math.pi
        self.power = PowerSupply()
        self.launch_time = time.time()
        self.file_handle = open('log_pid_new_new7.txt', 'w')

    def set_limits(self, negative, positive):
        self.neg_lim = negative
        self.pos_lim = positive

    def set_motor(self, new):
        self.motor = new

    def set_setup(self, new):
        (self.kp, self.ki, self.kd) = new

    def set_wanted_rad(self, wanted):
        self.state['wanted'] = wanted
        self.LIMIT_ERR = 0

    def set_wdup(self, new):
        self.wdup = new

    def proc(self):
        dt = (time.time() - self.last_time)
        self.last_time = time.time()
        error = self.state['wanted'] - self.state['now']
        error_d = (error - (self.state['wanted'] - self.state['last'])) / dt
        self.error_i += error * dt
        if self.wdup != 0:
            self.error_i = self.error_i if abs(self.error_i) < self.wdup else math.copysign(1, self.error_i) * self.wdup

        new_state = self.motor.position / 180 * math.pi / 5.5
        if new_state > self.pos_lim:
            self.LIMIT_ERR = 1
        elif new_state < self.neg_lim:
            self.LIMIT_ERR = -1
        else:
             self.LIMIT_ERR = 0

        (self.state['last'], self.state['now']) = (self.state['now'], new_state)
        Ut = self.kp * error + self.ki * self.error_i + self.kd * error_d
        value = (Ut * 5 / 0.5) / self.power.measured_volts * 100
        # R = 5
        # Km = 0.5
        # value = Ut * R / Km / Umax * 100%
        value = cut_abs(value, 100)


        if self.LIMIT_ERR != 0:
            if math.copysign(1, self.LIMIT_ERR) == math.copysign(1, value):
                self.motor.stop(stop_action = 'brake')
                return "limit+" if self.LIMIT_ERR > 0 else "limit-" + " error, (" + str(new_state) + " rad), lim[" + str(self.neg_lim) + ";" + str(self.pos_lim) + "], " + str(self.LIMIT_ERR)

        self.motor.run_direct(duty_cycle_sp = value)

        self.file_handle.write(str(self.state['now']) + " " + str(time.time() - self.launch_time) + "\n")

        return 'ok'

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
