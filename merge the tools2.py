import textwrap
s=input()
t=int(input())
p=len(s)//t
h=[]
for i in range(0,len(s),p):
        h.append(s[i:i+p])
for i in h:
        new=''
        for e in i:
                if e not in new:
                        new+=e
                else:
                        pass
        print(new)
        

