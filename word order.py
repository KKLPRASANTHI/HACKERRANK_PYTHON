n=int(input())
l=[]
count1=[]
def wordOrder():
    for i in range(n):
        l.append(input())
    t=set(l)
    setc=0
    for w in t:
        setc+=1
    print(setc)
    for ele in l:
        count=1
        for i in range(len(l)):
            if ele==l[i] and l.index(ele) is not i:
                count=count+1
                if l.index(ele) is not i:
                    l.remove(l[i])
        count1.append(count)
    #print(len(l))
    for i in count1:
        print(i,end=' ')
wordOrder()
    
#for counting no of distinct words
u=[]
for ele in l:
    if ele not in u:
        u.append(ele)

