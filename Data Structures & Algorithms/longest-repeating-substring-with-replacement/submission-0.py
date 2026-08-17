class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        right=0
        highest_frequency=0
        max_length=0
        seen={}
        while right<len(s):
            if s[right] not in seen:
                seen[s[right]]=1
            else:
                seen[s[right]]+=1
            right+=1

            highest_frequency=max(seen.values())

            while(right-left-highest_frequency)>k:
                seen[s[left]]-=1
                left+=1

                highest_frequency=max(seen.values())

            max_length=max(max_length,right-left)
        return max_length
