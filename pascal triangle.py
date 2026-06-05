class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pt= [[1]]
        if numRows == 1:
            return pt
        pt.append([1,1])
        for i in range(2,numRows):
            row = [1]
            for j in range (1,i):
                row.append(pt[i-1][j-1] + pt[i-1][j])
            row.append(1)
            pt.append(row)
        return pt                     
        
