M=int(input())
Mlis=set(map(int,input().split()))
N=int(input())
Nlis=set(map(int,input().split()))
symd=set()
symd=sorted(Mlis.union(Nlis)-Mlis.intersection(Nlis))
for ele in symd:
    print(ele)
