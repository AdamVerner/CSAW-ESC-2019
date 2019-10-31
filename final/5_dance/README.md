as first step, the challenge pushes some data on stack

renaming and restructuring data it looks like this:
```c
data._0_4_ = 0x20202020;
data._4_4_ = 0x20202020;

check._0_4_ = 0x9848885e;
check._4_4_ = 0x710428da;
check._8_4_ = 0x6fe5d051;
check._12_4_ = 0x2729c68d;
check._16_4_ = 0xd3d6073;
check._20_4_ = 0xd6bdab6a;
check._24_4_ = 0x72ef112a;
check._28_4_ = 0xd842151d;
```

after that the data variable gets overwriten with contents of rfid memmory.

specifically 8 bytes from offset 0x93
```c
i = 0;
while (i < 8) {
  data[i] = r.RFID[i + 0x83];
  i = i + 1;
}
```

then there is piece of code that initializes blake256 and calculates the hash of `data`
and then compares each byte with `check`

first idea was to bruteforce the data locally (it's just 8 bytes).
using simple python script to try all possible combinations:
```python
hsh = (int.from_bytes(b'', 'little')).to_bytes(8, 'little')
while True:
    hsh = (int.from_bytes(hsh, 'little') + 1).to_bytes(8, 'little')
    if blake2s(hsh).hexdigest() == '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8':
        print('password found: ', hsh)
        break
    if hsh == b'\x00' * 8:
        # catch overrun
        print('no password found')
        break
```

but before that script finnished, using google i found out that the hex equals to sha256 of `password`

https://md5hashing.net/hash/sha256/5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8

which was weird, as the challenge was calling blake256 (sha256 uses different algorithm)

but after sending the 'password' in the rfid memmory at offset 0x93 it worked.
Which was unexpected behavior, but we stuck with our anwer.


using our modified solver to get the hash
```python
k, p, a, b =  get_start()
sol = b'password'
for i in range(len(sol)):
    set_byte(p, i + 0x93, sol[i])
get_hash(p, a, b)
```
getting the hash:

```
e631b32e3e493c51e5c2b22d1486d401c76ac83e3910566924bcc51b2157c837
```
