N=int(input())
lis=[]
for i in range(N):
    base=[]
    base.extend(input().split())
    for i in range(1,len(base)):
        base[i]=int(base[i])
    x=base[0]
    if(x=='insert'):
        lis.insert(int(base[1]),int(base[2]))
    if(x=='print'):
        print(lis)
    if(x=='remove'):
        lis.remove(base[1])
    if(x=='append'):
        lis.append(int(base[1]))
    if(x=='sort'):
        lis.sort()
    if(x=='pop'):
        lis.pop(-1)
    if(x=='reverse'):
        lis.reverse()
    
        
