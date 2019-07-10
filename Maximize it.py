N,M=input().split()
N=int(N)
M=int(M)
s=[]
for i in range(N):
    s.append(input().split())
for i in range(len(s)):
    del s[i][0]
for l in s:
    for i in range(len(l)):
        l[i]=int(l[i])
maxl=[]
for l in s:
    maxl.append(max(l))
maxl=[i*i for i in maxl]
print(sum(maxl)%M)
    
    
