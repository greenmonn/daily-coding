class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0] * len(nums)
        if len(nums) == 0:
            return 0

        cache[0] = nums[0]

        if len(nums) == 1:
            return cache[0]

        cache[1] = max(cache[0], nums[1])

        for i, n in enumerate(nums):
            if i == 0 or i == 1:
                continue

            cache[i] = max(cache[i-1], cache[i-2] + nums[i])

        return cache[-1]
