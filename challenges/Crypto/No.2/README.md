# No.2

## Question Text
Cole has made another challenge but he had lost the key for encryption, Find the flag!

*Creator - Colin*

### Hints (Optional)
None

## Setup Guide
None

## Distribution
output.txt

## Solution
1. The cipher is based on reuse cipher key concept, decrypt from HEX first.
2. Since we know the flag starts with HNF{, the cipher & plaintext is exposed.
3. Hence, XOR both of them will give Key.
4. XOR the key with every line in the text file until the decrypted flag appears.

### Flag
HNF{S00R_Y_iF_Y_D3C0de_onE_bi_One}

## Recommended Reads (Optional)
NIL