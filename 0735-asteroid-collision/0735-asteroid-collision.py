class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        #add the newly arrived asteroid to the res
        #check if the new or the last element in res are opposite
            # if they are opposite remove the smaller one 
        #esle add to res

        for a in asteroids:
            #check for the collions
            while res and a < 0 < res[-1]:
                #crash the top if a is larger
                if abs(a) > res[-1]:
                    res.pop()
                # do nothing if a is smaller than top
                elif abs(a) < res[-1]:
                    break
                # if top and a are equal crash the top and do nothing to a
                else:
                    res.pop()
                    break
            else:
                res.append(a)

        return res