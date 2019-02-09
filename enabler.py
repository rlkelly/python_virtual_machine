from constants import OFF, ON
from gates import and_gate


class Enabler(object):
    def __init__(self, enabled=OFF):
        self.enabled = enabled
        self.input_byte = [0 for _ in range(8)]
        self.output = [0 for _ in range(8)]

    def set_enabled(self, enabled):
        self.enabled = enabled
        self.update()

    def set_byte(self, byte):
        self.input_byte = byte
        return self.update()

    def update(self):
        self.output = [and_gate(b, self.enabled) for b in self.input_byte]
        return self.output


def test():
    e = Enabler()
    b = Byte(ON)
    b.update(ON, OFF, ON, ON, OFF, ON, OFF, ON)
    assert e.update() == [0, 0, 0, 0, 0, 0, 0, 0]
    e.set_enabled(ON)
    e.set_byte(b.get_output())
    assert e.update() == [1, 0, 1, 1, 0, 1, 0, 1]
