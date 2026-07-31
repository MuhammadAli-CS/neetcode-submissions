class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        #divide array into before and after i[dont include i]
        pre=[]
        post=[1 for n in range(len(nums))]
        for i in range(len(nums)):
            if i==0:
                pre.append(1)
                continue
            pre.append(nums[i-1]*pre[i-1])

        for j in range(len(nums)-1, -1, -1):
            if j==len(nums)-1:
                post[j]=1
                continue
            post[j]=(nums[j+1]*post[j+1])
        
        for i in range(len(nums)):
            output.append(pre[i]*post[i])

        return output