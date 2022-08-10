import codecs

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
