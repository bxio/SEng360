#!/usr/bin/env python

'''
Assignment 1
SEng 360 Fall 2013
Alastair Fehr - 
Bill Xiong - V00737042
'''

import math

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

'''
purpose
	given an integer Index or character Index a shift
	of Offset is computed
preconditions
	Index: Character [A-Z] or integer [0-25]
	Offset: positive or negative integer
'''
def shift(Index, Offset):
	L = ""
	if Index is int:
		L = alpha[(Index + Offset) % 26]
	else:
		L = alpha[((alpha.index(Index) + Offset) % 26)]
	return L

'''
purpose
	given an integer Index or character Index a right shift
	of Offset is computed
preconditions
	Index: Character [A-Z] or integer [0-25]
	Offset: positive or negative integer
'''
def rightShift(Index, Offset):
	return shift(Index, int(math.fabs(Offset)))

'''
purpose
	given an integer Index or character Index a left shift
	of Offset is computed
preconditions
	Index: Character [A-Z] or integer [0-25]
	Offset: positive or negative integer
'''
def leftShift(Index, Offset):
	return shift(Index, int((-math.fabs(Offset))))


'''
purpose
	encrypt P using Caesar cipher with key K
preconditions
	P: string of A..Z
	K in 0..25
'''
def caesar_encrypt(P,K):
	C = ""
	for p in P:
		C += rightShift(p,K)
	return C
'''
purpose
	decrypt C using Caesar cipher with key K
preconditions
	C: string of A..Z
	K in 0..25
'''
def caesar_decrypt(C,K):
	P = ""
	for c in C:
		P += leftShift(c,K)
	return P

# --------------------------------------------------------------

'''
purpose
	encrypt P using substitution cipher with key K
preconditions
	P: string of A..Z
	K: permutation of A..Z
'''
def substitution_encrypt(P,K):
	C = ""
	for p in P:
		C += K[alpha.index(p)]
	return C
'''
purpose
	decrypt C using substitution cipher with key K
preconditions
	C: string of A..Z
	K: permutation of A..Z
'''
def substitution_decrypt(C,K):
	P = ""
	for c in C:
		P += alpha[K.index(c)]
	return P
# --------------------------------------------------------------

'''
purpose
	encrypt P using Vernam cipher with key K
	if len(P) > len(K) then repeat the key as needed
preconditions
	P: string of A..Z
	K: non-empty list of int in 0..25
'''
def vernam_encrypt(P,K):
	C = ""
	for i in range(0,len(P)):
		C += rightShift(P[i], K[i % len(K)])
	return C

'''
purpose
	decrypt C using Vernam cipher with key K
	if len(C) > len(K) then repeat the key as needed
preconditions
	C: string of A..Z
	K: non-empty list of int in 0..25
'''
def vernam_decrypt(C,K):
	P = ""
	for i in range(0, len(C)):
		P += leftShift(C[i], K[i % len(K)])
	return P
# --------------------------------------------------------------

'''
purpose
	encrypt P using book cipher with key K
	if len(P) > len(K) then repeat the key as needed
	converts Book Key into Vernam Key and calls vernam_encrypt
preconditions
	P: string of A..Z
	K: non-empty string of A..Z
'''
def book_encrypt(P,K):
	KEY = [0]*len(K)
	for i in range(0,len(K)):
		KEY[i] = alpha.index(K[i])
	return vernam_encrypt(P,KEY)
'''
purpose
	decrypt C using book cipher with key K
	if len(C) > len(K) then repeat the key as needed
	converts Book Key into Vernam Key and calls vernam_decrypt 
preconditions
	C: string of A..Z
	K: non-empty string of A..Z
'''
def book_decrypt(C,K):
	KEY = [0]*len(K)
	for i in range(0, len(K)):
		KEY[i] = alpha.index(K[i])
	return vernam_decrypt(C, KEY)
# --------------------------------------------------------------

'''
purpose
	encrypt P using columnar transposition cipher with key K
preconditions
	P: string of A..Z
	K > 1
'''
def columnar_encrypt(P,K):
	C = ""
	buckets  = [[] for _ in range(K)] # how to create list of lists quickly http://stackoverflow.com/a/8713681
	bucket = 0;

	for p in P:
		buckets[bucket].append(p)
		bucket = (bucket+1) % K

	for buck in buckets:
		for c in buck:
			C += c
	return C

'''
purpose
	decrypt C using columnar transposition cipher with key K
preconditions
	P: string of A..Z
	K > 1
'''
def columnar_decrypt(C,K):
	P = ""
	extra = len(C) % K

	if extra == 0:
		colHeight = len(C)/K
	else:
		colHeight = (len(C)/K)+1
		
	cols  = [[] for _ in range(K)]
	col = 0

	for i in range(len(C)):
	#	print col
		cols[col].append(C[i])
		colHeight -= 1;
		if colHeight == 0:
			extra -= 1
			if extra > 0:
				colHeight = (len(C)/K)+1	
			else: 
				colHeight = len(C)/K
			col = (col + 1) % K

	#print cols
	for y in range(len(cols[0])):
		for x in range(K):
			if(y < len(cols[x])):
				P += cols[x][y]

	return P






# --------------------------------------------------------------

'''
purpose
	encrypt P using RSA encryption with key K e,n
preconditions
	P: list of positive integers
	e,n selected according to the RSA requirements
'''
def rsa_encrypt(P,e,n):
	 C = []
	 for p in P:
	 	C.append((p**e) % n)
	 return C
'''
purpose
	decrypt C using RSA encryption with key K d,n
preconditions
	C: list of positive integers
	d,n selected according to the RSA requirements
'''
def rsa_decrypt(C,d,N):
	P = []
	for c in C:
		P.append((c**d) % N)
	return P
# --------------------------------------------------------------

'''
purpose
	return a list L where
		len(L) = 26
		L[i] contains the number of occurrences in S of the ith
			letter in the alphabet
preconditions
	S is a string of A..Z
'''
def count_letters(S):
	L = [0] * 26
	for letter in S:
		L[alpha.index(letter)] += 1
	return L

# --------------------------------------------------------------

'''
purpose
	return a dictionary D where
		D.keys() contains all of the digrams in S
		D[d] is the number of occurrences of digram d in S
preconditions
	S is a string of A..Z
'''
def count_digrams(S):
	D = {}
	for i in range(len(S)-1):
		di = S[i] + S[i+1]
		if di in D:
			D[di] = D[di]+1
		else:
			D[di] = 1
	return D

def bruteForce(C):
	print "BRUTE FORCE CAESAR: \n"
	for i in range(0,26):
		print caesar_decrypt(C,i)
	print "\nFINSIHED CAESAR: \n"

	print "BRUTE FORCE Columnar: \n"
	for i in range(1,26):
		print columnar_decrypt(C,i)
	print "\nFINSIHED Columnar: \n"
