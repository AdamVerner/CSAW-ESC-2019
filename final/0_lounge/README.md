# Challenge 0 (lounge)

There is a lot of things happening in the challenge fuction, but only few lines of code are important. The final comparison which determines if the challenge was solved correctly is:
```c
x * y == 6319
```

The number `6319` has only two factors, which are `71` and `89`. These are the values for `x` and `y` that we are looking for.

Therefore we need to find how the variables `x` and `y` are set. They are set as follows:

```c
doubleX = __aeabi_i2d(
                    (packet.RFID[76] >> 4 & 1) * 1+
                    (packet.RFID[77] >> 6 & 1) * 2 +
                    (packet.RFID[77] >> 3 & 1) * 4 + 
                    (packet.RFID[77] >> 0 & 1) * 8 +
                    (packet.RFID[76] >> 7 & 1) * 0x10 +
                    (packet.RFID[76] >> 1 & 1) * 0x20 +
                    (packet.RFID[77] >> 7 & 1) * 0x40);

doubleY = __aeabi_i2d(
                    (packet.RFID[77] >> 5 & 1) * 1 +
                    (packet.RFID[76] >> 0 & 1) * 2 +
                    (packet.RFID[77] >> 1 & 1) * 4 +
                    (packet.RFID[76] >> 6 & 1) * 8 +
                    (packet.RFID[76] >> 5 & 1) * 0x10 +
                    (packet.RFID[76] >> 2 & 1) * 0x20 +
                    (packet.RFID[77] >> 5 & 1) * 0x40);

int x = __aeabi_d2iz(doubleX);
int y = __aeabi_d2iz(doubleY);
```

Per the [ARM run-time ABI documentation][1], the function `__aeabi_i2d` converts an integer value to double.

Function `__aeabi_d2iz` converts double to integer using C-style conversion. Basically it just returns the integer part of a floating point number.

The 76th and 77th byte of the card memory have to be set in such a way that the bit shifting magic above evaluates to the desired values for `x` and `y`. We can achieve that by reversing the bit shifts.

```python
#!/usr/bin/env python3

x = 71
y = 89

rfid76 = (((x >> 4) & 1) << 7) |    \
            (((y >> 3) & 1) << 6) | \
            (((y >> 4) & 1) << 5) | \
            (((x >> 0) & 1) << 4) | \
            (((y >> 5) & 1) << 2) | \
            (((x >> 5) & 1) << 1) | \
            (((y >> 1) & 1) << 0)

rfid77 = (((x >> 6) & 1) << 7) |    \
            (((x >> 1) & 1) << 6) | \
            (((y >> 0) & 1) << 5) | \
            (((y >> 6) & 1) << 5) | \
            (((x >> 2) & 1) << 3) | \
            (((y >> 2) & 1) << 1) | \
            (((x >> 3) & 1) << 0)
```

This challenge actually has two possible solutions as the values of `x` and `y` can be swapped and the product is still the same.

```python
set_byte(p, 76, 112); set_byte(p, 77, 232)
```
`643a6fa20b171fdf3a9e7e1975ce62892fde9cecf2056a73d85fa2d0802d3000`

```python
set_byte(p, 76, 145); set_byte(p, 77, 163)
```
`6cd6ab9911818564e4f58cc5c25472a1c177917879210b077a728d96c23ccd83`

[1]: http://infocenter.arm.com/help/topic/com.arm.doc.ihi0043d/IHI0043D_rtabi.pdf