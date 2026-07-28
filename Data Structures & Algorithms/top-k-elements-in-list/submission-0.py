class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        import heapq
        freqheap = []
        #  build maxheap with heapq using -ive sign
        for item in nums:
            if item in freq:
                freq[item]-=1
            else: freq[item]=-1
        for num, count in freq.items():
            heapq.heappush(freqheap, (count, num))
        result=[]
        for _ in range(k):
            result.append(heapq.heappop(freqheap)[1])
        return result