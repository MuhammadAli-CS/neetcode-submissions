class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0 for i in range(len(temperatures))]
        stack=[]
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1]<temp:
                ans=stack.pop()
                answer[ans[0]]=i-ans[0]
            stack.append((i, temp))

        return answer