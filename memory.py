from constants import OFF, ON
from gates import nand_gate


class MemoryGate(object):
    def __init__(self, input, save):
        self.input = input
        self.save = save

        self.a = 0
        self.b = 0
        self.c = 0

        self.output = 0
        self.update()

    def set_input(self, i):
        self.input = i
        self.update()

    def set_save(self, s):
        self.save = s
        self.update()

    def update(self):
        self.a = nand_gate(self.input, self.save)
        self.b = nand_gate(self.a, self.save)
        self.c = nand_gate(self.b, self.output)
        self.output = nand_gate(self.a, self.c)
        # print 'save is %s' % self.save
        # print 'input is %s' % self.input
        # print 'a is %s' % self.a
        # print 'b is %s' % self.b
        # print 'c is %s' % self.c
        # print 'output is %s\n' % self.output
        return self.output

    def get_output(self):
        return self.output


def tests():
    m = MemoryGate(input=OFF, save=ON)
    # OFF / ON
    assert m.get_output() == OFF
    m.set_input(ON)
    # ON / ON
    assert m.get_output() == ON

    m.set_save(OFF)
    # ON / OFF
    assert m.get_output() == ON
    # OFF / OFF
    m.set_input(OFF)
    assert m.get_output() == ON

    m.set_save(ON)
    # OFF / ON
    assert m.get_output() == OFF
    m.set_input(ON)
    # ON / ON
    assert m.get_output() == ON

    m.set_input(OFF)
    assert m.get_output() == OFF

    m.set_save(OFF)
    assert m.get_output() == OFF
