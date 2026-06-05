class Solution:
    def commonElements(self, a, b, c):
        
       count = {}

       for i in range(len(a)):
            if i == 0 or a[i] != a[i - 1]:
                count[a[i]] = 1

       for i in range(len(b)):
            if i == 0 or b[i] != b[i - 1]:
              if count.get(b[i], 0) == 1:
                count[b[i]] = 2

       for i in range(len(c)):
            if i == 0 or c[i] != c[i - 1]:
              if count.get(c[i], 0) == 2:
                count[c[i]] = 3

       ans =[]

       for key, value in count.items():
            if value == 3:
                ans.append(key)

       return ans