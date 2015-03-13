__author__ = 'SolarLune'

from bge import logic

# Time-based mechanics.


class TimerBank():

    def __init__(self):

        self.time = 0.0

        self.timers = {}

    def add(self, timer_name):

        self.timers[timer_name] = Timer()

    def set(self, timer_name, time):

        self.timers[timer_name].set(time)

    def get_time_left(self, timer_name):

        return self.timers[timer_name].get_time_left()

    def time_up(self, timer_name):

        return self.timers[timer_name].time_up()

    def update(self):

        for t in self.timers:

            t.update()


class Timer():

    def __init__(self):

        self.time = 0.0
        self.wait_time = 0.0
        self.set_time = 0.0
        self.on = True

    def set(self, time):
        self.set_time = self.time
        self.wait_time = time
        self.on = True

    def add(self, time):

        #self.set_time += time
        self.wait_time += time

    def get_time_left(self):

        if self.on:
            return self.wait_time - (self.time - self.set_time)
        else:
            return 0

    def time_up(self):

        if self.on:
            return self.get_time_left() <= 0
        else:
            return False

    def pause(self):

        self.on = False

    def resume(self):

        self.on = True

    def update(self, frequency=0):

        if self.on:
            self.time += (1.0 / logic.getLogicTicRate()) * (frequency + 1)


timer_bank = TimerBank()
