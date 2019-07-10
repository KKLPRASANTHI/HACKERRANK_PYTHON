N=int(input())
Sgrade=[]
Sng=[]
Stot=[]
for i in range(N):
    name=input()
    grade=float(input())
    Sgrade.append(grade)
    Sng.append([name,grade])
for ele in Sgrade:
    if ele not in Stot:
        Stot.append(ele)
Stot.sort()
key=Stot[1]
Sng=sorted(Sng)
#above line sorts by first element in each list
#to sort by second element use the below code snippet
#sorted(sub_li, key = lambda x: x[1])
for n,g in Sng:
    #Difference between == and is operator in Python
#The == operator compares the values of both the operands and checks for value equality. Whereas is operator checks whether both the operands refer to the same object or not.
    if g==key:
        print(n)
