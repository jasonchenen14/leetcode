import bisect
from functools import cache
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        
        @cache
        def dp(i: int, prev: int) -> int:
            if i == len(arr1):
                return 0
                
            res = float('inf')
            
            if arr1[i] > prev:
                res = min(res, dp(i + 1, arr1[i]))
                
            idx = bisect.bisect_right(arr2, prev)
            if idx < len(arr2):
                res = min(res, 1 + dp(i + 1, arr2[idx]))
                
            return res
            
        ans = dp(0, float('-inf'))
        return ans if ans != float('inf') else -1
