Python 3.6.7 (v3.6.7:6ec5cf24b7, Oct 20 2018, 13:35:33) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='HACK'
>>> sorted(s)
['A', 'C', 'H', 'K']
>>> list(permutations(s,2))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list(permutations(s,2))
NameError: name 'permutations' is not defined
>>> from itertools import permutations
>>> list(permutations(s,2))
[('H', 'A'), ('H', 'C'), ('H', 'K'), ('A', 'H'), ('A', 'C'), ('A', 'K'), ('C', 'H'), ('C', 'A'), ('C', 'K'), ('K', 'H'), ('K', 'A'), ('K', 'C')]
>>> list(permutations(sorted(s),2))
[('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'A'), ('C', 'H'), ('C', 'K'), ('H', 'A'), ('H', 'C'), ('H', 'K'), ('K', 'A'), ('K', 'C'), ('K', 'H')]
>>> *list(permutations(sorted(s),2))
SyntaxError: can't use starred expression here
>>> print(*list(permutations(sorted(s),2)))
('A', 'C') ('A', 'H') ('A', 'K') ('C', 'A') ('C', 'H') ('C', 'K') ('H', 'A') ('H', 'C') ('H', 'K') ('K', 'A') ('K', 'C') ('K', 'H')
>>> print('\n'.join(*list(permutations(sorted(s),2))))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('\n'.join(*list(permutations(sorted(s),2))))
TypeError: join() takes exactly one argument (12 given)
>>> print('\n'.join(list(permutations(sorted(s),2))))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print('\n'.join(list(permutations(sorted(s),2))))
TypeError: sequence item 0: expected str instance, tuple found
>>> list(permutations(sorted(s),2))
[('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'A'), ('C', 'H'), ('C', 'K'), ('H', 'A'), ('H', 'C'), ('H', 'K'), ('K', 'A'), ('K', 'C'), ('K', 'H')]
>>> A=list(permutations(sorted(s),2))
>>> A
[('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'A'), ('C', 'H'), ('C', 'K'), ('H', 'A'), ('H', 'C'), ('H', 'K'), ('K', 'A'), ('K', 'C'), ('K', 'H')]
>>> A[1]
('A', 'H')
>>> A[1][0]+A[1][1]
'AH'
>>> for ele in A:
	for a,b in ele:
		ele=a+b

		
Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    for a,b in ele:
ValueError: not enough values to unpack (expected 2, got 1)
>>> A
[('A', 'C'), ('A', 'H'), ('A', 'K'), ('C', 'A'), ('C', 'H'), ('C', 'K'), ('H', 'A'), ('H', 'C'), ('H', 'K'), ('K', 'A'), ('K', 'C'), ('K', 'H')]
>>> for ele in A:
	for (a,b) in ele:
		ele=str(a+b)

		
Traceback (most recent call last):
  File "<pyshell#23>", line 2, in <module>
    for (a,b) in ele:
ValueError: not enough values to unpack (expected 2, got 1)
>>> for ele in A:
	for a,b in ele:
		print(a,b)

		
Traceback (most recent call last):
  File "<pyshell#27>", line 2, in <module>
    for a,b in ele:
ValueError: not enough values to unpack (expected 2, got 1)
>>> for i in range(len(A)):
	for j in range(2):
		A[i]+=A[i][j]

		
Traceback (most recent call last):
  File "<pyshell#31>", line 3, in <module>
    A[i]+=A[i][j]
TypeError: can only concatenate tuple (not "str") to tuple
>>> B=[]
>>> for i in range(len(A)):
	for j in range(n):
		B[i]+=A[i][j]

		
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    for j in range(n):
NameError: name 'n' is not defined
>>> n=2
>>> for i in range(len(A)):
	for j in range(n):
		B[i]+=A[i][j]

		
Traceback (most recent call last):
  File "<pyshell#43>", line 3, in <module>
    B[i]+=A[i][j]
IndexError: list index out of range
>>> B=[]
>>> for i in range(len(A)):
	B.append('')

	
>>> B
['', '', '', '', '', '', '', '', '', '', '', '']
>>> len(B)
12
>>> len(A)
12
>>> for i in range(len(A)):
	for j in range(n):
		B[i]+=A[i][j]

		
>>> B
['AC', 'AH', 'AK', 'CA', 'CH', 'CK', 'HA', 'HC', 'HK', 'KA', 'KC', 'KH']
>>> '\n'.join(B)
'AC\nAH\nAK\nCA\nCH\nCK\nHA\nHC\nHK\nKA\nKC\nKH'
>>> print('\n'.join(B))
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
>>> 
 RESTART: C:/Users/K.K.L.PRASANTHI/Desktop/prathi/python/Hacker rank/itertools.permutations().py 
HACK 2
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
>>> 
