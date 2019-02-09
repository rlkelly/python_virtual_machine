from gates import xor_gate, and_gate, not_gate, or_gate, threeway_and_gate


class Comparator(object):
    def __init__(self, a, b, prev_bits_equal, a_larger):
        self.a = a
        self.b = b
        self.prev_bits_equal = prev_bits_equal
        self.a_larger = a_larger

    def output(self):
        unequal = xor_gate(self.a, self.b)
        equal = not_gate(unequal)
        so_far_equal = and_gate(self.prev_bits_equal, equal)
        twa = threeway_and_gate(self.prev_bits_equal, self.a, unequal)
        a_larger = or_gate(self.a_larger, twa)
        return so_far_equal, a_larger, unequal


class EightBitComparator(object):
    def __init__(self, a=[0, 0, 0, 0, 0, 0, 0, 0], b=[0, 0, 0, 0, 0, 0, 0, 0]):
        self.a = a
        self.b = b
        self.output = [0, 0, 0, 0, 0, 0, 0, 0]

    def update_a(self, a):
        self.a = a

    def update_b(self, b):
        self.b = b

    def compare(self):
        so_far_equal = 1
        a_larger = 0
        for i in range(8)[::-1]:
            a = Comparator(self.a[i], self.b[i], so_far_equal, a_larger)
            so_far_equal, a_larger, unequal = a.output()
            self.output[i] = unequal
        return self.output, a_larger


def test():
    e = EightBitComparator([1, 1, 1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0])
    _, larger = e.compare()
    assert not larger

    e = EightBitComparator([1, 1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0])
    _, larger = e.compare()
    assert larger

    e = EightBitComparator([0, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0])
    _, larger = e.compare()
    assert larger
