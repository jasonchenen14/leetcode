class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)
        prev_bound = nums[-1]
        
        for i in range(n - 2, -1, -1):
            if nums[i] <= prev_bound:
                prev_bound = nums[i]
            else:
                k = (nums[i] + prev_bound - 1) // prev_bound
                operations += (k - 1)
                prev_bound = nums[i] // k
                
        return operations
