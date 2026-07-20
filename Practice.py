def max_in_row(nums):
    mi=nums[0]
    ans=0
    for i in range(1,len(nums)):
        if(nums[i]>mi):
            mi=nums[i]
            ans=i
    return ans

def findPeakGrid(mat):
    if(len(mat)==1 and len(mat[0])==1):
        return [0,0]
    m = len(mat) 
    n = len(mat[0])
    l=0
    r=m-1
    while(l<=r):
        mid=(l+r)//2
        ci=max_in_row(mat[mid])
        print([l,r,mid,ci])
        if(mid==0):
            if(mat[0][ci]>mat[1][ci]):
                return [0,ci]
            else:
                print("paas")
                mid+=1
        if(mid==m-1):
            if(mat[m-1][ci]>mat[m-2][ci]):
                return [m-1,ci]
            else:
                print("daas")
                mid-=1
        # else:
        if(mat[mid][ci]>mat[mid-1][ci] and mat[mid][ci]>mat[mid+1][ci]):
            return [mid,ci]
        if(mat[mid][ci]>mat[mid-1][ci] and mat[mid][ci]>=mat[l][ci]):
            l=mid+1
        else:
            r=mid-1
    print(l,r,mid,ci,"Khaas")
    return -1

arr=[[92, 91, 57],[98, 24, 34]]
print(findPeakGrid(arr))