class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix = 0
        ans = 0

        for i in range(len(nums)):
            prefix += nums[i]

            # ceil(prefix / (i+1))
            avg = (prefix + i) // (i + 1)

            ans = max(ans, avg)

        return ans