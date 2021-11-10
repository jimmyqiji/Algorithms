class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        for c in s:
            if c not in table:
                table[c] = 0
            table[c] += 1
        count = len(table)
        
        for c in t:
            if c not in table:
                return False
            table[c] -= 1
            if table[c] < 0: 
                return False
            if table[c] == 0:
                count -= 1
        return count == 0