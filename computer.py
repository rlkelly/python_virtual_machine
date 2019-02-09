from alu import ALU
from bus import Bus
from bus_one import BusOne
from clock import Clock
from constants import ON
from ram import RAM
from stepper import Stepper


class Computer(object):
    def __init__(self):
        steps = 7

        self.bus = Bus()
        self.bus_one = BusOne()
        self.bus.add_register('R0', [1, 1, 0, 0, 0, 0, 0, 0])
        self.bus.add_register('R1', [1, 0, 0, 0, 0, 0, 0, 0])
        self.bus.add_register('R2', [1, 0, 0, 0, 0, 0, 0, 0])
        self.bus.add_register('R3', [0, 0, 0, 0, 0, 0, 0, 0])

        self.bus.add_register('TMP')
        self.bus.registers['TMP'].update_save(ON)
        self.bus.add_register('ACC')
        self.bus.add_register('IAR')
        self.bus.add_register('IR')

        self.ram = RAM()

        self.bus.add_register_instance('MAR', self.ram.memory_access_register)
        self.bus.add_register_instance('RAM', self.ram)

        self.alu = ALU()
        self.stepper = Stepper(
            self.bus,
            self.bus_one,
            alu=self.alu,
            ram=self.ram,
            steps=steps,
        )
        self.clk = Clock(self.stepper, self.bus, speed=0.2)

    def set_step(self, step, ops):
        self.stepper.set_step(step, ops[4:])

    def run(self):
        self.clk.run()

if __name__ == '__main__':
    c = Computer()
    c.ram.update_ram_at_loc([0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 0])
    c.ram.update_ram_at_loc([1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 0, 1, 0, 0])
    c.ram.update_ram_at_loc([0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1])
    c.run()
