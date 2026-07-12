def BS(nums,l,r,t):
    while(l<=r):
        mid=(l+r)//2
        if(nums[mid]==t):
            return True
        elif(nums[mid]>t):
            r=mid-1
        else:
            l=mid+1
    return False

def search(nums, target):
    if(len(nums)==1):
        if(nums[0]==target):
            return True
        else:
            return False
    oldl=0
    oldr=len(nums)-1
    k=True
    if(nums[0]==nums[len(nums)-1]):
        if(target==nums[0]):
            return True
        else:
            while(nums[oldl]==nums[oldr] and oldl<oldr):
                oldl+=1
                oldr-=1
                print(oldl,oldr)
    if(oldl==oldr):
        if(nums[oldl]==target):
            return True
        else:
            return False
    l=oldl
    r=oldr
    k=0
    while(l<=r):    #[0,1,1,2,0,0]
        mid=(l+r)//2
        if(nums[k]>nums[mid]):
            k=mid
            r=mid-1
        else:
            if(oldl!=0 and l==r):
                k=mid
            l=mid+1
        print(k)
    l=oldl
    r=oldr
    print(k,l,r)
    if(nums[k]==target):
        return True
    if(target==nums[r]):
        return True
    if(target==nums[l]):
        return True
    if(target>nums[r]):
        return BS(nums,l,k,target)
    else:
        return BS(nums,k,r,target)  
      
a=[1,3,5]
y=3
print(search(a,y))