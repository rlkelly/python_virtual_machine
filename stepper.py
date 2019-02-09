from alu import ALU
from bus import Bus
from bus_one import BusOne
from constants import EMPTY_BYTE, OFF, ON
from ram import RAM


class Stepper(object):
    def __init__(self, bus=Bus(), bus_one=BusOne(), alu=ALU(), ram=RAM(), steps=7, instruction=[1, 0, 0, 0, 0, 0, 0, 0]):
        self.reset = OFF
        self.step = 0
        self.steps = steps
        self.step_connections = [None] * steps
        self.bus = bus
        self.bus_one = bus_one
        self.alu = alu
        self.instruction = instruction
        self.ram = ram

        # Initialize Instructions
        self.set_step(1, ['IAR', 'MAR'])
        self.set_step(2, ['RAM', 'IR'])
        self.set_step(3, ['ACC', 'IAR'])

    def clk(self, instruction=EMPTY_BYTE):
        self.step = (self.step + 1) % self.steps
        items = self.step_connections[self.step]

        if items:
            self.bus.registers[items[0]].update_emit(ON)
            self.bus.registers[items[1]].update_save(ON)

            if self.step == 1:
                self.bus_one.update_bus1_bit(ON)
                self.bus.registers['ACC'].update_save(ON)

            if items[1] == 'ACC' or self.step == 1:
                self.bus.registers['TMP'].update_emit(ON)
                self.bus_one.update_temp(self.bus.registers['TMP'].output())

                self.alu.update_inputs(
                    a=self.bus_one.output(),
                    b=self.bus.registers[items[0]].output(),
                    carry_in=self.bus.carry_in,
                    op=self.instruction[1:4],
                )
                self.bus.registers['ACC'].update_byte(self.alu.output())
                self.bus.registers['TMP'].update_emit(OFF)
            else:
                self.bus.update_byte(self.bus.registers[items[0]].output())

            print self.step, items[1], self.bus.registers[items[0]].output()

            if self.step == 1:
                self.ram.update_set_a(ON)
                self.ram.update_location(self.bus.registers[items[0]].output())
                self.ram.update_set_a(OFF)
                self.ram.update_save(OFF)

                self.bus_one.update_bus1_bit(OFF)
                self.bus.registers['ACC'].update_save(OFF)

            if self.step == 2:
                self.instruction = self.bus.registers[items[0]].output()
                first_register = mapping[tuple(self.instruction[4:6])]
                second_register = mapping[tuple(self.instruction[6:8])]
                if self.instruction[0] == 1:
                    self.set_step(4, [first_register, 'TMP'])
                    self.set_step(5, [second_register, 'ACC'])
                    self.set_step(6, ['ACC', first_register])
                else:
                    self.set_step(4, [second_register, 'IAR'])
                    self.set_step(5, None)
                    self.set_step(6, None)

            self.bus.registers[items[1]].update_save(OFF)
            self.bus.registers[items[0]].update_emit(OFF)

    def set_step(self, step, connection):
        self.step_connections[step] = connection

mapping = {
    (0, 0): 'R0',
    (0, 1): 'R1',
    (1, 0): 'R2',
    (1, 1): 'R3',
}

def test():
    steps = 7
    s = Stepper(steps)
    for _ in range(7):
        s.clk()
