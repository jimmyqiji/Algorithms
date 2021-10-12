from copy import copy

class Solution:
    def validate(self, cur, k, j):
        for i in range(1, self.n):
            if k-i >= 0 and j-i >= 0 and cur[k-i][j-i] == 'Q':
                return False
            if k-i >= 0 and cur[k-i][j] == 'Q':
                return False
            if k-i >= 0 and j+i < self.n and cur[k-i][j+i] == 'Q':
                return False
        return True
            
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        result = []
        cur = []
        
        def backtrack(k):
            if k == n:
                result.append(copy(cur))
                return
            for j in range(n):
                if self.validate(cur, k, j):
                    kth_row = "."*j + "Q" + "."*(n-j-1);
                    cur.append(kth_row)
                    backtrack(k+1)
                    cur.pop()
        
        backtrack(0)
        return result