s=input()
n=len(s)
vowels='AEIOUaeiou'
def minion_game(s):
    kevin=0
    stuart=0
    for i in range(n):
        if s[i] in vowels:
            kevin+=n-i
        else:
            stuart+=n-i
    if kevin>stuart:
        print('kevin'+' ',kevin)
    elif stuart>kevin:
        print('stuart',stuart)
    else:
        print('Draw')
minion_game(s)       
