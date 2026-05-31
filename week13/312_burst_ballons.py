from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        padded_nums = [1] + nums + [1]
        
        @cache
        def dp(left: int, right: int) -> int:
            if left + 1 == right:
                return 0
                
            max_coins = 0
            
            for k in range(left + 1, right):
                coins = padded_nums[left] * padded_nums[k] * padded_nums[right]
                total = coins + dp(left, k) + dp(k, right)
                max_coins = max(max_coins, total)
                
            return max_coins
            
        return dp(0, len(padded_nums) - 1)
