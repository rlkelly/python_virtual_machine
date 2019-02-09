from memory import MemoryGate
from constants import OFF, ON, EMPTY_BYTE


class Byte(object):
    def __init__(self, save=OFF, byte=EMPTY_BYTE):
        self.byte = [MemoryGate(byte[i], ON) for i in range(8)]
        self.set_save(save)
        self.output = [m.get_output() for m in self.byte]

    def update(self, d0, d1, d2, d3, d4, d5, d6, d7):
        self.byte[0].set_input(d0)
        self.byte[1].set_input(d1)
        self.byte[2].set_input(d2)
        self.byte[3].set_input(d3)
        self.byte[4].set_input(d4)
        self.byte[5].set_input(d5)
        self.byte[6].set_input(d6)
        self.byte[7].set_input(d7)

    def set_save(self, save):
        [m.set_save(save) for m in self.byte]
        return self.get_output()

    def get_output(self):
        self.output = [m.get_output() for m in self.byte]
        return self.output

def test():
    b = Byte()
    b.update(ON, OFF, ON, ON, OFF, ON, OFF, ON)
    assert b.get_output() == [0, 0, 0, 0, 0, 0, 0, 0]
    b.set_save(ON)
    b.update(ON, OFF, ON, ON, OFF, ON, OFF, ON)
    assert b.get_output() == [1, 0, 1, 1, 0, 1, 0, 1]
