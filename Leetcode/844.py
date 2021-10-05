class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        si = len(s)-1
        ti = len(t)-1
        
        def nextCharInd(string, i):
            if string[i] != '#':
                return i
            count = 0
            while i >= 0 and (count > 0 or count == 0 and string[i] == '#'):
                if string[i] == '#':
                    count += 1
                else:
                    count -= 1
                i -= 1
            return i
        
        while True:
            si = nextCharInd(s, si)
            ti = nextCharInd(t, ti)
            
            if not (si >= 0 and ti >= 0 and s[si] == t[ti]):
                return si == ti == -1
            si -= 1
            ti -= 1
        