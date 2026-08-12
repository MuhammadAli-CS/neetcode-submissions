class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        leng=len(words)
        charcounts=Counter()
        for word in words:
            charcounts.update(word)
        for count in charcounts.values():
            if count % leng!=0:
                return False
        return True