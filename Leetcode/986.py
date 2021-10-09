class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0
        while i < len(firstList) and j < len(secondList):
            [start_a, end_a] = firstList[i]
            [start_b, end_b] = secondList[j]
            if start_a <= start_b:
                if end_a < start_b:
                    i += 1
                elif end_a >= end_b:
                    j += 1
                    result.append([start_b, end_b])
                else:
                    i += 1
                    result.append([start_b, end_a])
            else:
                if end_b < start_a:
                    j += 1
                elif end_a <= end_b:
                    i += 1
                    result.append([start_a, end_a])
                else:
                    j += 1
                    result.append([start_a, end_b])
        return result
        