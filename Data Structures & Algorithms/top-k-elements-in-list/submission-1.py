class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])

        for num in count:
            frequency = count[num]
            bucket[frequency].append(num)

        result = []

        for frequency in range(len(nums), 0, -1):
            for num in bucket[frequency]:
                result.append(num)

                if len(result) == k:
                    return result