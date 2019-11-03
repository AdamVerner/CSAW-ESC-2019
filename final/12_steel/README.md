  
  
  
after decompilation the challenge with ghidra we get the following code

```c
in = (uint)r.RFID[385] - (uint)r.RFID[387] * (uint)r.RFID[386];
local_5c[0] = (char)in + (char)(in / 0x19) * -0x19 + 0x2d;
printf((Print *)&Serial,"center %x %c\n",(uint)local_5c[0],(uint)local_5c[0]);
```
which is weird, because the local_5c would always equal to 0x2d 
and the solution would work with empty card (it does not)

after inspectiong the dissassembly we found out the decompilation is wrong



```asm
bl         String::String                                   String * String(String * this, c
ldrb.w     r2,[r7,#r.RFID[385]]
ldrb.w     r3,[r7,#r.RFID[386]]
ldrb.w     r1,[r7,#r.RFID[387]]

mul        r3,r1,r3
sub        in,in,r3
ldr        r3,[DAT_00001930]                                = 51EB851Fh
smull      r1,r3,r3,in
asr        r1,r3,#0x3
r1 = 1374389535 * (-r387 * r386) << 3
asr        r3,in,#0x1f
sub        r1,r1,r3
mov        r3,r1
lsl        r3,r3,#0x2
add        r3,r1
lsl        r1,r3,#0x2
add        r3,r1
sub        r1,in,r3
uxtb       r3,r1
add        r3,#0x2d
uxtb       r3,r3
strb.w     r3,[r7,#local_5c]
ldrb.w     r3,[r7,#local_5c]
mov        in,r3
ldrb.w     r3,[r7,#local_5c]
ldr        r1=>s_center_%x_%c_0000b230,[PTR_s_center_%x_%c  = "center %x %c\n"
                                                            = 0000b230
ldr        r0=>Serial,[->Serial]                            =
                                                            = 1fff8e74
bl         Print::printf                                    int printf(Print * this, char *
```

after exhastively running it through debugger we get the formula
```
center = (r.RFID[385] - r.RFID[387] * r.RFID[386]) % 25 + 45;
```


```
...
4765fae13f940050ded3e959089093e7 3e
18c41a53c2be6229deb7711f9d95c8c9 3d
1bb86483cd6dec71551793f94d1ac95f 3c
703224f765d313ee4ed0fadcf9d63a5e 3b <-
9329af69fd45bf4fb15abf5cbe3d1625 3a
d561e48fc0b225b1ed37a6120ab0efd3 39
7a44262a1ea0504030bebe8a674779a8 38
...
```

