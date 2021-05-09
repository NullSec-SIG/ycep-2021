# Bufferman2
CHANGE THIS TO EXPECTED ... 
## Question Text
THERES ANOTHER ROOM?!!?

Creator - Nicolas Teo 

## Setup Guide 
Host bufferman2 on a port and have bufferman2 and flag.txt in the same folder. 

## Distribution 
Distribute bufferman2.c

## Solution
Simple buffer overflow exploit. 64 Characters are required to fill the buffer variable. The other characters would overflow into the changethis variable. Characters have to be written backwards because of Little Endian.
echo `python3 -c 'print("A"*64 +"\x54\x52\x53\x51")'` | ./bufferman2
## Flag 
HNF{1s_b1nAry3xp10itAt1on_f0n?!}
