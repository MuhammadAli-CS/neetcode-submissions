class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=''.join(sorted(s1))
        l=0
        for r in range(len(s1), len(s2)+1):

            substr=s2[l:r]
            substr=''.join(sorted(substr))
            if substr==s1: return True

            l+=1
        return False
