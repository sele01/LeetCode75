class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'AOEUIaoeui'
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] in vowel and s[right] in vowel:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left] not in vowel and s[right] not in vowel:
                left += 1
                right -= 1
            elif s[left] in vowel and s[right] not in vowel:
                right -= 1
            elif s[left] not in vowel and s[right] in vowel:
                left += 1
        
        return ''.join(c for c in s)
            
            
            
            