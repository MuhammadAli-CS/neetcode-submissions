class Solution:
    def isValid(self, s: str) -> bool:
       
        if len(s) % 2 !=0:
            return False
        paras = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            if char == "[" or char =="(" or char == "{":
                paras.append(char)
                continue
            if not paras:
                return False
            last = paras.pop()
            if last != pairs[char]:
                return False
        return not paras

