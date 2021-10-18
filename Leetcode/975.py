class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        odd_good = [False for _ in range(len(arr))]
        even_good = [False for _ in range(len(arr))]
        odd_stuck = [False] * len(arr)
        even_stuck = [False] * len(arr)
        s = []
        for i in range(len(arr)):
            s.append([arr[i], i])
        s.sort()
        
        cur = []
        def badRoute():
            for i in range(0, len(cur), 2):
                _, even_ind = cur[i]
                even_stuck[even_ind] = True
            for i  in range(1, len(cur), 2):
                _, odd_ind = cur[i]
                odd_stuck[odd_ind] = True
            cur.clear()
            return
        def goodRoute():
            for i in range(0, len(cur), 2):
                _, even_ind = cur[i]
                even_good[even_ind] = True
            for i  in range(1, len(cur), 2):
                _, odd_ind = cur[i]
                odd_good[odd_ind] = True
            cur.clear()
            return
        
        def backtrack(s_i) :
            val, ind = cur[-1]
            odd = len(cur) % 2
            if (odd and even_stuck[ind]) or (not odd and odd_stuck[ind]):
                badRoute()
                return
            if ind == len(arr)-1 or (odd and even_good[ind]) or (not odd and odd_good[ind]):
                goodRoute()
                return
            if not odd:
                if s_i + 1 < len(s) and s[s_i+1][0] == val:
                    cur.append(s[s_i+1])
                    backtrack(s_i+1)
                    return
                next_i = s_i-1
                while next_i >= 0 and s[next_i][1] < ind:
                    next_i -= 1
                while next_i - 1 >= 0 and s[next_i-1][0] == s[next_i][0] and s[next_i-1][1] > ind:
                    next_i -= 1
                if next_i >= 0 and s[next_i][1] > ind:
                    cur.append(s[next_i])
                    backtrack(next_i)
                else:
                    badRoute()
                return
            # odd jump
            next_i = s_i+1
            while next_i < len(s) and s[next_i][1] < ind:
                next_i += 1
            while next_i + 1 < len(s) and s[next_i+1][0] == s[s_i+1][0] and s[next_i][1] <= ind:
                next_i += 1
            if next_i < len(s) and s[next_i][1] > ind:
                cur.append(s[next_i])
                backtrack(next_i)
            else:
                badRoute()
            return
        
        for i in range(len(s)):
            cur.append(s[i])
            backtrack(i)
                
        return sum(even_good)