import codecs
import struct

import mips

print(eval("~0b1010 & ~0b0110"))
print(10 << 3)
string = "00616c6f"
byte_array = bytearray.fromhex(string)
byte_array.decode()
print(byte_array.decode()[::-1])
print(string[2:])
print(str(hex(int("1634627442")))[2:])
print(codecs.encode(b"\0alo", "hex"))



a = {
"268500992": 1634627442,
    "268500996": 544171116,
    "268501000": 1919184754,
    "268501004": 1702193001,
    "268501008": 115
}
t = 'rodrigues\n'
print(t[:4][::-1])
while len(t) > 0:
    print(t[:4][::-1])
    print(int(codecs.encode(bytes(t[:4][::-1], 'utf-8'), "hex").zfill(8), 16))
    t = t[4:]


print(int(list(a)[len(a)-1]))

mips.registradores[4] = 12

print({x: v for x, v in mips.registradores.items() if v != 0 and v != "00000000"})


def float_to_bin(num):
    bits, = struct.unpack('!I', struct.pack('!f', num))
    return "{:064b}".format(bits)


def ieee745(N): # ieee-745 bits (max 32 bit)
    a = int(N[0])        # sign,     1 bit
    b = int(N[1:9],2)    # exponent, 8 bits
    c = int("1"+N[9:], 2)# fraction, len(N)-9 bits

    return (-1)**a * c /( 1<<( len(N)-9 - (b-127) ))

N = "110000011010010011"  # str of ieee-745 bits
print( ieee745(N)  )  # -->  -20.59375

print(float_to_bin(10293789124142343428374274873917237.27))

print(list(mips.registradores.keys())[2])
print(mips.opcode['001000'].__name__)
