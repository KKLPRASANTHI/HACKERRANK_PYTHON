#import array
n,m=map(int,input().split())
#n=int(n)
#m=int(m)
num=list(map(int,input().split()))
#arr=array.array('i',num)
#for ele in range(len(num)):
   # print(arr[ele],end=" ")
#print('\n')
A=set(map(int,input().split()))
B=set(map(int,input().split()))
count=0
for ele in num:
    if ele in A:
        count=count+1
    if ele in B:
        count=count-1
print(count)
    

