N=int(input())
a=[]
a=list(map(int,input().split()))
b=tuple(a)
print(hash(b))
