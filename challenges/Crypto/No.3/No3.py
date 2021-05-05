from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

key = os.urandom(16)

def encrypt(plaintext):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128))
    ciphertext = (cipher.encrypt(plaintext)).hex()
    return ciphertext

test = b"We have a East Coast, Singapore, we have a together, an East Coast plan."
print(encrypt(test),"\n")

with open('flag.txt', 'rb') as f:
    text = f.read().strip()
print(encrypt(text))
