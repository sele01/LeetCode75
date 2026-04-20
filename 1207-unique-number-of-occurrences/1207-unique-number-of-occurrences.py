class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}

        for num in arr:
            if num not in map:
                map[num] = 1
            else:
                map[num] += 1
        
        return len(set(map.values())) == len(map.values())