class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        t00 = [0] * (4 * n)
        t01 = [0] * (4 * n)
        t10 = [0] * (4 * n)
        t11 = [0] * (4 * n)
        
        def push_up(node: int):
            L = node * 2
            R = node * 2 + 1
            t00[node] = max(t00[L] + t10[R], t01[L] + t00[R])
            t01[node] = max(t00[L] + t11[R], t01[L] + t01[R])
            t10[node] = max(t10[L] + t10[R], t11[L] + t00[R])
            t11[node] = max(t10[L] + t11[R], t11[L] + t01[R])

        def build(node: int, start: int, end: int):
            if start == end:
                t11[node] = max(0, nums[start])
                return
            mid = (start + end) // 2
            build(node * 2, start, mid)
            build(node * 2 + 1, mid + 1, end)
            push_up(node)

        def update(node: int, start: int, end: int, idx: int, val: int):
            if start == end:
                t11[node] = max(0, val)
                return
            mid = (start + end) // 2
            if idx <= mid:
                update(node * 2, start, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, end, idx, val)
            push_up(node)

        build(1, 0, n - 1)
        total_sum = 0
        
        for pos, x in queries:
            update(1, 0, n - 1, pos, x)
            total_sum = (total_sum + t11[1]) % MOD
            
        return total_sum
