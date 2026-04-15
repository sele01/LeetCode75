class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        min_dist = n

        for i in range(n):
            if words[i] == target:
                dist = abs(i - startIndex)
                actual_dist = min(dist, n - dist)
                min_dist = min(min_dist, actual_dist)
        
        return min_dist if min_dist != n else -1