class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        # We want to keep 'first' and 'second' as small as possible
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                # Found a new smallest element
                first = num
            elif num <= second:
                # Found an element larger than first, but smaller than second
                second = num
            else:
                # Found an element larger than both first and second!
                return True
                
        return False