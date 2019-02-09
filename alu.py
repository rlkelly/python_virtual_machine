from adder import eight_bit_adder
from constants import EMPTY_BYTE, OFF
from decoder import ThreeInputDecoder
from gates import xorer, orrer, ander, notter, left_bit_shifter, right_bit_shifter, zero_gate


class ALU(object):
    def __init__(self, a=EMPTY_BYTE, b=EMPTY_BYTE, carry_in=0, op=[0, 0, 0]):
        self.a = a
        self.b = b
        self.carry_in = carry_in
        self.operation = ThreeInputDecoder(*op)
        self.operations = [
            xorer,
            orrer,
            ander,
            notter,
            left_bit_shifter,
            right_bit_shifter,
            eight_bit_adder,
        ]
        self.carry_out = OFF
        self.a_larger = OFF
        self.result = EMPTY_BYTE
        self.zero = zero_gate(self.result)

    def update_inputs(self, a, b, carry_in, op):
        self.a = a
        self.b = b
        self.carry_in = carry_in
        self.update_op(op)

    def update_op(self, op):
        self.operation.update_inputs(*op)

    def current_op(self):
        return self.operation.output()

    def output(self):
        op = self.operations[self.current_op().index(1)]
        self.result, self.carry_out = op(self.carry_in, self.a, self.b)
        self.zero = zero_gate(self.result)
        return self.result

if __name__ == '__main__':
    alu = ALU()
    alu.update_op([0, 1, 1])
    alu.output()
