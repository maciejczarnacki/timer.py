# Simple timer package

import time

class Timer:
    def __init__(self, units = 's', precision = 0):
        self.start_point = 0
        self.end_point = 0
        self.total_time = 0
        self.elapsed_time = 0
        self.check_point = 0
        self.ticking = False
        self.units = units
        if self.units != 's' and self.units != 'ms':
            raise Exception('Unit must be seconds (s) or milliseconds (ms)!')
        self.precision = precision
    
    def start(self):
        self.zero()
        if self.ticking == False:
            self.start_point = time.time()
            self.ticking = True
    
    def stop(self) -> float:
        if self.ticking:
            self.end_point = time.time()
            self.total_time = self.end_point - self.start_point
            self.ticking = False
        if self.units == 's':
            return round(self.total_time, self.precision)
        elif self.units == 'ms':
            return round(self.total_time * 1000, self.precision)
    
    def check(self) -> float:
        if self.ticking:
            self.check_point = time.time()
            self.elapsed_time = self.check_point - self.start_point
        if self.units == 's' and self.ticking:
            return round(self.elapsed_time, self.precision)
        elif self.units == 'ms'and self.ticking:
            return round(self.elapsed_time * 1000, self.precision)
        else:
            self.zero()
            return 0
    
    def zero(self):
        self.start_point = 0
        self.end_point = 0
        self.total_time = 0
        self.elapsed_time = 0
        self.check_point = 0
        self.ticking = False
    
    def restart(self):
        self.zero()
        self.start()
        