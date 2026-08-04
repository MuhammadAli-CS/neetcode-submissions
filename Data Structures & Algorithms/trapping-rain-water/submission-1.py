class Solution:
    def trap(self, height: List[int]) -> int:
        
        #bounded if theres a non zero cell both below and after. 
        #hard part is taking account of heights as well tho cant just use min function

        #a possible way is that we go throught the array left to right and whenever we 
        #see a nonzero cell we start an area adding up the empty spaces in between upto 
        #height


        l=0
        r=len(height)-1
        total=0
        leftmax=rightmax=0
        while l<r:
            if height[l]<height[r]:
                leftmax=max(leftmax, height[l])
                total+=leftmax-height[l]
                l+=1
            else:
                rightmax=max(rightmax, height[r])
                total+=rightmax-height[r]
                r-=1
        return total
