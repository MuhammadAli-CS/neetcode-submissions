class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans=[]

        for point in points:
            distance=(math.sqrt(( point[0])**2 + (point[1])**2))
            dist_pnt=(-distance, point)
            heapq.heappush(ans, dist_pnt)
            if len(ans)>k:
                heapq.heappop(ans)

        
        return [point for _, point in ans]