# No.3

## Question Text
Dick was attempting to intercept an encrypted communication between Lin and Winson. Fortunately he managed to recover Winson's encryption file. When he ran the file he recieved this.
37f17aef7304e649ab8d00fa6e3bee5870525b86b031f7a51997a40cd8070b00886ccc5f5d05535cf00a18f22448083cd90387f0d2ce37571280c3e44f4eb20fef7f677b9642b371
28da1cfc4041d61a8ff32ede68108f7f4b526bb9e1

*Creator - Colin*

### Hints (Optional)
None

## Setup Guide
None

## Distribution
No.3.py

## Solution
1. The cipher is based on reuse cipher key concept. Decrypt from HEX first.
2. Since there is a test run, a sample cipher & plaintext is exposed.
3. Hence, XOR both of them will give Key.
4. XOR the key with flag's ciphertext will return the decrypted flag.

### Flag
HNF{R3UsE^kEu_AdTaCK}

## Recommended Reads (Optional)
NIL