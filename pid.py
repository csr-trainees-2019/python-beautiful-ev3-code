from time import time

class PID:
    def __init__(self, setup, motor):
        self.motor = motor
        (kp, ki, kd) = setup
        self.state = dict.fromkeys(['last', 'now', 'wanted'])
        (self.error_i, self.last_time) = (0, 0)

    def proc(self):
        dt = (time.time() - self.last_time) / 1000
        self.last_time = time.time()
        error = self.state['wanted'] - self.state['now']
        error_d = (error - (self.state['wanted'] - self.state['last'])) / dt
        self.error_i += error * dt

        new_state = self.motor.position

        (self.state['last'], self.state['now']) = (self.state['now'], new_state)
        Ut = kp * error + ki * self.error_i + kd * error_d
        value = Ut

        self.motor.run_direct(duty_cycle_sp=value)

    def reset(self):
        (self.last_time, self.error_i) = (0, 0)
