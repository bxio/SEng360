#!/usr/bin/python

import sys, argparse

small = "abcdefghijklmnopqrstuvwxyz"
big   = small.upper()
size  = len(big)-1
'''
#functions with support for lowercase characters
def caesar_encrypt(S, n = 3):
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

def caesar_decrypt(S, n = 3):
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
'''

def caesar_encrypt(P,K = 3):
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	C = ''
	for p in P:
		p_i = alphabet.index(p)
		c_i = (p_i+K) % len(alphabet)
		C += alphabet[c_i]
	return C

def caesar_decrypt(C,K = 3):
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

def caesar_bruteforce(S):
	for i in range(1,26):
		if(i<10):
			s = "0%d:" % i
		else:
			s = "%d:" % i
		s+=caesar_decrypt(S,i)
		print s

'''
purpose
	return a list L where
		len(L) = 26
		L[i] contains the number of occurrences in S of the ith
		letter in the alphabet
preconditions
	S is a string of A..Z
'''
def getLetterFreqAsList(S):
	L = [0] * 26
	for letter in S:
		L[alpha.index(letter)] += 1
	return L

def displayLetterFreq(S):
	print "[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R ,S, T ,U, V ,W ,X, Y, Z]"
	print getLetterFreqAsList(S)

parser = argparse.ArgumentParser(description='Encrypt or Decrypt using Caesar Cipher')
parser.add_argument('text', help='The Plaintext or Ciphertext in question.')
parser.add_argument('-e','--encode', action="store", dest="encode", type=int, help='The amount to shift by (if encoding)', required = False)
parser.add_argument('-d','--decode', action="store", dest="decode", type=int, help='The Key when Decrypting', required = False)
parser.add_argument('-f','--freq', dest="frequency", help='Display Letter Frequencies', required = False)
args = vars(parser.parse_args())
if args['encode']:
	print "Encoding %s with shift %d:" % (args['text'],args['encode'])
	print caesar_encrypt(args['text'],args['encode'])
elif args['decode']:
	print "Decoding %s with key %d:" % (args['text'],args['decode'])
	print caesar_decrypt(args['text'],args['decode'])
elif args['frequency']:
	displayLetterFreq(args['text'])
else:
	print "Bruteforcing %s:" % args['text']
	print caesar_bruteforce(args['text'])
