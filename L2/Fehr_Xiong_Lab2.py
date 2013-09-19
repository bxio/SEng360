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
	ret = ""
	for i in range (0, len(P)):
		pos = alpha.index(P[i])
		final = (pos + K[i]) % 26
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
	ret = ""
	for i in range (0, len(C)):
		pos = alpha.index(C[i])
		final = (pos - N[i]) % 26
		ret += alpha[final]
	return ret
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
	for i in range (0, len(P)):
		pos1 = alpha.index(P[i])
		pos2 = alpha.index(K[i])
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
	ret = ""
	for i in range(0, len(C)):
		pos1 = alpha.index(C[i])
		pos2 = alpha.index(N[i])
		final = (pos1 - pos2) % 26
		ret += alpha[final]
	return ret
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

a = "gurynlbhgjnfsbenybatgvzrabgfhpprffshyylcebiravananvepensg"
b = "NYJNLFTBGBBGURECRBCYRFSHARENYFBGUREJVFRGURLJBAGTBGBLBHEF"
print count_letters(b.upper())
print "[a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]"
