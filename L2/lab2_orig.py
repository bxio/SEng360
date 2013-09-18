'''
purpose
	encrypt P using Vernam cipher with key K
preconditions
	P string of A..Z
	K: non-empty list of int in 0..25
	len(P) <= len(K)
'''
def vernam_encrypt(P,K):
	pass # put your implementation here and REMOVE THIS LINE

'''
purpose
	decrypt C using Vernam cipher with key K
preconditions
	C string of A..Z
	K: non-empty list of int in 0..25
	len(C) <= len(K)
'''
def vernam_decrypt(C,N):
	pass # put your implementation here and REMOVE THIS LINE

# -----------------------------------------------------------------------

'''
purpose
	encrypt P using book cipher with key K
preconditions
	P string of A..Z
	K: non-empty string of A..Z
	len(P) <= len(K)
'''
def book_encrypt(P,K):
	pass # put your implementation here and REMOVE THIS LINE

'''
purpose
	decrypt C using book cipher with key K
preconditions
	C string of A..Z
	K: non-empty string of A..Z
	len(C) <= len(K)
'''
def book_decrypt(C,N):
	pass # put your implementation here and REMOVE THIS LINE

# -----------------------------------------------------------------------

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
	pass # put your implementation here and REMOVE THIS LINE
