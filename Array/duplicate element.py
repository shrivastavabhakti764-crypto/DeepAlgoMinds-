class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        ans =[]
        for i in nums:
            if i not in ans:
                ans.append(i)
            else :
                return i    
