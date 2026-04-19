class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        res = [1]
        
        while len(res) < n:
            odds = [2 * x - 1 for x in res if 2 * x - 1 <= n]
            evens = [2 * x for x in res if 2 * x <= n]
            res = odds + evens
            
        return res
