# Challange 9 (Board)

apart of the challange answer there are some data pushed on stack
``` c
	/* xx__o____ */
board._0_4_ = 0x5f5f7878;
board._4_4_ = 0x5f5f5f6f;
board[8] = '_';
```
we'll get to what they mean and naming later

after looking around we'll find calls to 
```
evaluate((char (*) [3])board);
findBestMove((char (*) [3])&local_78);
```

guessing from that the challange is trying to play some game.
After decoding the initial data to ascii and dividing it to 3x3 grid wi find out it's actually TIC-TAC TOE

Out input gets processed by this piece of code:
```c
eval1 = evaluate((char (*) [3])board);
if (eval1 / 10 == 0) {
  cor_y = (uint)(r.RFID[i + 0x8c] >> 4);
  cor_x = (uint)r.RFID[i + 0x8c] & 0xf;
				/* check if the value on pointer is 'empty' */
  if ((&stack0xffffffe0)[cor_x + cor_y * 3 + -0x48] == '_') {
	(&stack0xffffffe0)[cor_x + cor_y * 3 + -0x48] = 0x6f;
  }
```
the cor_y and cor_x were named after the call: 
```c
(&stack0xffffffe0)[cor_x + cor_y * 3 + -0x48] == '_'
```

which is just weirdly decompiled indexing of `board`.
if you flip the `0xffffffe0` to get stack offset and add `0x48` you'll get the offset of the
`board` variable. Why doesn't ghidra recognize this is a mistery.


After three round of the game the loop is ended and if you have won (indictaed by the output of `evaluate((char (*) [3])board)`)
the data from `answer` will get copied into the challHash.

## Playing the game

In the beggining the gameboard looks like:
```
x x _
_ o _
_ _ _
```

Judging from the years of TIC-TAC-TOE practice we see right away, that this game if played right 
can only be tied, not won by any party, but that should not be a problem as a tie is enough for us.

### Round 1
So let's play `[2:0]` so opponent can't win
```
x x o
_ o _
_ _ _
```

Now the oponent should block our obvous row of 2 `o`'s
```
x x o
_ o _
x _ _
```

### Round 2
It's obvious what we should play next
```
x x o
o o _
x _ _
```
and so is for the oponent
```
x x o
o o x
x _ _
```

# Round 3
Looking at the gameboard from last round we see  a little issue.

No matter what we choose the game will end without any winner, 
you can see that in the next figure.
```
x x o   ||  x x o
o o x   ||  o o x
x x o   ||  x o x
```

But this has one backdraw. We have two different ways to play this game, that means
we'll get two different flags.

```
a536829856d84ccd53ff8bcf534a65c5678bdbe9ce20f78407e1c987ba517e8a
```
or
```
a536829856d84ccd53ff8bcf534a65c5678bdbe9ce20f78407e1c987ba517e8a
```