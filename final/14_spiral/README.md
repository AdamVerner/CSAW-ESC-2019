

we have to reverse this

```c
  p1 = _byteswap_ushort(*&r.RFID[381]);
  v14 = _byteswap_ushort(*&r.RFID[383]);
  ctxt_one = (v14 + ((p1 << 8) | (p1 >> 8))) ^ 0xBEEF;
  v6 = ctxt_one ^ ((v14 >> 13) | 8 * v14);
  v7 = (v6 + ((ctxt_one << 8) | (ctxt_one >> 8))) ^ 0x9BB0;
  v8 = v7 ^ ((v6 >> 13) | 8 * v6);
  v17 = 26909;
  v16 = -19303;
  v9 = (v8 + ((v7 << 8) | (v7 >> 8))) ^ 0xB499;
  ctxt_two = v9 ^ ((v8 >> 13) | 8 * v8);
  check = v9 == 41631 && ctxt_two == 54401;
```
