from modules.pid import *

class Mani:
    def __init__(self, knots, motors, setuplist, ratiolist, wdup, limits):
        self.pidlist = []
        self.gear_ratio_list = ratiolist
        for i in range(knots):
            self.pidlist.append(PID(setuplist[i], motors[i]))
        for i in range(0, len(self.pidlist)):
            (neg, pos) = limits[i]
            self.pidlist[i].set_limits(neg * self.gear_ratio_list[i], pos * self.gear_ratio_list[i])
            self.pidlist[i].set_wdup(wduplist[i])

    def set_state(self, wantedlist):
        for i in range(0, len(self.pidlist)):
            self.pidlist[i].set_wanted_rad(wantedlist[i] * self.gear_ratio_list[i])

    def get_state(self):
        to_ret = []
        for i in range(0, len(self.pidlist)):
            to_ret.append(self.pidlist[i].get_state() / self.gear_ratio_list[i])
        return to_ret

    def is_competed(self, eps):
        for i in self.pidlist:
            if i.is_competed(eps) != True:
                return False
        return True

    def reset(self):
        for i in self.pidlist:
            i.reset()

    def unreset(self):
        for i in self.pidlist:
            i.last_time = time.time()

    def proc(self):
        for i in self.pidlist:
            i.proc()
