class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        str1={}
        str2={}
        for item in s:
            if item in str1:
                str1[item]+=1
            else:
                str1[item]=1
        for item in t:
            if item in str2:
                str2[item]+=1
            else:
                str2[item]=1
        if str1==str2:
            return True
        return False





