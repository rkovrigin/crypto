import codecs
import binascii


def strxor(s1,s2):
    r = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
    return r




# print strxor(strxor(codecs.decode("09e1c5f70a65ac519458e7e53f36", 'hex'), "attack at dawn"), "attack at dusk").encode('hex')
print strxor(strxor(codecs.decode("09e1c5f70a65ac519458e7e53f36", 'hex'), "attack at dawn"), "attack at dusk").encode('hex')
# r1 = strxor(codecs.decode("09e1c5f70a65ac519458e7e53f36", "hex"), "attack at dawn")
# print(r1)
# r2 = strxor(r1, "attack at dawn")
# print(r2)
# t = ''.join(chr(i) for i in r2)
# print([hex(ord(i)) for i in t])

# r = strxor(r, "attack at dawn")
# print(binascii.hexlify(r))
# r2 = strxor2(r, "attack at dusk")

# strxor1("09e1c5f70a65ac519458e7e53f36", "attack at dawn")