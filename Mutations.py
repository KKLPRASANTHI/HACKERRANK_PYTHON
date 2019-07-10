def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]
#or
def mutate_string2(string, position, character):
    l=list(string)
    l[position]=character
    string=''.join(l)
    return string
S=input()
P,C=input().split()
res1=mutate_string(S,int(P),C)
res2=mutate_string2(S,int(P),C)
print(res1)
print(res2)
