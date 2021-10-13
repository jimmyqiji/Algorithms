class Solution:
    def longestPalindrome(self, s: str) -> str:
        pointer = 0
        longest = ""
        while pointer < len(s):
            even_i = pointer-1
            even_j = pointer
            odd_i = pointer-1
            odd_j = pointer+1
            even_str = ""
            while even_i >= 0 and even_j < len(s) and s[even_i] == s[even_j]:
                even_str = s[even_i: even_j+1]
                even_i -= 1
                even_j += 1
            odd_str = s[pointer]
            while odd_i >= 0 and odd_j < len(s) and s[odd_i] == s[odd_j]:
                odd_str = s[odd_i:odd_j+1]
                odd_i -= 1
                odd_j += 1
            if len(even_str) > len(longest):
                longest = even_str
            if len(odd_str) > len(longest):
                longest = odd_str
            pointer += 1
        return longest