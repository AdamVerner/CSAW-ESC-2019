#!/bin/env/python3
mem = [

	# 61 = 0  # just zerp
	# 62 = 1  # +1 increment
	# 63 = 3  # ROT
	

	# create -1 to use in pointer increase
	62, 60, 3, # 0

	# decrement the string, then jump to addr 15
	# uses 
	63, 64, 0, # 3   # decrese the first char by 1
	62, 10, 9,   # 6  decrement next B to -1
	64, 0, 0,   # 9  write  from pointer to out
	
	# reset the previous b to 0, so we can use it again
	10, 10, 15,   # 12

	# increase the index pointer and copy pointer
	60, 4, 0,  # 15
	60, 9, 0,  # 18
	
	# 57 is the number of chars processed
	62, 57, 27, # 21 go to end if there are less than 30 chars
	
	61, 61, 3, # 24    # 0-0 always go to begging
	
	62, 30, 30, # 27  # set next A to -1(break) and jump there
	0, 0, 0, # 30    # end program
	
	0, 0, 0, # 33
	0, 0, 0, # 36
	0, 0, 0, # 39
	0, 0, 0, # 42
	0, 0, 0, # 45
	0, 0, 0, # 48
	0, 0, 0, # 51
	0, 0, 0, # 54
	31, 0, 0, # 57
	
	0,  0,  1, # 60
	3, 118, 114, # 63
	111, 121, 104, # 66
	103, 35, 102, # 69
	107, 100, 111, # 72
	111, 104, 113, # 75
	106, 104, 35, # 78
	120, 113, 114, # 81
	35, 100, 101, # 84
	102, 103, 104, # 87
	105, 106, 107, # 90
	108, 109, # 93
]
print(mem)
print(mem[0x40])
print(len(mem))
assert len(mem) == 95

out = ['\x00'] * 32

j = 0
ptr = 0
inp = 242
stp = -1
while ptr >= 0:

	stp += 1

		
		
	# fetch instructions
	a = mem[ptr]
	b = mem[ptr+1]
	c = mem[ptr+2]
	ptr += 3
	
				
	

	if not inp:
			# print memmory 
		for x in range(0, 95, 3):
			print('[%d]' % x, end=' ')
			for y in mem[x:x+3]:
				print (y, end = ' ')
			print()
		
		print(''.join([chr(x) for x in mem [64:]]))
		print('out = %s' % ''.join(out))
		print('step ', stp)
		print('ptr = %d;    %d, %d, %d' % (ptr-3, a, b, c))
		print('[ptr] %d;   %d, %d, %d; -> %d' % (mem[ptr-3], mem[a], mem[b], mem[c], mem[b] - mem[a]))
		
		inp = input('?')
		try:
			inp = int(inp)
		except:
			inp = 1
			
	inp -= 1
	
	
	# logic
	
	if ptr > 60:
		break
	
	if 	a == -1: 
		print('requested stop')
		break
	
	if b != -1 or j > 30:
		mem[b] -= mem[a]
		if mem[b] <= 0:
			ptr = c;
		
	else:
		out[j] = chr(mem[a])
		j += 1
		
print(''.join(out))
print('done')
print('solved challenge uno abcdefghij')