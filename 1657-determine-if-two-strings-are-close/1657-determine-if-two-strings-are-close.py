class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        # check if the length are equal(if not return false)
        if len(word1) != len(word2):
            return False
        

        #we can use counter class to get the key and the frequencies
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        #check if the keys and the frequencies are equal

        return (counter1.keys() == counter2.keys()) and (sorted(counter1.values()) == sorted(counter2.values()))
        

    