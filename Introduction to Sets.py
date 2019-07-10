def average(array):
    l=set(array)
    return sum(l)/len(l)
n=int(input())
arr=list(map(int,input().split()))
res=average(arr)
print(res)
