from itertools import product
A=list(map(int,input().split()))
B=[int(x) for x in input().strip().split()]
l=list(product(A,B))
print(*l)
