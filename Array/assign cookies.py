class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child = 0
        cookie = 0
        count = 0
        g.sort()
        s.sort()
        while cookie < len(s) and child < len(g):
            if s[cookie]>=g[child]:
                count +=1
                cookie+=1
                child+=1
            else:
                cookie+=1
        return count

            

            

        
            