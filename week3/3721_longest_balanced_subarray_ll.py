class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.min_val = [0] * (4 * n)
        self.max_val = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def push_down(self, node: int):
        if self.lazy[node] != 0:
            lz = self.lazy[node]
            left, right = 2 * node, 2 * node + 1
            
            self.min_val[left] += lz
            self.max_val[left] += lz
            self.lazy[left] += lz
            
            self.min_val[right] += lz
            self.max_val[right] += lz
            self.lazy[right] += lz
            
            self.lazy[node] = 0

    def push_up(self, node: int):
        self.min_val[node] = min(self.min_val[2 * node], self.min_val[2 * node + 1])
        self.max_val[node] = max(self.max_val[2 * node], self.max_val[2 * node + 1])

    def update(self, node: int, start: int, end: int, l: int, r: int, val: int):
        if l <= start and end <= r:
            self.min_val[node] += val
            self.max_val[node] += val
            self.lazy[node] += val
            return

        self.push_down(node)
        mid = (start + end) // 2
        if l <= mid:
            self.update(2 * node, start, mid, l, r, val)
        if r > mid:
            self.update(2 * node + 1, mid + 1, end, l, r, val)
        self.push_up(node)

    def query_first_zero(self, node: int, start: int, end: int, limit_r: int) -> int:
        if start > limit_r or self.min_val[node] > 0 or self.max_val[node] < 0:
            return -1

        if start == end:
            return start if self.min_val[node] == 0 else -1

        self.push_down(node)
        mid = (start + end) // 2

        res = self.query_first_zero(2 * node, start, mid, limit_r)
        if res != -1:
            return res
        return self.query_first_zero(2 * node + 1, mid + 1, end, limit_r)
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        tree = SegmentTree(n)
        last_seen = {}
        max_len = 0
        
        for R in range(n):
            val = nums[R]
            prev_idx = last_seen.get(val, -1)
            diff = 1 if val % 2 == 0 else -1
            
            tree.update(1, 0, n - 1, prev_idx + 1, R, diff)
            last_seen[val] = R
            
            first_zero_L = tree.query_first_zero(1, 0, n - 1, R)
            
            if first_zero_L != -1:
                max_len = max(max_len, R - first_zero_L + 1)
                
        return max_len
