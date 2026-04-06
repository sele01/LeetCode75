class Solution:
    def reverseWords(self, s: str) -> str:
        # .strip() removes leading/trailing whitespace
        s = s.strip().split()
    
        # Use .isalpha() to check for letters and [::-1] for a cleaner reverse
        return ' '.join(word for word in s[::-1] if word.isalnum())

