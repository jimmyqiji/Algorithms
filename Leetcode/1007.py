class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def alignX(x):
            top_flips = 0
            bot_flips = 0
            for i in range(len(tops)):
                if tops[i] == x:
                    if bottoms[i] != x:
                        bot_flips += 1
                elif bottoms[i] == x:
                    top_flips += 1
                else:
                    top_flips = -1
                    bot_flips = -1
                    break
            return min(top_flips, bot_flips)
        a = tops[0]
        b = bottoms[0]
        
        res_a = alignX(a)
        res_b = alignX(b)
        if res_a == res_b == -1:
            return -1
        if res_a == -1:
            return res_b
        if res_b == -1:
            return res_a
        return min(res_a, res_b)
 