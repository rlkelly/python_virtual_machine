from constants import EMPTY_BYTE, OFF
from gates import xor_gate, and_gate, or_gate


class Adder(object):
    def __init__(self, a=EMPTY_BYTE, b=EMPTY_BYTE, carry_in=0):
        self.a = a
        self.b = b
        self.carry_in = carry_in

    def output(self):
        diff = xor_gate(self.a, self.b)
        self.sum = xor_gate(diff, self.carry_in)
        first_carry = and_gate(self.carry_in, diff)
        second_carry = and_gate(self.a, self.b)
        self.carry_out = or_gate(first_carry, second_carry)
        return self.sum, self.carry_out


class EightBitAdder(object):
    def __init__(self, a=[0, 0, 0, 0, 0, 0, 0, 0], b=[0, 0, 0, 0, 0, 0, 0, 0]):
        self.a = a
        self.b = b
        self.output = [0, 0, 0, 0, 0, 0, 0, 0]

    def update_a(self, a):
        self.a = a

    def update_b(self, b):
        self.b = b

    def add(self):
        carry_in = 0
        for i in range(8):
            a = Adder(self.a[i], self.b[i], carry_in)
            sum, carry_in = a.output()
            self.output[i] = sum
        return self.output


def eight_bit_adder(carry_in, a, b):
    adder = EightBitAdder(a, b)
    return adder.add(), OFF


def test():
    e = EightBitAdder([1, 0, 1, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0])
    assert e.add() == [0, 0, 0, 1, 0, 0, 0, 0]
