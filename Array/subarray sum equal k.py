class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
       
        count = 0
        for start in range(len(nums)):
            current_sum =0
            for end in range(start , len(nums)):
                current_sum+=nums[end]
                if current_sum == k :
                   count += 1
        return count
    
    #optimized approach 
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sum_count = {0: 1}  # Prefix sum count map

        for num in nums:
            current_sum += num
            
            # Check if there is a prefix sum that matches current_sum - k
            if (current_sum - k) in prefix_sum_count:
                count += prefix_sum_count[current_sum - k]
            
            # Update the prefix sum count map
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
        
        return count
