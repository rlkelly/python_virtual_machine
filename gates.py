from constants import OFF


def nand_gate(a, b):
    return (not (a & b)).conjugate()

def not_gate(a):
    return nand_gate(a, a)

def and_gate(a, b):
    return not_gate(nand_gate(a, b))

def or_gate(a, b):
    return nand_gate(not_gate(a), not_gate(b))

def xor_gate(a, b):
    return nand_gate(nand_gate(not_gate(a), b), nand_gate(not_gate(b), a))

def threeway_and_gate(a, b, c):
    return and_gate(and_gate(a, b), c)

def fourway_and_gate(a, b, c, d):
    return and_gate(threeway_and_gate(a, b, c), d)

def right_bit_shifter(carry_in, bytes, unused_arg=None):
    b0, b1, b2, b3, b4, b5, b6, b7 = bytes
    return [carry_in, b0, b1, b2, b3, b4, b5, b6], b7

def left_bit_shifter(carry_in, bytes, unused_arg=None):
    b0, b1, b2, b3, b4, b5, b6, b7 = bytes
    return [b1, b2, b3, b4, b5, b6, b7, carry_in], b0

def zero_gate(bytes):
    b0, b1, b2, b3, b4, b5, b6, b7 = bytes
    return not_gate(or_gate(b0, or_gate(b1, or_gate(b2, or_gate(b3, or_gate(b4, or_gate(b5, or_gate(b6, b7))))))))

def notter(shift_in, bytes, unused_arg=None):
    b0, b1, b2, b3, b4, b5, b6, b7 = bytes
    return [
        not_gate(b0),
        not_gate(b1),
        not_gate(b2),
        not_gate(b3),
        not_gate(b4),
        not_gate(b5),
        not_gate(b6),
        not_gate(b7),
    ], OFF

def orrer(carry_in, bytes0, bytes1):
    return [
        or_gate(bytes0[0], bytes1[0]),
        or_gate(bytes0[1], bytes1[1]),
        or_gate(bytes0[2], bytes1[2]),
        or_gate(bytes0[3], bytes1[3]),
        or_gate(bytes0[4], bytes1[4]),
        or_gate(bytes0[5], bytes1[5]),
        or_gate(bytes0[6], bytes1[6]),
        or_gate(bytes0[7], bytes1[7]),
    ], OFF

def ander(carry_in, bytes0, bytes1):
    return [
        and_gate(bytes0[0], bytes1[0]),
        and_gate(bytes0[1], bytes1[1]),
        and_gate(bytes0[2], bytes1[2]),
        and_gate(bytes0[3], bytes1[3]),
        and_gate(bytes0[4], bytes1[4]),
        and_gate(bytes0[5], bytes1[5]),
        and_gate(bytes0[6], bytes1[6]),
        and_gate(bytes0[7], bytes1[7]),
    ], OFF

def xorer(carry_in, bytes0, bytes1):
    return [
        xor_gate(bytes0[0], bytes1[0]),
        xor_gate(bytes0[1], bytes1[1]),
        xor_gate(bytes0[2], bytes1[2]),
        xor_gate(bytes0[3], bytes1[3]),
        xor_gate(bytes0[4], bytes1[4]),
        xor_gate(bytes0[5], bytes1[5]),
        xor_gate(bytes0[6], bytes1[6]),
        xor_gate(bytes0[7], bytes1[7]),
    ], OFF
