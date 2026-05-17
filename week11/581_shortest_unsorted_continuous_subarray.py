class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        left, right = -1, -1
        max_val = float('-inf')
        min_val = float('inf')
        
        for i in range(n):
            if nums[i] < max_val:
                right = i
            else:
                max_val = nums[i]
                
        for i in range(n - 1, -1, -1):
            if nums[i] > min_val:
                left = i
            else:
                min_val = nums[i]
                
        if right == -1:
            return 0
            
        return right - left + 1
