# Challenge Name
Strongest Bricks
## Question Text

I need to find the biggest number I can get when I go down this wall. 
However, I can only go directly down, diagonally down left or diagonally down right.

Example:
2,3,4,5,6
1,5,8,9,0
6,4,3,6,7
5,4,7,3,5

In this case, if I start from 2 on the first line, I can only go to 1 or 5 of the second line. If I start from 4 on the first line, I can go to 5,8 or 9. 

If I start from 2 on the first line and go to 5, 3 and 7, my total would be 2+5+3+7, and the final number will be 17.

*Creator - Timothy*

### Hints (Optional)
1. I should try to find the highest number from the 3 option I can go down from
2. I mean, brute forcing could also be an option

## Setup Guide
1. NIL

## Distribution
- thegreatnumberwall.csv
    

## Solution
1. Solution found in strongbrick.py
2. Store all the countable letters in a list
3. Find the most common word in the list

### Flag
`HNF{3272865}`

## Recommended Reads (Optional)
* NIL
