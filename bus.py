from constants import EMPTY_BYTE, OFF, ON
from register import Register


class Bus(object):
    def __init__(self):
        self.byte = EMPTY_BYTE
        self.carry_in = OFF
        self.op = [1, 1, 0]
        self.registers = {}

    def add_register(self, name, byte=EMPTY_BYTE):
        self.registers[name] = Register(byte=byte)

    def add_register_instance(self, name, register):
        self.registers[name] = register

    def update_byte(self, byte):
        self.byte = byte
        [r.update_byte(self.byte) for r in self.registers.values()]

    def set_bus_save(self, save):
        for r in self.registers:
            self.registers[r].set_bus_save(save)

    def set_bus_emit(self, enabled):
        for r in self.registers:
            self.registers[r].set_bus_emit(enabled)

def test():
    b = Bus()
    b.add_register('R1')
    b.set_bus_save(ON)
    b.set_bus_emit(ON)
    assert b.registers['R1'].output() == [0, 0, 0, 0, 0, 0, 0, 0]

    b.registers['R1'].update_save(ON)
    b.registers['R1'].update_emit(ON)

    b.update_byte([0, 1, 1, 0, 1, 0, 1, 0])
    assert b.registers['R1'].output() == [0, 1, 1, 0, 1, 0, 1, 0]
