class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            remainder = target - num
            if remainder not in seen:
                seen[num]=i
            else:
                return [seen[remainder], i]
            