# Challenge Name

## Question Text

We found this log file and want to trace it back to its organization, but to do that we'll need to know their public key. Can you retrieve it from this bit of information?

Flag format is HNF{x}, where x is the respective value of the public key in Base16. The y value is not needed.


*Creator - Clement Neo | @ApproxNeo

### Hints (Optional)
1. It seems they use elliptic curves, I hear Sage has a builtin library for handling that.

## Setup Guide
1. Distribute handout.txt

## Distribution
- handout.txt

## Solution
1. Substitute Generator values into the equation to find out that b = 7, hence the eqn is y^2 = x^3 + 7
2. Utilize Sage to conduct ECC Multiplication of (G * PrivKey), the result is the Public Key
3. Sample sage code:

    `F = FiniteField(0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f)`  
    `E = EllipticCurve(F,[0, 7])`  
    `G = E.point((0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,   0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8))`  
    `d = 54579156511173636181080397525378494796415869850149828786275540366892832517944`  
    `G*d`

### Flag
`HNF{f412445c3cfe7eb3ad217b91f0bef42c27bdf9099ee191aad6512da8cbab59b3}`

