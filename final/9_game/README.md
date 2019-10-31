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

the gameboard looks like:
```
x x _
_ o _
_ _ _
```
so the game already started and it's our move.
Placing `o` at coords `[2:0] ` will stop our opponent.
```
x x o
_ o _
_ _ _
```
If the opponent is programmed correctly (and we hope he is) he will play `[0:2]` 

There are no outputs to Serial, so we'll just hope he'll play:
```
x x o
_ o _
x _ _
```
Stopping us.

Our next play will be `[2:1]` making us win in the next round
```
x x o
_ o o
x _ _
```

But heres the problem, we do not know if the bot will play `[0:1]` or `[2:2]` and we can't learn that in any way.
So we'll try `[0:1]` first, if that doesn't succeed, we'll try `[2:2]`
If the bot is deterministic we'll win on either one of the tries.

Eventually we could try to rewrite the bots logic and run it locally, but this is faster.

```
set_byte(n, 0x9c, 0x02)
set_byte(n, 0x9d, 0x12)
set_byte(n, 0x9e, 0x10)  # set_byte(n, 0x9e, 0x22)
```

