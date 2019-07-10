def count_substring(string,sub_string):
    count=0
    for i in range(0,len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count=count+1
    return count
main=input()
sub=input()
res=count_substring(main,sub)
print(res)
