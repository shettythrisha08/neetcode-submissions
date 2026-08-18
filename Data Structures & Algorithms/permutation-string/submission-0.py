class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        right=0
        
        seen1={}
        seen2={}

        while right<len(s1):
            if s1[right] not in seen1:
                seen1[s1[right]]=1
            else:
                seen1[s1[right]]+=1
            right+=1
        right=0
        while right<len(s2):
            if s2[right] not in seen2:
                seen2[s2[right]]=1
            else:
                seen2[s2[right]]+=1
            right+=1
            
            if right-left>len(s1):
                seen2[s2[left]]-=1
                if seen2[s2[left]]==0:
                    del seen2[s2[left]]
                left+=1
            if right-left==len(s1):
                if seen1==seen2:
                    return True
        return False
