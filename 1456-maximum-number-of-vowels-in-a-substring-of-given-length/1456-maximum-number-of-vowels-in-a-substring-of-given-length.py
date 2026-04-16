class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'o', 'e', 'u', 'i'}

        curr_vol = 0
        for i in range(k):
            if s[i] in vowels:
                curr_vol += 1
        
        max_vol = curr_vol

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr_vol += 1
            if s[i - k] in vowels:
                curr_vol -= 1
            
            if curr_vol == k:
                return k
            
            max_vol = max(max_vol, curr_vol)
        
        return max_vol