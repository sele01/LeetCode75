class Solution:
    def removeStars(self, s: str) -> str:
        res = []

        for ch in s:
            if ch is '*':
                res.pop()
            else:
                res.append(ch)
        
        return ''.join(res)