#!/usr/bin/env python3

from hashlib import sha256
from serial import Serial
from sys import argv


def get_hash(p, a, b):
    entry = (''.join([''.join(str(x)) for x in p]))
    entry += str(a)
    entry += str(b)
    return sha256(entry.encode('utf-8')).hexdigest()


def set_byte(p, index, val):
    sector = index // 16
    byte = index % 16
    p[sector][byte] = val


if __name__ == "__main__":
    if len(argv) < 2:
        print(f'Usage: {argv[0]} <send|hash>')
        exit(1)

    cmd = argv[1]
    if cmd not in ['send', 'hash']:
        print('Unrecognized command')
        exit(1)


    k = [bytes([68+i for j in range(3)]) for i in range(16)]
    p = [[0]*16 for i in range(64)]
    a = 0x0
    b = 0x0

    # Chall 0 (lounge) solutions: (ask if there can be two -> https://github.com/TrustworthyComputing/csaw_esc_2019/issues/8)
    # 643a6fa20b171fdf3a9e7e1975ce62892fde9cecf2056a73d85fa2d0802d3000
    # set_byte(p, 76, 112); set_byte(p, 77, 232)
    # 6cd6ab9911818564e4f58cc5c25472a1c177917879210b077a728d96c23ccd83
    # set_byte(p, 76, 145); set_byte(p, 77, 163)

    # Chall 1 (closet) solution
    # 293f7b60b994512db99836ae7d5bab88b2d0089f90fcf6d51b95b374200dc20f
    # p[5] = [0]*12 + [24,25,26,27]
    # p[6] = [i+28 for i in range(8)] + [0]*8

    # Chall 2 (cafe) solution
    # 851a72b7fa00d1888fdcfecc5ccf5359c45b2003e2b5350e92798507c82f09a1
    # a = [48, 72, 80, 32, 92, 36, 45, 32, 62, 146, 6, 23, 32, 20]
    # for i in range(len(a)):
    #     set_byte(p, i+78, a[i])

    # Chall 3 (stairs) solution
    # 396f4b1cdf1cc2e7680f2a8716a18c887cd489e12232e75b6810e9d5e91426c7
    # p[4] = [0x4a, 0x5c, 0x4c, 0x3e, 0x36, 0x22, 0x7d, 0x60, 0x6c, 0x64, 0x7c, 0x2e, 0, 0, 0, 0]

    # Chall 4 (mobile) solution
    # 807548c85963e9f9aa9921cb344997ccfe57ba91cd00f13122c2f15e5b3a70d1
    # a = [17, 16, 51, 1, 4, 68, 4, 68, 2, 32, 85, 3, 2, 32]
    # for i in range(len(a)):
    #     set_byte(p, i+132, a[i])

    # Chall 5 (dance) solution
    # e631b32e3e493c51e5c2b22d1486d401c76ac83e3910566924bcc51b2157c837
    # sol = b'password'
    # for i in range(len(sol)):
    #     set_byte(p, i + 147, sol[i])
    # from IPython import embed; embed()

    # Chall 6 (code) solution
    # 372ded6746e45ef7c8ad5a22c5738a4b5aa982da66bc8a426aa1cca830d05af3
    # set_byte(p, 155, ord(b'L'))
	
    # Chall 8 uno solution
    # mem1 = [62, 60, 3, 63, 64, 0,62, 10, 9,64, 0, 0,10, 10, 15,60, 4, 0,
    #     60, 9, 0, 62, 57, 27, 61, 61, 3, 62, 30, 30]
    # mem2 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0,  0,  1, 3]
    # for off in range(len(mem1)):
    #     set_byte(p, 0x1f0+16+off, mem1[off])
    # for off in range(len(mem2)):
    #     set_byte(p, 0x230+16+off, mem2[off])
	# 2e120f2237c71f18d29451c4787ac1df8285909618e2a821ee7c97d7efde246c
	
	
	# Chall 9 game solution
    # set_byte(p, 0x9c, 0x02)
    # set_byte(p, 0x9d, 0x12)
    # set_byte(p, 0x9e, 0x10) #    set_byte(p, 0x9e, 0x22)
	# either
	# 96411a826eba4299493b6f1e29b3cb278ab9f2c3f47300b37d0588656145d513
	# or 
	# 03fe0fec145adf7d629e6471822a145d9920536658a80f9d2c1694ebc174cecf

    # Chall 10 (break)
	# d19ead7568e53d7fa072df4b36662ee35d2bf53dab39fbe3580895633ef861a7
    # set_byte(p, 143+0x10, 0x41)
    # set_byte(p, 144+0x10, 0x61)

    # 	Chall 11 (recess) solution
    # 4c1f09387311c2e55c864f5ce02b08aa93104269144e44fc2aa5a171735dfab2
    # a = list(b'g00d')
    # for i in range(len(a)):
    #     set_byte(p, i+161, a[i])

    # Chall 13 (caeser)
    # 551b5cff372d310b57d39b616400461be0a1450c519a2a542f33a7af0dd565f3
    # set_byte(p, 400 + 0x10, 242)
    # set_byte(p, 417, 169)
    # set_byte(p, 418, 66)
    # set_byte(p, 419, 97)
    # a = 171 >> 4   # A = 10
    # b = 171 & 0xf  # B = 11

    # Chall 14 (spiral)
    # 6fd4edcfdb3a0289ac07472d65ed410d1dbca321ca5833c66560a30ede110db1
    # a = bytes.fromhex('cafefade')
    # for i in range(len(a)):
    #     set_byte(p, i+381+16, a[i])


    # Blocks 3, 7,... are where the MIFARE keys are stored, (probably) can't be used
    try:
        for i in range(3, 64, 4):
            assert p[i] == [0]*16
    except AssertionError:
        print(f'Block #{i} is not writable')
        exit(1)


    if cmd == 'send':
        print(get_hash(p,a,b))
        # serial = Serial('/dev/ttyACM0', 2000000)
        serial = Serial('COM3', 2000000)            
        serial.write(b'p')

        for i in range(64):
            serial.write(p[i])

        for i in range(16):
            serial.write(k[i])

        serial.write(b'\xaa\xbb')
    elif cmd == 'hash':
        print(get_hash(p,a,b))
