class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans=[]
        prev=intervals[0]
        for i in range(1,len(intervals)):
            curr=intervals[i]
            if curr[0]>prev[1]:
                ans.append(prev)
                prev=curr
                continue
            prev=[min(curr[0],prev[0]),max(curr[1],prev[1])]
        ans.append(prev)
        return ans