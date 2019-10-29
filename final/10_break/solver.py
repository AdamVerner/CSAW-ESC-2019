from z3 import *
s = Solver()

r144 = BitVec('r144', 8)
r143 = BitVec('r143', 8)
buttons = BitVec('buttons', 8)

s.add(  ( (16 * buttons) | r144 | (r143 << 8) | (buttons << 8) & 0xF000) == 0x4161)
s.check()
print(s.model())

