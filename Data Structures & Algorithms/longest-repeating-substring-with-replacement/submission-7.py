class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #assign left and right index
        count = {}
        left_index = 0
        right_index = 0
        max_length = 0
        for right_index in range (len(s)):

        #length of the sub string to do calculations for the least letter used
            length_sub = right_index - left_index + 1
            


        #initializing the letter within the count dictionary and adding 1 to it everytime we encounter it
            if s[right_index] in count:
                count[s[right_index]] += 1
            else:
                count[s[right_index]] = 1


            while (length_sub - max(count.values())  > k):
                count[s[left_index]] -= 1
                left_index +=1
                length_sub = right_index - left_index + 1

            if length_sub > max_length:
                max_length = length_sub
            
        return max_length

