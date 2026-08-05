class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def compare(freq1, freq2):
            for key in freq2:
                if key not in freq1:
                    return False
                if freq1[key]<freq2[key]: 
                    return False
            return True

        if len(s)<len(t): return ''
        freqt={}
        for r in range(len(t)):
            freqt[t[r]]=freqt.get(t[r],0)+1
        
        freq={}
        for r in range(len(t)):
            if s[r] in freqt:
                freq[s[r]]=freq.get(s[r],0)+1

        if freq==freqt:
            return s[:len(t)]

        l=0
        found= False
        res=s[:]
        r=len(t)
        while r<len(s):
            if s[r] in freqt:
                freq[s[r]]=freq.get(s[r],0)+1
            while r>l and s[l] not in freqt:
                l+=1
            while r>l and s[l] in freqt and freq.get(s[l], 0)>freqt[s[l]]:
                freq[s[l]]-=1
                if freq[s[l]]==0: del freq[s[l]]
                l+=1

            #whole substring completed
            while compare(freq, freqt):
                found=True
                if len(res)>(r-l+1):
                    res=s[l:r+1]
                if s[l] in freqt: 
                    freq[s[l]]=freq.get(s[l],1)-1
                    if freq[s[l]]==0: del freq[s[l]]
                l+=1
            r+=1


        if not found: return ''
        return res