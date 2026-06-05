class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = {}
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]]+=1
            else:
                counter[nums[i]]=1  

        for k,v in counter.items():
            if v == 1:
                return k

