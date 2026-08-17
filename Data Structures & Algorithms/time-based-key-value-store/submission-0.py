class TimeMap:

    def __init__(self):
        self.tmap={} #maps key: [[timestamp, value]]
    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.tmap:
            self.tmap[key]=[]
        self.tmap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        #binary search to get target time closest to given timestamp
        if not key in self.tmap: return ''
        l=0
        r=len(self.tmap[key])-1
        res=''
        
        while l<=r:    
            mid=(l+r)//2
            if self.tmap[key][mid][0] <=timestamp:
                res=self.tmap[key][mid][1]
                l=mid+1
            else:
                r=mid-1

        return res
                
        