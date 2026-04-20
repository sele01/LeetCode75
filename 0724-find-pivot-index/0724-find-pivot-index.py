class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left = 0
        right = total_sum - left

        for i in range(len(nums)):
            if right - nums[i] == left:
                return i
            left += nums[i]
            right = total_sum - left
        
        return -1
