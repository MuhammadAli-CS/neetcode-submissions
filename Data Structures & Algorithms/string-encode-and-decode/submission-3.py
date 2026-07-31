class Solution:

    def encode(self, strs: List[str]) -> str:
        #str(char), ord(char) , chr(ascii)
        if not strs:
            return "!"
        result=[]
        for words in strs:
            temp=[]
            for chars in words:
                asc=ord(chars)
                if asc<10: temp.append("00"+str(asc))
                elif asc<100: temp.append("0"+str(asc))
                else: temp.append(str(asc))
            
            result.append("".join(temp))
        s=''
        if result:
            s=",".join(result)
        return s
    def decode(self, s: str) -> List[str]:
        if s == "!": return []
        res=[]
        i=0
        lens=len(s)
        temp=[]
        while i<lens:
            if s[i]==",":
                res.append("".join(temp))
                temp=[]
                i+=1
            else:
                temp.append(chr(int(s[i:i+3])))
                i+=3
        res.append("".join(temp))
        return res
