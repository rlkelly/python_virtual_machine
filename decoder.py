from gates import not_gate, and_gate, threeway_and_gate, fourway_and_gate


class TwoInputDecoder(object):
    def __init__(self, a, b):
        self.a = a
        self.not_a = not_gate(a)
        self.b = b
        self.not_b = not_gate(b)

    def update_a(self, a):
        self.a = a
        self.not_a = not_gate(a)
        self.output()

    def update_b(self, b):
        self.b = b
        self.not_b = not_gate(b)
        self.output()

    def output(self):
        self.first = and_gate(self.not_a, self.not_b)
        self.second = and_gate(self.not_a, self.b)
        self.third = and_gate(self.a, self.not_b)
        self.fourth = and_gate(self.a, self.b)
        return [self.first, self.second, self.third, self.fourth]

class ThreeInputDecoder(object):
    def __init__(self, a, b, c):
        self.a = a
        self.not_a = not_gate(a)
        self.b = b
        self.not_b = not_gate(b)
        self.c = c
        self.not_c = not_gate(c)

    def update_a(self, a):
        self.a = a
        self.not_a = not_gate(a)
        self.output()

    def update_b(self, b):
        self.b = b
        self.not_b = not_gate(b)
        self.output()

    def update_c(self, c):
        self.c = c
        self.not_c = not_gate(c)
        self.output()

    def update_inputs(self, a, b, c):
        self.a = a
        self.not_a = not_gate(a)
        self.b = b
        self.not_b = not_gate(b)
        self.c = c
        self.not_c = not_gate(c)
        return self.output()

    def output(self):
        self.first = threeway_and_gate(self.not_a, self.not_b, self.not_c)
        self.second = threeway_and_gate(self.not_a, self.not_b, self.c)
        self.third = threeway_and_gate(self.not_a, self.b, self.not_c)
        self.fourth = threeway_and_gate(self.not_a, self.b, self.c)
        self.fifth = threeway_and_gate(self.a, self.not_b, self.not_c)
        self.sixth = threeway_and_gate(self.a, self.not_b, self.c)
        self.seventh = threeway_and_gate(self.a, self.b, self.not_c)
        self.eighth = threeway_and_gate(self.a, self.b, self.c)
        return [
            self.first,
            self.second,
            self.third,
            self.fourth,
            self.fifth,
            self.sixth,
            self.seventh,
            self.eighth,
        ]

class FourInputDecoder(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.not_a = not_gate(a)
        self.b = b
        self.not_b = not_gate(b)
        self.c = c
        self.not_c = not_gate(c)
        self.d = d
        self.not_d = not_gate(d)

    def update_a(self, a):
        self.a = a
        self.not_a = not_gate(a)
        self.output()

    def update_b(self, b):
        self.b = b
        self.not_b = not_gate(b)
        self.output()

    def update_c(self, c):
        self.c = c
        self.not_c = not_gate(c)
        self.output()

    def update_d(self, d):
        self.d = d
        self.not_d = not_gate(d)
        self.output()

    def update_inputs(self, a, b, c, d):
        self.a = a
        self.not_a = not_gate(a)
        self.b = b
        self.not_b = not_gate(b)
        self.c = c
        self.not_c = not_gate(c)
        self.d = d
        self.not_d = not_gate(d)

    def output(self):
        # TODO: Fix order of gates
        self.first = fourway_and_gate(self.not_a, self.not_b, self.not_c, self.not_d)
        self.second = fourway_and_gate(self.not_a, self.not_b, self.not_c, self.d)
        self.third = fourway_and_gate(self.not_a, self.not_b, self.c, self.not_d)
        self.fourth = fourway_and_gate(self.not_a, self.not_b, self.c, self.d)
        self.fifth = fourway_and_gate(self.not_a, self.b, self.not_c, self.not_d)
        self.sixth = fourway_and_gate(self.not_a, self.b, self.not_c, self.d)
        self.seventh = fourway_and_gate(self.not_a, self.b, self.c, self.not_d)
        self.eighth = fourway_and_gate(self.not_a, self.b, self.c, self.d)

        self.nine = fourway_and_gate(self.a, self.not_b, self.not_c, self.not_d)
        self.ten = fourway_and_gate(self.a, self.not_b, self.not_c, self.d)
        self.eleven = fourway_and_gate(self.a, self.not_b, self.c, self.not_d)
        self.twelve = fourway_and_gate(self.a, self.not_b, self.c, self.d)
        self.thirteen = fourway_and_gate(self.a, self.b, self.not_c, self.not_d)
        self.fourteen = fourway_and_gate(self.a, self.b, self.not_c, self.d)
        self.fifteen = fourway_and_gate(self.a, self.b, self.c, self.not_d)
        self.sixteen = fourway_and_gate(self.a, self.b, self.c, self.d)

        return [
            self.first,
            self.second,
            self.third,
            self.fourth,
            self.fifth,
            self.sixth,
            self.seventh,
            self.eighth,
            self.nine,
            self.ten,
            self.eleven,
            self.twelve,
            self.thirteen,
            self.fourteen,
            self.fifteen,
            self.sixteen,
        ]


def test_two():
    d = TwoInputDecoder(0, 0)
    assert d.output() == [1, 0, 0, 0]

    d.update_a(0)
    d.update_b(1)
    assert d.output() == [0, 1, 0, 0]

    d.update_a(1)
    d.update_b(0)
    assert d.output() == [0, 0, 1, 0]

    d.update_a(1)
    d.update_b(1)
    assert d.output() == [0, 0, 0, 1]


def test_three():
    d = ThreeInputDecoder(0, 0, 0)
    assert d.output() == [1, 0, 0, 0, 0, 0, 0, 0]

    d.update_a(0)
    d.update_b(0)
    d.update_c(1)
    assert d.output() == [0, 1, 0, 0, 0, 0, 0, 0]

    d.update_a(0)
    d.update_b(1)
    d.update_c(0)
    assert d.output() == [0, 0, 1, 0, 0, 0, 0, 0]

    d.update_a(0)
    d.update_b(1)
    d.update_c(1)
    assert d.output() == [0, 0, 0, 1, 0, 0, 0, 0]

    d.update_a(1)
    d.update_b(0)
    d.update_c(0)
    assert d.output() == [0, 0, 0, 0, 1, 0, 0, 0]

    d.update_a(1)
    d.update_b(0)
    d.update_c(1)
    assert d.output() == [0, 0, 0, 0, 0, 1, 0, 0]

    d.update_a(1)
    d.update_b(1)
    d.update_c(0)
    assert d.output() == [0, 0, 0, 0, 0, 0, 1, 0]

    d.update_a(1)
    d.update_b(1)
    d.update_c(1)
    assert d.output() == [0, 0, 0, 0, 0, 0, 0, 1]
