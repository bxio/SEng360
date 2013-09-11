'''
purpose
	encrypt P using substitution cipher with key K
preconditions
	P: possibly empty string of A..Z
	K: permutation of A..Z
'''
def substitution_encrypt(P,K):
	pass # put your implementation here and REMOVE THIS LINE

'''
purpose
	decrypt C using substitution cipher with key K
preconditions
	C: possibly empty string of A..Z
	K: permutation of A..Z
'''
def substitution_decrypt(C,K):
	pass # put your implementation here and REMOVE THIS LINE


# test
#    ABCDEFGHIJKLMNOPQRSTUVWXYZ
K = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
C = substitution_encrypt('CAT',K)
if not C == 'DBU':
	print 'test_0 failed'
P = substitution_decrypt('DBU',K)
if not P == 'CAT':
	print 'test_1 failed'
