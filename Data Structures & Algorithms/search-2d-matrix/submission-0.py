class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lm, rm=0, len(matrix)-1
        l, r=0, len(matrix[0])-1
        while lm<=rm:
            midr=(lm+rm)//2
            if matrix[midr][0]>target:rm=midr-1
            elif matrix[midr][-1]<target: lm=midr+1
            else: break
            
        
        while l<=r:
            mid=(l+r)//2
            if matrix[midr][mid]==target: return True
            if matrix[midr][mid]<target:
                l=mid+1
            else:
                r=mid-1

        return False