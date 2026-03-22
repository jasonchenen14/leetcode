class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(left: int, right: int) -> int:
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = mergeSort(left, mid) + mergeSort(mid + 1, right)
            
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
                
            temp = []
            p1, p2 = left, mid + 1
            
            while p1 <= mid and p2 <= right:
                if nums[p1] <= nums[p2]:
                    temp.append(nums[p1])
                    p1 += 1
                else:
                    temp.append(nums[p2])
                    p2 += 1
            
            while p1 <= mid:
                temp.append(nums[p1])
                p1 += 1
            while p2 <= right:
                temp.append(nums[p2])
                p2 += 1
                
            nums[left:right + 1] = temp
            
            return count

        return mergeSort(0, len(nums) - 1)
