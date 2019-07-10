s=input()
k=int(input())
n=len(string)
p=n//k
t=[]
def merge_the_tools(string, k):
    for i in range(0,n,p):
        t.append(string[i:i+k])
    for ele in t:
        new=''
        for i in ele:
            if i not in new:
                new+=i
        print(new)
merge_the_tools(string,k)       
    


    
