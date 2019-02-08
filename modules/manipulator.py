from modules.pid import *

class Mani:
    def __init__(self, knots, motors, setuplist, ratiolist):
        self.CREATE_ERR = False
        if knots != len(motors) or knots != len(setuplist) or knots != len(ratiolist):
            self.CREATE_ERR = True
        else:
            self.pidlist = []
            self.gear_ratio_list = ratiolist
            for i in range(knots):
                self.pidlist.append(PID(setuplist[i], motors[i]))

    def set_limits(self, neg, pos):
        if self.CREATE_ERR:
            return 'create error'
        if len(neg) != len(self.pidlist) or len(pos) != len(self.pidlist):
            return 'error'
        for i in range(0, len(self.pidlist)):
            self.pidlist[i].set_limits(neg[i] * self.gear_ratio_list[i], pos[i] * self.gear_ratio_list[i])
        return 'ok'

    def set_setup(self, setuplist):
        if self.CREATE_ERR:
            return 'create error'
        if len(setuplist) != len(self.pidlist):
            return 'error';
        for i in range(0, len(self.pidlist)):
            self.pidlist[i].set_setup(setuplist[i])
        return 'ok'

    def set_state(self, wantedlist):
        if self.CREATE_ERR:
            return 'create error'
        if len(wantedlist) != len(self.pidlist):
            return 'error';
        for i in range(0, len(self.pidlist)):
            self.pidlist[i].set_wanted_rad(wantedlist[i] * self.gear_ratio_list[i])
        return 'ok'

    def get_state(self):
        if self.CREATE_ERR:
            return 'create error'
        to_ret = []
        for i in range(0, len(self.pidlist)):
            to_ret.append(self.pidlist[i].get_state() / self.gear_ratio_list[i])
        return to_ret

    def set_wdups(self, wduplist):
        if self.CREATE_ERR:
            return 'create error'
        if len(wduplist) != len(self.pidlist):
            return 'error';
        for i in range(0, len(self.pidlist)):
            self.pidlist[i].set_wdup(wduplist[i])
        return 'ok'

    def is_competed(self, eps):
        if self.CREATE_ERR:
            return True
        for i in self.pidlist:
            if i.is_competed(eps) != True:
                return False
        return True

    def reset(self):
        if self.CREATE_ERR:
            return 'create error'
        for i in self.pidlist:
            i.reset()

    def unreset(self):
        if self.CREATE_ERR:
            return 'create error'
        for i in self.pidlist:
            i.last_time = time.time()

    def proc(self):
        if self.CREATE_ERR:
            return 'create error'
        print('----------')
        for i in self.pidlist:
            print(i.proc())
