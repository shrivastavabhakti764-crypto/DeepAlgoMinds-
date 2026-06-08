class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxaverage = float("-inf")
       
        for start in range (len(nums)-k+1):
             sum1 = 0
             for end in range (start ,start + k):
                sum1 += nums[end]
             maxaverage=max(maxaverage,sum1/k)
        return maxaverage

#optimized solution
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):

            window_sum = window_sum + nums[i] - nums[i-k]

            max_sum = max(max_sum, window_sum)

        return max_sum / k
    