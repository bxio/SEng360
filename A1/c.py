#!/usr/bin/python

import sys, optparse






small = "abcdefghijklmnopqrstuvwxyz"
big   = small.upper()
size  = len(big)-1

def caesar_encipher(S, n = 3):
	finale_str = ''
	for c in S:
		if c.islower():
			if (small.find(c)+n)>size:
				c = small[(small.find(c)+n)-(size+1)]
			else:
				c = small[small.find(c)+n]
		elif c.isupper():
			if (big.find(c)+n)>size:
				c = big[(big.find(c)+n)-(size+1)]
			else:
				c = big[big.find(c)+n]
		finale_str += c
	return finale_str

def caesar_decipher(S, n = 3):
	finale_str = ''
	for c in S:
		if c.islower():
			if (small.find(c)-n)<0:
				c = small[size-small.find(c)-(n-1)]
			else:
				c = small[small.find(c)-n]
		elif c.isupper():
			if (big.find(c)-n)<0:
				c = big[size-big.find(c)-(n-1)]
			else:
				c = big[big.find(c)-n]
		finale_str += c
	return finale_str

def caesar_bruteforce(S):
	for i in range(0,26):
		print caesar_decipher(S,i)


# Encipher examples...
print caesar_encipher("abcdefghijklmnopqrstuvwxyz", 1)
print caesar_encipher("abcdefghijklmnopqrstuvwxyz", 2)
print caesar_encipher("abcdefghijklmnopqrstuvwxyz")

print caesar_encipher("v0id is me!", 1)
print caesar_encipher("v0id is me!", 2)
print caesar_encipher("v0id is me!")

print "\n"

# Decipher examples...
print caesar_decipher("x0kf ku og!", 1)
print caesar_decipher("x0kf ku og!", 2)
print caesar_decipher("x0kf ku og!")

print "\n"

# Both...
string = "x0kf ku og!"
print caesar_bruteforce(string)

