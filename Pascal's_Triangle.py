class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return pascal
        for i in range(numRows-2):
            num = [1]        
            for i in range(len(pascal[-1]) - 1):
                num.append(pascal[-1][i] + pascal[-1][i+1])
            num.append(1)
            pascal.append(num)
        return pascal
