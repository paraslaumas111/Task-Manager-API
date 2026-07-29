def smallestPalindrome(s):
    ans=[]
    # half=0
    # even=0
    # if(len(s)%2==0):
    #     half=len(s)//2-1
    #     even=1
    # else:
    #     half=len(s)//2
    for i in range(0,len(s)//2):
        ans+=s[i]
    ans.sort()
    if(len(s)%2==1):
        ans+=s[len(s)//2]
    print(ans)
    f_ans=''
    for i in ans:
        f_ans+=i
    print(f_ans)
    if(len(s)%2==0):
        for i in range(-1,-1*len(ans)-1,-1):
            f_ans+=ans[i]
    else:
        for i in range(-2,-1*len(ans)-1,-1):
            f_ans+=ans[i]
    return f_ans

print(smallestPalindrome("daccad"))