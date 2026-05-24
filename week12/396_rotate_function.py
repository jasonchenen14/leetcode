class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        array_sum = sum(nums)
        current_f = sum(i * num for i, num in enumerate(nums))
        max_val = current_f
        
        for k in range(1, n):
            current_f = current_f + array_sum - n * nums[n - k]
            if current_f > max_val:
                max_val = current_f
                
        return max_val
