class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = end = 0
        table = {}
        types = 0
        longest = 0
        
        while end < len(fruits):
            if fruits[end] not in table:
                table[fruits[end]] = 0
            if table[fruits[end]] == 0:
                types += 1
            table[fruits[end]] += 1
            end += 1
            
            if types == 3:
                while types == 3:
                    table[fruits[start]] -= 1
                    if table[fruits[start]] == 0:
                        types -= 1
                    start += 1
            else:
                longest = max(longest, end-start)
        return longest