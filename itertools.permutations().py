from itertools import permutations
s,n=input().split()
n=int(n)
A=list(permutations(sorted(s),n))
B=[]
for i in A:#to make B as a list having len(A) number of empty elements
    B.append('')
for i in range(len(A)):
    for j in range(n):
        B[i]+=A[i][j]
print('\n'.join(B))
