class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1): return False
        freq={}
        for alpha in s1:
            freq[alpha]=freq.get(alpha, 0)+1
        window={}
        l=0
        for i in range(0, len(s1)):
            window[s2[i]]=window.get(s2[i],0)+1
        if window==freq: return True
        for r in range(len(s1), len(s2)):
            window[s2[l]]-=1
            if window[s2[l]]==0: del window[s2[l]]
            window[s2[r]]=window.get(s2[r],0)+1
            if window==freq: return True

            l+=1
        return False
