from modules.pi_by_speed import *

class Manispd:
    def __init__(self, knots, motors, setuplist, ratiolist, wduplist):
        self.pilist = []
        self.gear_ratio_list = ratiolist
        for i in range(knots):
            self.pilist.append(PI(setuplist[i], motors[i], wduplist[i]))

    def set_state_spd(self, wantedlist):
        for i in range(0, len(self.pilist)):
            self.pilist[i].set_wanted_spd(wantedlist[i] * self.gear_ratio_list[i])

    def get_state_spd(self):
        to_ret = []
        for i in range(0, len(self.pilist)):
            to_ret.append(self.pilist[i].get_state_spd() / self.gear_ratio_list[i])
        return to_ret

    def reset(self):
        for i in self.pilist:
            i.reset()

    def unreset(self):
        for i in self.pilist:
            i.last_time = time.time()

    def proc(self):
        for i in self.pilist:
            i.proc()
