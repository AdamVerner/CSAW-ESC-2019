# Challenge 2 (cafe)

This challenge begins by definining two character arrays: mangled challenge success message and some other text.

```c
char winText[] = "\xcb\x83\xc4\xa6\x93r challenge \xb0\xe5Z\xc7*4bcdefghi ";
char haxorz[] = "h4x0R2 dr00L";
```

We know that we need to demangle the message (here named `winText`) so that it says `solved challenge cafe abcdefghi `. The message has 12 bytes changed in total, 6 bytes at offset 0 and 6 bytes at offset 17.

The challenge code continues with the following loops.

```c
for (int i = 0; i < 6; i++) {
    winText[i] ^= haxorz[i];

    if (((packet.RFID[90] >> i) & 1) == 0) {
        winText[i] -= packet.RFID[i + 78];
    } else {
        winText[i] += packet.RFID[i + 78];
    }
}
```

The first loop changes the first group of mangled bytes. For each byte, it xors it with a character from `haxorz` array and then depending on bit *i* from `packet.RFID[90]` adds or subtracts byte `packet.RFID[i + 78]`.

```c
for (int j = 17; j < 23; j++) {
    winText[j] ^= haxorz[j - 11];

    if (((packet.RFID[91] >> (j - 17)) & 1) == 0) {
        winText[j] -= packet.RFID[j + 67];
    } else {
        winText[j] += packet.RFID[j + 67];
    }
}
```

The second loop does the same thing with minor differences. It operates with the 6 bytes at offset 17, select addition or subtraction by bits in byte `packet.RFID[91]` and adds or subtracts value from byte `packet.RFID[i + 67]`.

We can solve this challenge by simply xoring the mangled message bytes with corresponding characters in the `haxorz` text and then calculating the difference between the resulting value and correct success message bytes. The loop for solving the first 6 bytes looks like this:

```python
for i in range(6):
    win_text[i] ^= haxorz[i]

    diff = win_text[i] - win_text_correct[i]

    RFID[i + 78] = abs(diff)
    if diff < 0:
        RFID[90] |= (1 << i)
```

Second loop with rest of the solution can be found in [solve.py](solve.py) script.


The solution hash is `851a72b7fa00d1888fdcfecc5ccf5359c45b2003e2b5350e92798507c82f09a1`.