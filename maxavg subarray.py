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
        maxaverage = float("-inf")
        current_sum = sum(nums[:k])  # Sum of the first 'k' elements
        maxaverage = max(maxaverage, current_sum / k)
        
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # Slide the window
            maxaverage = max(maxaverage, current_sum / k)
        
        return maxaverage