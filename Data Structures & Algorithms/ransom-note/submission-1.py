class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letteramount={}
        for char in ransomNote:
            letteramount[char]=letteramount.get(char,0)+1
        for char in magazine:
            if char in letteramount:
                letteramount[char]-=1
                if letteramount[char]==0: del letteramount[char]
        return letteramount =={}