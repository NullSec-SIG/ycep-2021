# No.1

## Question Text
Cole is participating as a challenger creator, for 'Hack n Flag' CTF. Dick his boss, is going attempting his challenge. Can you help him decrypt it?
Encrypted Text - 2f272112305a02052b362307080c1a

*Creator - Colin*

### Hints (Optional)
None

## Setup Guide
None

## Distribution
None

## Solution
1. Although Key is unknown, we do know that the first 4 Bytes is 'HNF{'. Decrypt from HEX First.
2. XOR that with the first 4 bytes of the encrypted hex will return the key.
3. Use the key to decrypt the entire ciphertext.

### Flag
HNF{W3elL_Dnoe}

## Recommended Reads (Optional)
NIL