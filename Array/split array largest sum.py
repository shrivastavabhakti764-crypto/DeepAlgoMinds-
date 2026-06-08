class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(mid):
            current = 0
            parts = 1
            for  i in nums:
                if current + i <= mid:
                    current += i
                else:
                    parts += 1
                    current = i
            return parts <= k

        low = max(nums)
        high = sum(nums)
        ans = 0

        while low <= high:
            mid = (low + high)//2
            if canSplit(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans        
