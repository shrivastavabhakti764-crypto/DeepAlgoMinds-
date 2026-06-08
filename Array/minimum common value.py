class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
      
        d = {}

        for i in nums1:
            d[i] = 1

        for j in nums2:
            if j in d:
                return j

        return -1