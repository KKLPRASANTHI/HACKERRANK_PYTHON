n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
listnew=[]
for i in arr:
    if i not in listnew:
        listnew.append(i)
        #listnew.sort(reverse=True)
print(listnew[1])
