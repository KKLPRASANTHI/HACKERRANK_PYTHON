e=int(input())
Eset=set(map(int,input().split()))
f=int(input())
Fset=set(map(int,input().split()))
T=Eset.difference(Fset)
print(len(T))
