from functools import cache
class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0
            
        compressed_s = [s[0]]
        for char in s[1:]:
            if char != compressed_s[-1]:
                compressed_s.append(char)
        s = "".join(compressed_s)
        
        @cache
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
                
            res = dp(i, j - 1) + 1
            
            for k in range(i, j):
                if s[k] == s[j]:
                    res = min(res, dp(i, k) + dp(k + 1, j - 1))
                    
            return res
            
        return dp(0, len(s) - 1)
