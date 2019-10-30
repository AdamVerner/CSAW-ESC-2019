#!/usr/bin/env python3  

win_text_changed = bytearray(b'\xcb\x83\xc4\xa6\x93r challenge \xb0\xe5Z\xc7*4bcdefghi ')
win_text = bytearray(b'solved challenge cafe abcdefghi ')
haxorz = b'h4x0R2 dr00L'
RFID = [0]*1024

for i in range(6):
    win_text_changed[i] ^= haxorz[i]

    diff = win_text_changed[i] - win_text[i]

    RFID[i + 78] = abs(diff)
    if diff < 0:
        RFID[90] |= (1 << i)

for j in range(17, 23):
    win_text_changed[j] ^= haxorz[j - 11]

    diff = win_text_changed[j] - win_text[j]

    RFID[j + 67] = abs(diff)
    if diff < 0:
        RFID[91] |= (1 << (j-17))

print(RFID[78:92])