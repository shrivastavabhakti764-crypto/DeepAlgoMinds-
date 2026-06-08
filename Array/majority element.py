class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = {}
        n = len(nums)
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for k,v in freq.items():
            if v > n//2: 
                return k   
