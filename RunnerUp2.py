import heapq
from collections import Counter
def runnerUp():
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr,reverse=True)
    key=arr.count(max(arr))
    if(key is 1):
        return arr[1]
    else:
        while(key is not 1):
            del arr[0]
            key=arr.count(max(arr))
        if(key is 1):
            return arr[1]
result=runnerUp()
print(result)
