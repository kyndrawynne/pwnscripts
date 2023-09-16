###
### Welcome to /challenge/babymem_level6.0!
###

The challenge() function has just been launched!
Before we do anything, let's take a look at challenge()'s stack frame:
+---------------------------------+-------------------------+--------------------+
|                  Stack location |            Data (bytes) |      Data (LE int) |
+---------------------------------+-------------------------+--------------------+
| 0x00007fffd1d96da0 (rsp+0x0000) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96da8 (rsp+0x0008) | 78 7f d9 d1 ff 7f 00 00 | 0x00007fffd1d97f78 |
| 0x00007fffd1d96db0 (rsp+0x0010) | 68 7f d9 d1 ff 7f 00 00 | 0x00007fffd1d97f68 |
| 0x00007fffd1d96db8 (rsp+0x0018) | 23 b7 4a a1 01 00 00 00 | 0x00000001a14ab723 |
| 0x00007fffd1d96dc0 (rsp+0x0020) | a0 74 4a a1 31 7f 00 00 | 0x00007f31a14a74a0 |
| 0x00007fffd1d96dc8 (rsp+0x0028) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96dd0 (rsp+0x0030) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96dd8 (rsp+0x0038) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96de0 (rsp+0x0040) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96de8 (rsp+0x0048) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96df0 (rsp+0x0050) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96df8 (rsp+0x0058) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96e00 (rsp+0x0060) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96e08 (rsp+0x0068) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96e10 (rsp+0x0070) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96e18 (rsp+0x0078) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96e20 (rsp+0x0080) | 00 00 00 00 00 00 00 00 | 0x0000000000000000 |
| 0x00007fffd1d96e28 (rsp+0x0088) | 00 00 00 00 ff 7f 00 00 | 0x00007fff00000000 |
| 0x00007fffd1d96e30 (rsp+0x0090) | d0 11 40 00 00 00 00 00 | 0x00000000004011d0 |
| 0x00007fffd1d96e38 (rsp+0x0098) | d0 6d d9 d1 ff 7f 00 00 | 0x00007fffd1d96dd0 |
| 0x00007fffd1d96e40 (rsp+0x00a0) | 70 7e d9 d1 ff 7f 00 00 | 0x00007fffd1d97e70 |
| 0x00007fffd1d96e48 (rsp+0x00a8) | 4e 2b 40 00 00 00 00 00 | 0x0000000000402b4e |
+---------------------------------+-------------------------+--------------------+
Our stack pointer points to 0x7fffd1d96da0, and our base pointer points to 0x7fffd1d96e40.
This means that we have (decimal) 22 8-byte words in our stack frame,
including the saved base pointer and the saved return address, for a
total of 176 bytes.
The input buffer begins at 0x7fffd1d96dd0, partway through the stack frame,
("above" it in the stack are other local variables used by the function).
Your input will be read into this buffer.
The buffer is 92 bytes long, but the program will let you provide an arbitrarily
large input length, and thus overflow the buffer.

In this level, there is no "win" variable.
You will need to force the program to execute the win_authed() function
by directly overflowing into the stored return address back to main,
which is stored at 0x7fffd1d96e48, 120 bytes after the start of your input buffer.
That means that you will need to input at least 128 bytes (92 to fill the buffer,
28 to fill other stuff stored between the buffer and the return address,
and 8 that will overwrite the return address).

We have disabled the following standard memory corruption mitigations for this challenge:
- the canary is disabled, otherwise you would corrupt it before
overwriting the return address, and the program would abort.
- the binary is *not* position independent. This means that it will be
located at the same spot every time it is run, which means that by
analyzing the binary (using objdump or reading this output), you can
know the exact value that you need to overwrite the return address with.

Payload size: 