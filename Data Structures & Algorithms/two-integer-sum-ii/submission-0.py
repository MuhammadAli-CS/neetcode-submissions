class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hmap= {}
        for i, num in enumerate(numbers):
            remainder = target - num
            if remainder not in hmap:
                hmap[num]= i 
            else:
                return [ hmap[remainder]+1,i+1]