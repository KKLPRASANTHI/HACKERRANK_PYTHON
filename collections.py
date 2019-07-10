from collections import Counter
X=int(input())
lis=list(map(int,input().split()))
shoe_collection=Counter(lis)
tot_mney=0
N=int(input())
sety=[]
for i in range(N):
    size,price=[int(v) for v in input().split()]
    if shoe_collection.get(size):
        tot_mney += price
        shoe_collection[size] -= 1
print(tot_mney)
    
    
   
    
