N=int(input())
dic={}
for i in range(N):
    Name,math,phy,chem=input().split()
    math=float(math)
    phy=float(phy)
    chem=float(chem)
    dic[Name]=[math,phy,chem]
Stu=input()
res=sum(dic[Stu])/3.0
print("{:.2f}".format(res))

