class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting=set()

        def dfs(crs):
            if crs in visiting: return False #cycle
            if preMap[crs]==[]: 
                return True
            visiting.add(crs)
            for course in preMap[crs]:
                if not dfs(course): return False
            
            visiting.remove(crs)
            preMap[crs]=[]
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True