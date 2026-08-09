class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            #found
            if nums[mid]==target: return mid

            #eft half is sorted
            if nums[mid]>nums[r]:
                if nums[l]<=target<nums[mid]:
                    #hould be in sorted side
                    r=mid-1
                else:
                    #unsorted side
                    l=mid+1
            else: #right half sorted
                if nums[mid]<target<=nums[r]:
                    l=mid+1
                else: r=mid-1

        return -1