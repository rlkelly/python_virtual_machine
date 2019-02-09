import time

from bus import Bus
from constants import OFF, ON
from stepper import Stepper


class Clock(object):
    def __init__(self, stepper=Stepper(), bus=Bus(), steps=7, speed=1):
        self.clk = OFF
        self.stepper = stepper
        self.bus = bus
        self.speed =  speed

    def tick(self):
        self.bus.set_bus_emit(ON)
        self.bus.set_bus_save(ON)
        self.stepper.clk()
        self.bus.set_bus_save(OFF)
        self.bus.set_bus_emit(OFF)

    def run(self):
        while True:
            time.sleep(self.speed)
            self.tick()
