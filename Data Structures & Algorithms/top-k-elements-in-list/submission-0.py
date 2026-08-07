class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

    # Step 1: Count frequency
        for num in nums:
            count[num] = count.get(num, 0) + 1

    # Step 2: Create buckets
        bucket = []

        for i in range(len(nums) + 1):
            bucket.append([])

    # Step 3: Put numbers into frequency buckets
        for num in count:
            frequency = count[num]
            bucket[frequency].append(num)

    # Step 4: Traverse buckets from highest frequency
        result = []

        for frequency in range(len(nums), 0, -1):
            for num in bucket[frequency]:
                result.append(num)

                if len(result) == k:
                    return result