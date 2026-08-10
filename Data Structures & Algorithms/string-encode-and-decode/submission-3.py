class Solution:

    def encode(self, strs: List[str]) -> str:
        sstrs=""
        for el in strs:
            sstrs+=str(len(el))+"#"+el
        return sstrs

    def decode(self, s: str) -> List[str]:
        i=0
        result=[]
    
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            leng=int(s[i:j])
            word=s[j+1:leng+1+j]
            result.append(word)
            i=j+1+leng
        return result