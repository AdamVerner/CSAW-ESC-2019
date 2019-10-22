# Chall 6 (code) solution

first off we see some data being pushed on stack and one additional byte from 155 (139+0x10)
```c
data._0_4_ = 0x756a6d69;
data._4_4_ = 0x61727473;
data._8_4_ = 0x6d6f646e;
data._12_4_ = 0x61746164;
data._16_4_ = 0x74616874;
data._20_4_ = 0x6e736168;
data._24_4_ = 0x61656d6f;
data._28_4_ = 0x676e696e;
data._32_4_ = 0x74616877;
data._36_4_ = 0x76656f73;
data._40_4_ = CONCAT13(r.RFID[139],0x217265);
```

also there is a hint
```c
String(&hint,"QmVyZ2VyIEtpbmc=");
```
if  decoded from base64 yeilds `Berger King`.
No idea what that could mean, so skipping it.

then there are calls to H45H class on functions
 - Init
 - Update
 - Final
 - digestChars

the return of digetsChars is compared to some static string

```c
if ( !strcmp(inputHash.digestChars, "242b461d0b97cca55e5d62372b770ab4") )
	v12 = 1;
```

These two facts lead us to belive that H45H is some hash function, after testing the `242b...` in  (HashAnalyzer)[www.tunnelsup.com/hash-analyzer/]
tells us it's either MD5 and MD4.

MD5 is more popular (or at leas was), so let's test that first.

We can control only one byte, that leads to 256 possilbe combinations, that will be really quickly test


```python
from hashlib import md5

s = b'imjustrandomdatathathasnomeaningwhatsoever!'
for key in range(256):
    m = md5(s + key.to_bytes(1, 'little'))
    if (m.hexdigest() == '242b461d0b97cca55e5d62372b770ab4'):
        print('hooooooray')
        print(key, sx, m.hexdigest())
        break

k, p, a, b =  get_start()
set_byte(p, 155, key)
print(get_hash(p, a, b))
```

which work and yeild hash
```
372ded6746e45ef7c8ad5a22c5738a4b5aa982da66bc8a426aa1cca830d05af3
```


