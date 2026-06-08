def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_sum = float('-inf')
        for size in range (1 , n+1):
           for start in range (n-size +1):
              sum_subarray = sum(nums[start:start+size])
              max_sum = max(sum_subarray, max_sum)
        return max_sum      