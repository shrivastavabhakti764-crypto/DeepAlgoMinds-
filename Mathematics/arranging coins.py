class Solution:
    def arrangeCoins(self, n: int) -> int:
        total = 0

        for i in range(1, n + 1):
            total += i

            if total > n:
                return i - 1

        return n
    
    #optimized solution using binary search 
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = left + (right - left) // 2
            total = mid * (mid + 1) // 2

            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            else:
                right = mid - 1

        return right