"""
Suppose you are told that the one time pad encryption of the message "attack at dawn" is 09e1c5f70a65ac519458e7e53f36

(the plaintext letters are encoded as 8-bit ASCII and the given ciphertext is written in hex).
What would be the one time pad encryption of the message "attack at dusk" under the same OTP key?
"""

import codecs
import binascii


text = "attack at dawn"
enc = "09e1c5f70a65ac519458e7e53f36"
h = codecs.decode(enc, 'hex')

def myxor(ar, str):
    return [a ^ ord(b) for a, b in zip(ar, str)]


out1 = myxor(codecs.decode(enc, 'hex'), text)
print(out1)
out2 = myxor(out1, text)
print([hex(i) for i in out2])
print([chr(i) for i in out2])
print(codecs.encode(bytearray(out2), 'hex'))