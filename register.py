from constants import OFF, ON, EMPTY_BYTE
from byte import Byte
from enabler import Enabler
from gates import and_gate


class Register(object):
    def __init__(self, save=OFF, byte=EMPTY_BYTE, enabled=OFF):
        self.byte = Byte(save, byte)
        self.enabler = Enabler(enabled)
        self.bus_save = OFF
        self.bus_emit = OFF

    def update_byte(self, byte):
        self.byte.update(*byte)

    def update_save(self, save):
        self.byte.set_save(and_gate(save, self.bus_save))

    def update_emit(self, enabled):
        self.enabler.set_enabled(and_gate(enabled, self.bus_emit))

    def set_bus_emit(self, enabled):
        self.bus_emit = enabled

    def set_bus_save(self, set):
        self.bus_save = set

    def output(self):
        return self.enabler.set_byte(self.byte.get_output())

def test():
    r = Register(save=OFF, enabled=ON)
    r.set_bus_save(ON)
    r.update_save(ON)
    r.update_byte([ON, OFF, ON, ON, OFF, ON, OFF, ON])
    assert r.output() == [1, 0, 1, 1, 0, 1, 0, 1]

    r.update_emit(OFF)
    r.set_bus_emit(OFF)
    assert r.output() == [0, 0, 0, 0, 0, 0, 0, 0]
