S=input()
count1=0
count2=0
count3=0
count4=0
count5=0
for i in S:
    if i.isalnum():
        count1=count1+1
if count1==0:
    print("False")
else:
    print("True")
for i in S:
    if i.isalpha():
        count2=count2+1
if count2==0:
    print("False")
else:
    print("True")        
for i in S:
    if i.isdigit():
        count3=count3+1
if count3==0:
    print("False")
else:
    print("True")
for i in S:
    if i.islower():
        count4=count4+1
if count4==0:
    print("False")
else:
    print("True")
for i in S:
    if i.isupper():
        count5=count5+1
if count5==0:
    print("False")
else:
    print("True")
