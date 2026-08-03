class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        res=0
        count={}
        chmax=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r], 0)
            chmax=max(chmax, count[s[r]])

            while (r-l+1) - chmax > k:
                count[s[l]]-=1
                l+=1
            res=max(res, r-l+1)
        return res
