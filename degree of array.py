class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        first = {}

        degree = 0
        ans = len(nums)

        for i in range(len(nums)):

            if nums[i] not in first:
                first[nums[i]] = i

            count[nums[i]] = count.get(nums[i], 0) + 1

            if count[nums[i]] > degree:
                degree = count[nums[i]]
                ans = i - first[nums[i]] + 1

            elif count[nums[i]] == degree:
                ans = min(ans, i - first[nums[i]] + 1)

        return ans