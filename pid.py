from time import time
''' pid obj prototype
pid_obj = {
    'setup': (0, 0, 0, 0), #kp, ki, kd, initial_value

    'error_i': 0,
    'ini_val': 0,
    'last_time': 0,

    'state': dict.fromkeys(['last', 'now', 'wanted']),

    Motor: <...>,
    Sensor: <...>
}
'''

def reset_pid(pid_obj):
    pid_obj['error_i'] = 0
    pid_obj['ini_val'] = 0
    pid_obj['last_time'] = 0

def pid(pid_obj):

    dt = (time.time() - pid_obj['last_time']) / 1000
    pid_obj['last_time'] = time.time()

    (kp, ki, kd, ini_val) = pid_obj['setup']

    error = state['wanted'] - state['now']
    error_d = (error - (state['wanted'] - state['last'])) / dt
    pid_obj['error_i'] += error * dt

    new_state = 0
    #new_state = Sensor.<get_value>()

    (pid_obj['state']['last'], pid_obj['state']['now']) = (pid_obj['state']['now'], new_state)

    Ut = kp * error + ki * pid_obj['error_i'] + kd * error_d

    value = ini_val + Ut

    #Motor.<set_value>()
