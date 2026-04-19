class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        trip = [0]
    

        for alt in gain:
            trip.append(alt + trip[-1])
        
        return max(trip)