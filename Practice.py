def minDays(nums, m, k):
    if(m*k>len(nums)):
        return -1
    for i in range(0,len(nums)):
        ele=2**63 - 1
        for p in nums:
            if(type(p)==int):
                if(p<ele):
                    ele=p
        print(ele)
        for j in range(0,len(nums)):
            if(nums[j]==ele):
                nums[j]='$'
        e=0
        t=0
        bq=0
        while(e<len(nums)):
            if(nums[e]=='$'):
                t+=1
                if(t==k):
                    t=0
                    bq+=1
                    ans=ele
                e+=1
            else:
                t=0
                e+=1
        print(nums)
        if(bq>=m):
            return ans
                
nums=[1,10,2,9,3,8,4,7,5,6]
print(minDays(nums, 4, 2))