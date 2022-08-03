import  sys
print(sys.getdefaultencoding())

print(ord('a'))
print(chr(97))

s = 'hello'
enc_ascii = s.encode('ascii')
enc_utf8 = s.encode('utf8')
enc_utf16 = s.encode('utf16')

print(enc_ascii)
print(enc_utf8)
print(enc_utf16)

#
str_in_bytes = b'hello'
str_in_bytes = s.encode('utf8')

str_in_text = 'hello'

print(type(str_in_bytes))
print(type(str_in_text))

ba = bytearray(b'hello')
ba[0] = 87
print(ba)

result = str(str_in_bytes, 'utf8')
print(result)

result2 = str_in_bytes.decode('utf8')
print(result2)


jpeg = [120, 3, 255, 0, 100]
with open(r'btest.bin', 'w+b') as file:
    file.write(bytes(jpeg))

with open(r'btest.bin', 'rb') as file:
    data = file.read()
    for b in data:
        print(int(b))