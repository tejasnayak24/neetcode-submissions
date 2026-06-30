class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW=len(matrix)
        COL=len(matrix[0])
        l=0
        r=(ROW*COL)-1
        while l<=r:
            m=(l+r)//2
            row=m//COL
            col=m%COL
            if matrix[row][col]<target:
                l=m+1
            elif matrix[row][col]>target:
                r=m-1
            else:
                return True
        return False       