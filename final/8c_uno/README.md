# Chall 6 (code) solution

This challenge has a hint at the start
```c
String(&hint,"SXMgT0lTQyAxMzM3Pw==");
```

which translates to `is OISC 1337`
OISC is an abbreviation of *One instruction set computer*  
some examples of these lanngues could be found on [wikipedia][1]

Then there is modifed challenge answer, right away we can see that it's rot3 encoded string
```bash
vroyhg#fkdoohqjh#xqr#defghijklm
# after rot 3
solved challenge uno abcdefghij
```

After that, there are two parts of RFID memmory card which get copied to buffer
```
  while (i < 0x30) {
    buff[i] = (int)(char)r.RFID[i + 0x1f0];
    i = i + 1;
  }
  j = 0;
  while (j < 0x10) {
    buff[j + 0x30] = (int)(char)r.RFID[j + 0x230];
    j = j + 1;
  }
```
The memmory is divided into 2 block such that you you don't overwrite the card keys 

The ghidra decompilation is little hard to read, because there are gotos, 
but after spending some time shuffling with the code and looking at the function graph, 
we notice that it is an implemntation of [subleq][2].

 - if `*b` is -1 one byte from `*a` is appended to challHash
 - if `ptr` is > 60 or `*a` is -1 execution ends
 - everything else is same as **subleq**
 
after writing a simple subleq virtual machine and debugger in python we start to work on the subleq code
 
pseudocode is: 
```
# handy constants
for x in {63..94}
    m[x] -= 3;
    challHash_write(m[x])
exit()
```

To implement this in subleq was quiet tricky, but using our debugger made everything much simpler.

The final *subleq* script along with the vm and debugger code can be found inside solver.py

As many others, this challenge does have multiple possible solution, our is only one of them.


```
2e120f2237c71f18d29451c4787ac1df8285909618e2a821ee7c97d7efde246c
```



[1]: https://en.wikipedia.org/wiki/One_instruction_set_computer
[2]: https://esolangs.org/wiki/Subleq


