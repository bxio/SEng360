#!/usr/bin/python

import sys, argparse

small = "abcdefghijklmnopqrstuvwxyz"
big   = small.upper()
size  = len(big)-1
'''
#Professor's Encrypt function
def caesar_encrypt(P,K):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	C = ''
	for p in P:
		p_i = alphabet.index(p)
		c_i = (p_i+K) % len(alphabet)
		C += alphabet[c_i]
	return C

#Professor's Decrpyt function
def caesar_decrypt(C,K):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	P = ''
	for c in C:
		c_i = alphabet.index(c)
		if c_i >= K:
			p_i = c_i-K
		else:
			p_i = c_i + len(alphabet) - K
		P += alphabet[p_i]
	return P
'''
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

parser = argparse.ArgumentParser(description='Encrypt or Decrypt using Caesar Cipher')
parser.add_argument('text', help='The Plaintext or Ciphertext in question.')
parser.add_argument('-e','--encode', action="store", dest="encode", type=int, help='The amount to shift by (if encoding)', required = False)
parser.add_argument('-d','--decode', action="store", dest="decode", type=int, help='The Key when Decrypting', required = False)

args = vars(parser.parse_args())
if args['encode']:
	print "Encoding %s with shift %d:" % (args['text'],args['encode'])
	print caesar_encipher(args['text'],args['encode'])
elif args['decode']:
	print "Decoding %s with key %d:" % (args['text'],args['decode'])
	print caesar_decipher(args['text'],args['decode'])
else:
	print "Bruteforcing %s:" % args['text']
	print caesar_bruteforce(args['text'])




'''
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
'''
