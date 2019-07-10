s,w=input(),int(input())
t=[]
def TextWrap(s,k):
    for i in range(0,len(s),w):
        t.append(s[i:i+w])
    return '\n'.join(t)
res=TextWrap(s,w)
print(res)
