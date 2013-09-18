alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
'''
purpose
	encrypt P using Vernam cipher with key K
preconditions
	P string of A..Z
	K: non-empty list of int in 0..25
	len(P) <= len(K)
'''
def vernam_encrypt(P,K):
	ret = ''
	for letter in P:
		pos = alpha.index(letter)
		offset = K[P.index(letter)]
		final = (pos + offset) % 26
		ret += alpha[final]
	return ret
'''
purpose
	decrypt C using Vernam cipher with key K
preconditions
	C string of A..Z
	K: non-empty list of int in 0..25
	len(C) <= len(K)
'''
def vernam_decrypt(C,N):
	pass
	# ret = ""
	# for letter in C:
	# 	pos = alpha.index(letter)
	# 	offset = N[C.index(letter)]
	# 	final = (pos - offset) % 26
	# 	ret += alpha[final]
	# return ret
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
	ret = ""
	for letter in P:
		pos1 = alpha.index(letter)
		pos2 = alpha.index(K[P.index(letter)])
		final = (pos1 + pos2) % 26
		ret += alpha[final]
	return ret

'''
purpose
	decrypt C using book cipher with key K
preconditions
	C string of A..Z
	K: non-empty string of A..Z
	len(C) <= len(K)
'''
def book_decrypt(C,N):
	pass
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
	L = [0] * 26
	for letter in S:
		L[alpha.index(letter)] += 1
	return L

#tests follow
a = 'ABCDEFGHIJAKLMNOPQRSTUVWXYZ'
print count_letters(a)
