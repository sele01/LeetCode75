class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = 1
        pos = 1
        res = [0]*n

        #pre fix product
        for i in range(n):
            res[i] = pre
            pre *=nums[i]
        #post fix product
        for i in range(n - 1, -1, -1):
            res[i] *= pos
            pos *= nums[i]
        
        return res