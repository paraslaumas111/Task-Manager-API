def removeOuterParentheses(s):
    o=0
    c=1
    ans=''
    for i in s:
        if(i=='('):
            o+=1
            if(o!=c):
                ans+='('
        else:
            c+=1
            if(o==c):
                ans+=')'
        print(o,c,i)
    if(len(ans)%2):
        ans+=')'
    return ans
s = "(()())(())(()(()))"
print(removeOuterParentheses(s))