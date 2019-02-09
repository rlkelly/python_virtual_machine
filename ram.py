from bus import Bus
from constants import EMPTY_BYTE, OFF, ON
from decoder import FourInputDecoder
from gates import and_gate
from register import Register


class MemoryLocation(object):
    def __init__(self):
        self.register = Register()
        self.vertical = OFF
        self.horizontal = OFF
        self.save = OFF
        self.emit = OFF

        self.update_activated()

    def set_horizontal(self, horizontal):
        self.horizontal = horizontal
        self.update_activated()

    def set_vertical(self, vertical):
        self.vertical = vertical
        self.update_activated()

    def update_activated(self):
        self.activated = and_gate(self.horizontal, self.vertical)

    def update_save(self, save):
        self.register.update_save(and_gate(self.activated, save))

    def update_emit(self, enabled):
        self.register.update_emit(and_gate(self.activated, enabled))

    def update_byte(self, byte):
        self.register.update_byte(byte)

    def output(self):
        return self.register.output()


class RAM(object):
    def __init__(self, set_a=ON, save=OFF, enabled=OFF):
        # Memory Address Register
        self.memory_access_register = Register(save=set_a, enabled=ON)
        self.decoder_one = FourInputDecoder(0, 0, 0, 0)
        self.decoder_two = FourInputDecoder(0, 0, 0, 0)
        self.ram_grid = [[MemoryLocation() for _ in range(16)] for _ in range(16)]
        self.current_register = self.ram_grid[0][0].register

    def update_set_a(self, set_a):
        self.memory_access_register.update_save(set_a)

    def update_location(self, byte):
        self.memory_access_register.update_byte(byte)
        bytes = self.memory_access_register.output()
        self.decoder_one.update_inputs(*bytes[:4])
        self.decoder_two.update_inputs(*bytes[4:])
        self.set_location()

    def update_horizontals(self, axis):
        for i, row in enumerate(self.ram_grid):
            if i == axis:
                [ml.set_horizontal(ON) for ml in row]
            else:
                [ml.set_horizontal(OFF) for ml in row]

    def update_verticals(self, axis):
        for row in self.ram_grid:
            for i, ml in enumerate(row):
                if i == axis:
                    ml.set_vertical(ON)
                else:
                    ml.set_vertical(OFF)

    def set_location(self):
        x = self.decoder_one.output().index(1)
        y = self.decoder_two.output().index(1)
        self.update_horizontals(x)
        self.update_verticals(y)
        active_registers = []
        for row in self.ram_grid:
            for ml in row:
                if ml.activated:
                    active_registers.append(ml)
        if len(active_registers) > 1:
            raise Exception('Not Physically Possible')
        if len(active_registers) == 0:
            return 'No Active Registers'
        self.current_register = active_registers[0].register

    def update_byte(self, byte):
        for row in self.ram_grid:
            for ml in row:
                ml.update_byte(byte)

    def update_save(self, save):
        for row in self.ram_grid:
            for ml in row:
                ml.register.set_bus_save(ON)
                ml.update_save(save)

    def update_emit(self, enabled):
        for row in self.ram_grid:
            for ml in row:
                ml.register.set_bus_emit(ON)
                ml.update_emit(enabled)

    def update_ram_at_loc(self, location=EMPTY_BYTE, value=EMPTY_BYTE):
        loc = self.update_location(location)
        self.update_save(ON)
        self.update_emit(ON)
        self.update_byte(value)

    def set_bus_emit(self, emitter):
        self.current_register.set_bus_emit(emitter)

    def set_bus_save(self, save):
        self.current_register.set_bus_save(save)

    def output(self):
        return self.current_register.output()


def test():
    r = RAM()
    r.update_location([1, 0, 0, 0, 0, 0, 0, 0])

    r.update_save(ON)
    r.update_emit(ON)

    r.update_byte([1, 1, 1, 1, 0, 0, 0, 0])
    assert r.output() == [1, 1, 1, 1, 0, 0, 0, 0]

    r.update_emit(OFF)
    assert r.output() == [0, 0, 0, 0, 0, 0, 0, 0]

    r.update_ram_at_loc([1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1])
    r.update_location([1, 1, 0, 0, 0, 0, 0, 0])
    assert r.output() == [1, 1, 1, 1, 1, 1, 1, 1]

    loc = r.update_location([1, 0, 0, 0, 0, 0, 0, 0])
    r.update_emit(ON)
    assert r.output() == [1, 1, 1, 1, 0, 0, 0, 0]


if __name__ == '__main__':
    test()
