class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start=0
        end= len(s)-1
        while end>start:
            while start < end and not s[start].isalnum():
                start += 1

            while start < end and not s[end].isalnum():
                end -= 1
            if s[start].lower() != s[end].lower(): return False
            end-=1
            start+=1
        return True