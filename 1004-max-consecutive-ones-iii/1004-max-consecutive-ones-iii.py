class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = max_len = zeros = 0

        #traversing the array
        for right in range(len(nums)):
            #counting the zeros
            if nums[right] == 0:
                zeros += 1
            
            #shinking the array
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            

            max_len = max(max_len, right - left + 1)
        
        return max_len