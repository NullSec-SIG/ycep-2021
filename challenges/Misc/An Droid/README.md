# An Droid

## Question Text

Droid be like beep boop beep...

*Creator - Benedict*

### Hints (Optional)
1. dex it to a jar.

## Setup Guide
NIL

## Distribution
- app-debug.apk

## Solution
1. Unzip the .apk file, you will see classes.dex
2. De-compile the .dex with https://github.com/pxb1988/dex2jar to get a .jar file
3. Unzip the .jar to get the underlying class.
4. Open with a java de-compiler e.g. IntelliJ to view the source code.
5. In d.a.a.a.a, there is a if condition `var1.equals("hacker") && var2.equals("bypassthis!")`
6. Install and open the apk on a android phone / simulator. Key in `hacker` as username and `bypassthis!` as password.
7. Click on sign in and a new activity will open with the flag.

### Flag
`HNF{Hack3d_tHe_dr0id}`

## Recommended Reads (Optional)
NIL