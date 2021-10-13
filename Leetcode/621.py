class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        table = {}
        max_count = 0
        number_of_max = 0
        for task in tasks:
            if task not in table:
                table[task] = 0
            table[task] += 1
            if table[task] == max_count:
                number_of_max += 1
            elif table[task] > max_count:
                number_of_max = 1
                max_count = table[task]
                
        slots = max_count - 1
        idles_per_slot = n - number_of_max + 1
        idles = slots * idles_per_slot
        available_tasks = len(tasks) - number_of_max * max_count
        return len(tasks) + max(0, idles - available_tasks)
        