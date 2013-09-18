'''
purpose
	encrypt P using substitution cipher with key K
preconditions
	P: possibly empty string of A..Z
	K: permutation of A..Z
'''
O = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def substitution_encrypt(P,K):
	ret = ''
	for letter in P:
		pos = O.index(letter)
		ret += K[pos]
	return ret
'''
purpose
	decrypt C using substitution cipher with key K
preconditions
	C: possibly empty string of A..Z
	K: permutation of A..Z
'''
def substitution_decrypt(C,K):
	ret = ''
	for letter in C:
		pos = K.index(letter)
		ret += O[pos]
	return ret

# test
#    ABCDEFGHIJKLMNOPQRSTUVWXYZ
K = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
C = substitution_encrypt('CAT',K)
if not C == 'DBU':
	print 'test_0 failed'
P = substitution_decrypt('DBU',K)
if not P == 'CAT':
	print 'test_1 failed'
