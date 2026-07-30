class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        leng=len(nums)
        res=[]
        for i in range(leng):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l=i+1
            r=leng-1
            target=-nums[i]
            while l<r:
                curr=nums[l]+nums[r]
                if curr == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif curr<target:
                    l+=1
                else: r-=1
        return res