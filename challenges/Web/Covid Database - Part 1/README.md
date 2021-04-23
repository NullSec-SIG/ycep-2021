# Covid Database - Part 1

## Question Text
I want to access some covid data... but lost my password. Got a token tho, hopefully that helps.

*Creator - Benedict*

### Hints (Optional)
1. RESTful api is fun, so much json stuff!

## Setup Guide
This is a python flask application.
A docker file has been provided which can be used as a base to deploy the web application.

## Distribution
- token.txt

## Solution
1. Based on the formatting and hint of "beaver token" in api docs, discover that its a JWT token.
1. When trying to use this token, the request will be rejected as the token expired.
1. View the payload in the token with a website like https://jwt.io/.
1. Modify the token such that the `alg` is `none` and the `exp` is a timestamp greater than the time of access.
1. Get the countries data with a get request on `/api/data/countries`.
1. Discover that there is a country named `HackNFlag`.
1. Get the `HackNFlag` country details of with 1. request on `/api/data/countries/HackNFlag`.
1. The flag `c0vId_DaTaBa$e_BrEach3d` is found at path `countryInfo.flag`.

### Flag
`HNF{c0vId_DaTaBa$e_BrEach3d}`

## Recommended Reads (Optional)
* https://medium.com/@Asm0d3us/ritsec-ctf-web-challenges-writeup-e46e4965495f
* https://medium.com/swlh/hacking-json-web-tokens-jwts-9122efe91e4a
