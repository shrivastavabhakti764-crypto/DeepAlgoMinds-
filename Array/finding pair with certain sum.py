class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1= nums1 
        self.nums2= nums2

    def add(self, index: int, val: int) -> None:
        
       self.nums2[index]+=val

    def count(self, tot: int) -> int:
        ans = 0
        for i in range(len(self.nums1)):
            for j in range (len(self.nums2)):
               if self.nums1[i]+self.nums2[j] == tot:
                  ans += 1
        return ans       


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)