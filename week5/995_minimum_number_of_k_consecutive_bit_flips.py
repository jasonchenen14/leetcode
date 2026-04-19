import collections
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        q = collections.deque()
        res = 0
        n = len(nums)
        
        for i in range(n):
            if q and i >= q[0] + k:
                q.popleft()
                
            if (nums[i] + len(q)) % 2 == 0:
                if i + k > n:
                    return -1
                
                q.append(i)
                res += 1
                
        return res
