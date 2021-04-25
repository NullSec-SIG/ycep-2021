# Challenge Name
Hide and Then What Happens?

## Question Text
Patrick looks like he's hiding something...

*Creator - Elsa*

### Hints (Optional)
1. Maybe Patrick likes messing with MetaData?

## Setup Guide
NIL

## Distribution
- rock.zip

## Solution
1. Unzip folder and figure out that it's evilpatrick.jpeg because other pics are .png
2. Download exiftool and steghide on Linux
3. View the image's metadata by using command "exiftool evilpatrick.jpeg"
4. Find "Comment: aVN0SGlzVGhFS3J1c1R5S3JhQg==" and decrypt it from Base64 to get password for next step
5. Extract the txt file from the image by using command "steghide extract -sf evilpatrick.jpeg"
6. Enter decrypted password which is iStHisThEKrusTyKraB
7. txt file will contain the flag backwards

### Flag
`HNF{n0_tHi5_iS_p4TriCk}`

## Recommended Reads (Optional)