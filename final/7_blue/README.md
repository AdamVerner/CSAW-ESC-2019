# Challenge 7 (blue)

hint: `time to use that blue tag`

8 important bytes in memory of blue tag at offset 960: `5d9295a4b98018b5`

hash that has to be computed from the 8 bytes at RFID[960]: `0e14a8412724702ff129b6c2d0e2984bff0138ef49f1c0e71fcc31ef2c7fbe1f`

mifare key A for sector 0x3F that we had to reverse engineer from the AVR binary: `5d6a0064f591`


an attempt for sender.py (not functional):
```
data = bytes.fromhex('5d9295a4b98018b5')
offset = 960
for i, b in enumerate(data):
    self.set_byte(i + offset, b)
key = bytes.fromhex('5d6a0064f591')
for i, b in enumerate(key):
    self.set_byte(i + 0x3f0, b)
```
