def split_and_join(s):
    l=s.split()
    s='-'.join(l)
    return s
s=input()
res=split_and_join(s)
print(res)
