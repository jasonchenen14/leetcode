class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            current_sum = 0
            workers_needed = 1
            
            for num in nums:
                if current_sum + num > max_sum:
                    workers_needed += 1
                    current_sum = num
                else:
                    current_sum += num
                    
            return workers_needed <= k

        left = max(nums)
        right = sum(nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
                
        return left
