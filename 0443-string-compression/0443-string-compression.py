class Solution:
    def compress(self, chars: List[str]) -> int:
        #holder for unique values and seeker for iteration on the array
        holder, seeker = 0, 0

        while seeker < len(chars):
            letter = chars[seeker]
            count = 0
            #counting similar characters
            while seeker < len(chars) and chars[seeker] == letter:
                count += 1
                seeker += 1
            
            chars[holder] = letter
            holder += 1
            #converting and storing the count to the array
            if count > 1:
                for c in str(count):
                    chars[holder] = c
                    holder += 1
        #returing the length of the final array
        return holder
        