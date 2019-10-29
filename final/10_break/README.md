# Chall 10 Break

```c
  var = 0xace1;
  i = 0;
  while (i < 0x656) {
    var = ((ushort)((int)(uint)var >> 5) ^
          (ushort)((int)(uint)var >> 3) ^ var ^ (ushort)((int)(uint)var >> 2)) << 0xf |
          (ushort)((int)(uint)var >> 1);
    i = i + 1;
  }
```

the value of variable `var` is checked  against 
```c
(ushort)(((ushort)r.keys[32] & 0xf) << 4 | (ushort)r.RFID[144] | ((ushort)r.RFID[143] | (ushort)r.keys[32] & 0xf0) << 8) 
```
The first part is static no matter what we change. We can run it locally. (see solve.c)


```
$ gcc solve.c
$ ./a.out
16737 (0x4161)
```

for the second part the simplest solution is setting
byte 143 to 0x41
byte 144 to 0x61
and both a and b to 0


and it works!
```
d19ead7568e53d7fa072df4b36662ee35d2bf53dab39fbe3580895633ef861a7
```

but there are many more ways to solve it.

giving our constrain to z3 we get 

1208370192830918 possible combinations (with different hashes)

this was solved using z3, see more in solve.py



