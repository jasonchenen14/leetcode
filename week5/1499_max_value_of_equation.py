import collections
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = collections.deque()
        max_val = float('-inf')
        
        for x, y in points:
            while q and x - q[0][1] > k:
                q.popleft()
                
            if q:
                max_val = max(max_val, q[0][0] + y + x)
                
            current_diff = y - x
            while q and q[-1][0] <= current_diff:
                q.pop()
                
            q.append((current_diff, x))
            
        return max_val
