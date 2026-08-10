class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i=0
        while i<len(intervals):
            interval=intervals[i]
            if interval[0]>newInterval[1]: #new interval is ending before the one we are on right now   
                #starts
                return intervals[:i]+[newInterval]+intervals[i:]
                i+=1
            if newInterval[0]>interval[1]: #new intreval starts after the one we are on ends
                i+=1  
                continue
                     
            newInterval=[min(newInterval[0], interval[0]), max(newInterval[1],interval[1])]
            del intervals[i]

        return intervals+[newInterval]