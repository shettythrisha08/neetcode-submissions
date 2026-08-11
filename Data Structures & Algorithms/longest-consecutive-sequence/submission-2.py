class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        count=0
        for i in range(len(nums)):
            if nums[i]-1 not in seen:
                current=nums[i]
                current_count=1
                while current+1 in seen:
                    current+=1
                    current_count+=1
                count=max(count,current_count)
        return count