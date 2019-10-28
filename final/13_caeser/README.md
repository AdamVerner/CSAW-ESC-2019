# Challenge 13 (caeser)


at start there is a hint
```c
String(&hint,"V2hhdCBpcyBUdW5nc3Rlbi1BPw==");

$echo V2hhdCBpcyBUdW5nc3Rlbi1BPw== | base64 --decode 
What is Tungsten-A
```

As with the previous hints, we had no idea what that means.


Starting from the bottom to complete the challenge the `check` variable must be equal to 0.
```c
if (!check) {
	l = 0;
	while (l < 0x1f) {
		challHash[l] = answer[l];
		l = l + 1;
	}
}
```

The variable is initialized as 0, but there are three parts that could set it to 1.

there are three calls to `poly` function. And each one is chcked to be equal with some different variable.

The first one looks like this
```c
Y = (uint)r.keys[32] * 0x101;
k_00  = (uint)r.RFID[401] * 0x100 + (uint)r.RFID[400];
X1[0] = 0x3b0d;
X1[1] = 0xd056;
X1[2] = 0x8bf9;
X1[3] = 0xc111;
X1[4] = 0x8291;

if (poly(k_00, X1, Y, 5) != 0xc428) check = 1;
```

We have control over `k_00` and `Y` which is three bytes. We could either reverse the poly function (the proper way) or we could just try every combination.

## The trial and error way
The poly functions complexity is O(n). It has one inner loop which depends on variable `n` which is 5 for every function making it really trivial.
Three bytes to try, that's around 17 mega combination, estimating one run of `poly` function to cca 150 instructions leads us to 2.5 giga instructions.
On a regular machine that will run under a second.
Leading us to result

```c
r.RFID[400 + 0x10] = 242
r.RFID[401 + 0x10] = 169
r.keys[32 + 0x10] = 171
r.RFID[402] = 66
r.RFID[403] = 97
```

## Calculating the math way
ain't nobody got time for that.jpg


```python
# Challenge 13 (caeser)
k, p, a, b =  get_start()
set_byte(p, 400 + 0x10, 242)
set_byte(p, 417, 169)
set_byte(p, 418, 66)
set_byte(p, 419, 97)

a  = 171 >> 4
b = 171 & 0xf
get_hash(p, a, b)
```

## the final flag?
probably 
```
551b5cff372d310b57d39b616400461be0a1450c519a2a542f33a7af0dd565f3
```
but it's not tested yet