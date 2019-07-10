#N=int(input())
#Sname=[]
#Sgrade=[]
#for i in range(N):
    #Sname.append(input())
    #Sgrade.append(map(int,input()))
#print(Sgrade)
#print(Sname)
#Sgrade.sort()
#key=Sgrade.count(min(Sgrade))
#count=0
#if key is 1:
    #del Sgrade[0]
    #count=count+1
#else:
    #while(key is not 1):
        #del Sgrade[0]
        #key=Sgrade.count(max(Sgrade))
        #count=count+1
    #if key is 1:
        #del Sgrade[0]
        #count=count+1
#key2=Sgrade.count(max(Sgrade))
#if(key2 is 1):
    #return
marksheet=[]
scoresheet=[]
for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scoresheet+=[score]
x=sorted(scoresheet)[1]
for n, s in sorted(marksheet):
    if s==x:
        print(n)
