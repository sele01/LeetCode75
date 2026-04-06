class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        new = [0] + flowerbed + [0]

        for i in range(1, len(new)-1):
            if new[i-1] == new[i] == new[i+1] == 0:
                new[i] = 1
                n -= 1
        
        return n <= 0

            