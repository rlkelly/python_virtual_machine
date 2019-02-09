from constants import EMPTY_BYTE, OFF, ON
from gates import and_gate, not_gate, or_gate


class BusOne(object):
    def __init__(self, a=EMPTY_BYTE, bus_1_bit=OFF):
        self.a = a
        self.bus_1_bit = bus_1_bit
        self.not_bus_1_bit = not_gate(bus_1_bit)
        self.response = EMPTY_BYTE

    def update_temp(self, a=EMPTY_BYTE):
        self.a = a

    def update_bus1_bit(self, bus_1_value):
        self.bus_1_bit = bus_1_value
        self.not_bus_1_bit = not_gate(bus_1_value)
        self.output()

    def output(self):
        for i, bit in enumerate(self.a):
            if i == 0:
                self.response[i] = or_gate(self.bus_1_bit, bit)
            else:
                self.response[i] = and_gate(self.not_bus_1_bit, bit)
        return self.response


def test():
    b = BusOne([1, 1, 1, 1, 0, 0, 0, 0], OFF)
    assert b.output() == [1, 1, 1, 1, 0, 0, 0, 0]
    b.update_bus1_bit(ON)
    assert b.output() == [1, 0, 0, 0, 0, 0, 0, 0]


if __name__ == '__main__':
    test()
