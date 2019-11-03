#!/usr/bin/env python3
from sender import Challenge

template = solver = '''#!/usr/bin/env python3

import serial
import hashlib

ser = serial.Serial('/dev/ttyACM0', 2000000)


p = [bytes([108+i+j for j in range(32)]) for i in range(32)]
k = [bytes([68+i for j in range(3)]) for i in range(16)]

#     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
p = #RFID_ARRAY#


a = #A_HEX#
b = #B_HEX#

entry = (''.join([''.join(str(x)) for x in p]))
entry += str(a)
entry += str(b)

print(hashlib.sha256(entry.encode('utf-8')).hexdigest())


ser.write(b'p')
for i in range(64):
    ser.write(p[i])
for i in range(16):
    ser.write(k[i])
ser.write(b'\\xaa\\xbb')
'''

ids = ['0','1','2','3','4','5','6','7','8c','9','10','11','8d', '12','13','14','15','17']
idname = [
    'sender0-lounge.py', 
    'sender1-closet.py', 
    'sender2-cafe.py', 
    'sender3-stairs.py', 
    'sender4-mobile.py', 
    'sender5-dance.py', 
    'sender6-code.py', 
    'sender7-blue.py', 
    'sender8-uno.py', 
    'sender9-game.py',  
    'sender10-break.py', 
    'sender11-recess.py', 
    'sender8-bounce.py', 
    'sender12-steel.py', 
    'sender13-caeser.py', 
    'sender14-spiral.py', 
    'sender15-tower.py', 
    'sender17-spire.py', 
]

for i, name in zip(ids, idname):
    print(f'making {name} (challenge: {i})')
    nch = Challenge()
    try:
        nch.load_challenge(i)
    except Exception as exc:
        print(f'sender {name} failed because of {exc}')
        continue
    
    s = template
    s = s.replace('#RFID_ARRAY#', str(nch.p).replace('], [', '],\n[').replace('[', '     [').replace('     [     [', '[['))
    
    s = s.replace('#A_HEX#', hex(nch.a))
    s = s.replace('#B_HEX#', hex(nch.b))

    with open('senders/' + name, 'w') as f:
        f.write(s)
    









