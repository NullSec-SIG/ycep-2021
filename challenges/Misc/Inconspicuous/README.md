# Challenge Name

## Question Text

We've managed to crack the key to their secure tunnel but it seems they've only been sending each other images. Can you find their underlying messages?

*Creator - Clement Neo | @ApproxNeo

### Hints (Optional)
1. Most files have a structure; they have specific hex values for each chunk of the file.

## Setup Guide
1. Distribute hamster.png 

## Distribution
- hamster.png

## Solution
1. Use a hex editor to look in depth
2. Research and find out that .png files end with IEND
3. Realize that there is extra data after IEND, and that it starts with "7z".
4. Open cmd prompt and run `7z x hamster.png`
5. Grep the unzipped file for `'HNF{'`

### Flag
`HNF{r1t3_undR_ur_n0s3}`