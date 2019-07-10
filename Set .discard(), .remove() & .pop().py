n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(N):
    x=input().split()
    y=x[0]
    if y=='pop':
        s.pop()
    if y=='remove':
        s.remove(int(x[1]))
    if y=='discard':
        s.discard(int(x[1]))
print(sum(s))
