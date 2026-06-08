class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
    
        n = len(arr)

        for i in range(n):
            for j in range(n):
                if i != j and arr[i] == 2 * arr[j]:
                    return True

        return False
    
    #optimized solution
    def checkIfExist(self, arr: List[int]) -> bool:
    
        s = set()

        for i in arr:
            if 2 * i in s :
                return True
            if i % 2 == 0 and i // 2 in s:
                return True
            s.add(i)

        return False