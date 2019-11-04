#!/usr/bin/env python3

from hashlib import sha256
from serial import Serial
from sys import argv
import struct

class Challenge():
    
    def __init__(self):
        self.a = 0
        self.b = 0
        self.k = [bytes([68+i for j in range(3)]) for i in range(16)]
        self.p = [[0]*16 for i in range(64)]
        
    def verify(self):
        try:
            for i in range(3, 64, 4):
                assert self.p[i] == [0]*16
        except AssertionError:
            print(f'Block #{i} is not writable')
            exit(1)
        
    def get_hash(self):
        self.verify()   
        entry = (''.join([''.join(str(x)) for x in self.p]))
        entry += str(self.a)
        entry += str(self.b)
        return sha256(entry.encode('utf-8')).hexdigest()
        
    def set_byte(self, index, value):
        assert value <= 0xff
        sector = index // 16
        byte = index % 16
        if self.p[sector][byte]:
            print('overwriting already set memory at %d' % index)
        self.p[sector][byte] = value
        
    def set_bytes(self, offset, bytes):
        for idx, value in enumerate(bytes):
            self.set_byte(offset + idx, value)

        
    def send(self, port='/dev/ttyACM0'):
        self.verify()   
    
        print('sending : ', self.get_hash())
   
        serial = Serial(port, 2000000)
        serial.write(b'p')
        for i in range(64):
            serial.write(self.p[i])

        for i in range(16):
            serial.write(self.k[i])

        serial.write(b'\xaa\xbb')
        print('Hash successfully sent to device');
        serial.close()
        
    def load_challenge(self, identificator:str):
    
        if identificator == 'all':
            for iden in self.identificators()[:-1]:
                try:
                    self.load_challenge(iden)
                except Exception as exc:
                    print(exc.args[0])
            return
        
        if identificator == '0':  # A - lounge
            self.set_byte(76, 112)
            self.set_byte(77, 232)
            # 643a6fa20b171fdf3a9e7e1975ce62892fde9cecf2056a73d85fa2d0802d3000
        
        elif  identificator == '0a':  # A - lounge (second variant)
            self.set_byte(76, 145)
            self.set_byte(77, 163)
            # 6cd6ab9911818564e4f58cc5c25472a1c177917879210b077a728d96c23ccd83
        
        elif  identificator == '1':  # A - closet
            self.set_bytes(92, range(24, 36))
            # 293f7b60b994512db99836ae7d5bab88b2d0089f90fcf6d51b95b374200dc20f
        
        elif  identificator == '2':  # A - cafe
            a = [48, 72, 80, 32, 92, 36, 45, 32, 62, 146, 6, 23, 32, 20]
            # self.set_bytes(78, a)
            for i in range(len(a)):
                self.set_byte(i+78, a[i])
            # 851a72b7fa00d1888fdcfecc5ccf5359c45b2003e2b5350e92798507c82f09a1
            
        elif  identificator == '3':  # A - stairs
            self.p[4] = [0x4a, 0x5c, 0x4c, 0x3e, 0x36, 0x22, 0x7d, 0x60, 0x6c, 0x64, 0x7c, 0x2e, 0, 0, 0, 0]
            # 396f4b1cdf1cc2e7680f2a8716a18c887cd489e12232e75b6810e9d5e91426c7

        elif  identificator == '4':  # B - mobile
            a = [17, 16, 51, 1, 4, 68, 4, 68, 2, 32, 85, 3, 2, 32]
            for i in range(len(a)):
                self.set_byte(i+132, a[i])
            # 807548c85963e9f9aa9921cb344997ccfe57ba91cd00f13122c2f15e5b3a70d1    
        
        elif  identificator == '5':  # B - dance
            sol = b'password'
            for i in range(len(sol)):
                self.set_byte(i + 147, sol[i])
            # e631b32e3e493c51e5c2b22d1486d401c76ac83e3910566924bcc51b2157c837

        elif  identificator == '6':  # B - code
            # 372ded6746e45ef7c8ad5a22c5738a4b5aa982da66bc8a426aa1cca830d05af3
            self.set_byte(155, ord(b'L'))
    
        elif  identificator == '7':  # B - 
            data = bytes.fromhex('5d9295a4b98018b51dd9213c2aef00cc6abc1ffbd341d88226fed70d4b6449dc55c57178fd1034da11e073ba2d6f2f45')
            # data = bytes.fromhex('5d9295a4b98018b5')
            for i, b in enumerate(data):
                self.set_byte(i + 960, b)

            # Should set key A for sector 0x3F (not working with sender.py)
            key = bytes.fromhex('5d6a0064f591')
            for i, b in enumerate(key):
                self.set_byte(i + 0x3f0, b)
        
        elif  identificator == '8c':  # C - Uno
            # one of many solutions
            mem1 = [62, 60, 3, 63, 64, 0,62, 10, 9,64, 0, 0,10, 10, 15,60, 4, 0, 60, 9, 0, 62, 57, 27, 61, 61, 3, 62, 30, 30]
            mem2 = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 0, 0, 0,  0,  1, 3]
            for off in range(len(mem1)):
                self.set_byte(0x1f0+16+off, mem1[off])
            for off in range(len(mem2)):
                self.set_byte(0x230+16+off, mem2[off])
            # 2e120f2237c71f18d29451c4787ac1df8285909618e2a821ee7c97d7efde246c
        
        elif  identificator == '9':  # C - game
            self.set_byte(0x9c, 0x02)  # y = 0 x = 2
            self.set_byte(0x9d, 0x10)  # y = 1 x = 0
            self.set_byte(0x9e, 0x21)  # or 0x22 for different flag
            # a536829856d84ccd53ff8bcf534a65c5678bdbe9ce20f78407e1c987ba517e8a
        
        elif  identificator == '9a':  # C - game
            self.set_byte(0x9c, 0x02)
            self.set_byte(0x9d, 0x10)
            self.set_byte(0x9e, 0x22)
            # 63c0b41f89bbf493ba791c092b3e5473e243b9c16666f1e5eaa82bc52eeb1613
        
        elif  identificator == '10':  # C - break
            # d19ead7568e53d7fa072df4b36662ee35d2bf53dab39fbe3580895633ef861a7
            self.set_byte(143+0x10, 0x41)
            self.set_byte(144+0x10, 0x61)
        
        elif  identificator == '11':  # C - recess
            # 4c1f09387311c2e55c864f5ce02b08aa93104269144e44fc2aa5a171735dfab2
            a = list(b'g00d')
            for i in range(len(a)):
                self.set_byte(i+161, a[i])
        elif  identificator == '8d':  # D - bounce
            raise Exception("8d is not solved yet")
            
        elif  identificator == '12':  # D - steel
            self.set_byte(401, 14)
            # 5921d2ca353338c5f04c92205dc8f8bc8734f092a9e63e5f02ec106f7a7d99b4
            
        elif  identificator == '13':  # D - caeser
            # 551b5cff372d310b57d39b616400461be0a1450c519a2a542f33a7af0dd565f3
            self.set_byte(400 + 0x10, 242)
            self.set_byte(417, 169)
            self.set_byte(418, 66)
            self.set_byte(419, 97)
            self.a = 171 >> 4   # A = 10
            self.b = 171 & 0xf  # B = 11

        elif  identificator == '14':  # D - spiral
            a = bytes.fromhex('cafefade')
            # 6fd4edcfdb3a0289ac07472d65ed410d1dbca321ca5833c66560a30ede110db1
            for i in range(len(a)):
                self.set_byte(i+381+16, a[i])
        elif  identificator == '15':  # D - tower
            raise Exception("15 is ot solved yet")
        elif  identificator == '17':  # D - spire
            
            a = struct.pack('<i', -12)[::-1]
            for i in range(len(a)):
                self.set_byte(644+i, a[i])
            self.set_byte(879, 1)
            a = b'\x74\x76\x00\x20'[::-1]
            for i in range(len(a)):
                self.set_byte(719-1-i, a[i])
            for i in range(4):
                self.set_byte(719-9-i, 1)
            # f322344822257bb66542629db08bcea285411068963e30f0595847c79ef76f37
            
        else:
            raise Exception("Invalid Identificator")
        
    def identificators(self):
        ids = [
            '0',
            '0a',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8c',
            '9',
            '9a',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '8d',
            '17', 
            'all',
        ]
        return ids
    



if __name__ == "__main__":

    c = Challenge()

    if len(argv) < 2 or argv[1] not in c.identificators():
        print(f'Usage: {argv[0]} ID [COMMAND [PORT]] ')
        
        print('known ids:', ', '.join(c.identificators()) )
        
        exit(1)

    c.load_challenge(argv[1].lower())
    
    if c.a:
        print("set 'a' to", c.a)
    if c.a:
        print("set 'b' to", c.b)
    
    if len(argv) >= 3:
        cmd = argv[2].lower()
    else:
        cmd = 'hash'
    
    if cmd == 'send':
        if len(argv) == 4:
            c.send(argv[3])
        else:
            c.send()
        
    elif cmd == 'hash':
        print(c.get_hash())
