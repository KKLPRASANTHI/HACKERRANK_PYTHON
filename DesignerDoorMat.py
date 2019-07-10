#print('.|.'.center(21,'-'))
N,M=input().split()
N=int(N)
M=int(M)
g=(N-1)//2
s='.|.'
for k in range(1,N-1,2):#for 9 it has .|. 7 times and for 7 it has .|. 5 times so for n it has .|. n-2 times....so n-2+1=n-1
    print((s*k).center(M,'-'))
print('WELCOME'.center(M,'-'))
for k in range(N-2,0,-2):
    print((s*k).center(M,'-'))
    
