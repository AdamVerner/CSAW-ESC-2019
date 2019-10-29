# Challenge 14 (spiral)

Main code of this challenge looks like this:

```c
uVar1 = uVar2 + byteswap(uVar1) ^ 0xbeef;
uVar2 = uVar1 ^ rol(uVar2, 3);
uVar1 = uVar2 + byteswap(uVar1) ^ 0x9bb0;
uVar2 = uVar1 ^ rol(uVar2, 3);
uVar1 = uVar2 + byteswap(uVar1) ^ 0xb499;
uVar2 = uVar1 ^ rol(uVar2, 3);

if (uVar1 == 0xa29f && uVar2 == 0xd481) {
    correct = true;
}
```

where `uVar1` and `uVar2` are saved in bytes from 397 to 401 on the RFID card. Therefore, to solve this challenge, we need to set the mentioned bytes so that the variables evaluate to correct values after the operations above (`0xa29f` and `0xd481`).

Thanks to the fact, that no information is lost during the operations, we can simply reverse their order to get the original values, like so:

```c
uint16_t uVar1 = 0xa29f;
uint16_t uVar2 = 0xd481;

uVar2 = ror(uVar2 ^ uVar1, 3);
uVar1 = byteswap((uVar1 ^ 0xb499) - uVar2);
uVar2 = ror(uVar2 ^ uVar1, 3);
uVar1 = byteswap((uVar1 ^ 0x9bb0) - uVar2);
uVar2 = ror(uVar2 ^ uVar1, 3);
uVar1 = byteswap((uVar1 ^ 0xbeef) - uVar2);

printf("%hx %hx\n", uVar1, uVar2);
```

The resulting values are `0xcafe` and `0xfade` which we can save to the RFID card by the python code below.

```python
a = bytes.fromhex('cafefade')
for i in range(len(a)):
    set_byte(p, i+381+16, a[i])
```

And the challenge solution hash is `6fd4edcfdb3a0289ac07472d65ed410d1dbca321ca5833c66560a30ede110db1`.