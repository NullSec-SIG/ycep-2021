# hush

## Question Text

Shakespeare is proving adamant in his security. We've broken in once but can't anymore. Luckily, we set up a backdoor. See what you can do.

*Creator - Clement Neo | @ApproxNeo

### Hints (Optional)
1. It seems one command won't cut it, how do we get multiple commands running in a single line?

## Setup Guide
1. Build and run dockerfile thnx

## Distribution
- None 

## Solution
1. Inspect element to find the backdoor (under 2nd blog post)
2. Figure out that the backdoor utilizes URL queries. `eg: (HOST:PORT?cmd=ls)`
3. Use cd and ls to find flag
4. Navigate to /var and cat flag with something along the line of `HOST:PORT?cmd=cd../../;cat+flag;`

### Flag
`HNF{hush_sw33t_prnce}`
