from functools import cache
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(i: int, j: int, k: int) -> int:
            if i > j:
                return 0
            
            i_new, k_new = i, k
            while i_new + 1 <= j and boxes[i_new + 1] == boxes[i]:
                i_new += 1
                k_new += 1
                
            ans = (k_new + 1) ** 2 + dp(i_new + 1, j, 0)
            
            for m in range(i_new + 1, j + 1):
                if boxes[m] == boxes[i]:
                    ans = max(ans, dp(i_new + 1, m - 1, 0) + dp(m, j, k_new + 1))
                    
            return ans
            
        return dp(0, len(boxes) - 1, 0)
