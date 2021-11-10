class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        table = {}
        for [a, b] in prerequisites:
            if a not in table:
                table[a] = []
            table[a].append(b)
        visited = set()
        recursing = set()
        
        def findCycle(course):
            visited.add(course)
            if course not in table:
                return False
            recursing.add(course)
            for nc in table[course]:
                if nc not in visited:
                    if findCycle(nc):
                        return True
                elif nc in recursing:
                    return True
            recursing.remove(course)
            return False
        
        for course in range(numCourses):
            if course not in visited:
                if findCycle(course):
                    return False
        return True