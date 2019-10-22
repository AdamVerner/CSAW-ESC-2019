# Challenge 1 (closet)

Challenge 1, called closet, firstly saves the string `ESC19-rocks!` on stack. 

```c
char str[] = "ESC19-rocks!";    // R7+0x40
```

Specifically to location `R7+0x40` where register R7 is used as a kind of a base register.

Next, bytes received from the RFID card on indexes `92` to `115` are copied to an array on stack to location `R7+0x28`. Values of the loop variable (here named `i`) is printed to the serial.

```c
uint8_t data[24];       // R7+0x28
for (int i = 0; i < 24; i++) {
    data[i] = RFID[i+92];
    Print::println(Serial, i);
}
```

Lastly, the bytes from RFID card are used as offsets in the following loop:

```c
bool correct = true;
for (int i = 0; i < 12; i++) {
    if (*((uint8_t*)(R7 + 0x28 + data[i])) != str[i]) {
        correct = false;
    }
}
```

Therefore, our goal is to make the expression `(R7 + 0x28 + data[i])` evaluate in such a way that the resulting pointer points to the initial string `ESC19-rocks!`. We can do that by setting the first 12 bytes of `data` array to values `24, 25, 26, ..., 34, 35`. The result then points to `R7 + 0x28 + 0x18 = R7 + 0x40` which is the same location as the desired char array.

In sender.py, we can simply set the desired bytes like so:

```python
p[5] = [0]*12 + [24,25,26,27]
p[6] = [i+28 for i in range(8)] + [0]*8
```

Resulting solution hash is `293f7b60b994512db99836ae7d5bab88b2d0089f90fcf6d51b95b374200dc20f`.