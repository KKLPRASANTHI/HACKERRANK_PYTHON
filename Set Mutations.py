a=int(input())
A=set(map(int,input().split()))
n=int(input())
for i in range(n):
    x=input().split()
    y=set(map(int,input().split()))
    key=x[0]
    if key=='intersection_update':
        A.intersection_update(y)
    if key=='update':
        A.update(y)
    if key=='difference_update':
         A.difference_update(y)
    if key=='symmetric_difference_update':
        A.symmetric_difference_update(y)
print(sum(map(int,A)))
