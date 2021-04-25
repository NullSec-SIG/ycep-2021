# Covid Database - Part 2

## Question Text
Admin user access as well please...!?

*Creator - Benedict*

### Hints (Optional)
1. Dw the secret is only 6.

## Setup Guide
Same as part 1.

## Distribution
Same as part 1.

## Solution
1. Send post request to /api/login with username as admin. It will response with "Invalid password for user 43274923".
1. Since the secret is simple, we can brute force it (~10min). The secret is covidb.
1. Create a new jwt token with user_id 43274923 and encrypted with covidb.
1. Do a get request /api/users/43274923 with created auth token.
1. Flag can be found in the bio.
1. See solution.py for one possible method of implementing the above steps.

### Flag
`HNF{yAyYyY_aDmiN_AcceSs}`

## Recommended Reads (Optional)
NIL
