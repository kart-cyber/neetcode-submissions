class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        s2_dict = {}
        left = 0
        right = len(s1) - 1

        #1. make sure to put all the characters of s1 into a dictionary for comparison
        for char in s1:
            if char in s1_dict:
                s1_dict[char] +=1
            else:    
                s1_dict[char] = 1
        
        #2. start by assigning the window and checking if its respective dictionary matches the substring
        for right in range(len(s2)):
            new_char = s2[right]
            if new_char in s2_dict:
                s2_dict[new_char] +=1
            else: 
                s2_dict[new_char] = 1
        #3. Have a condition to check if the window size is too big and remove the old character from the previous left pointer index
            if right - left + 1 > len(s1):
                oldChar = s2[left]
                s2_dict[oldChar] -=1
                if s2_dict[oldChar] == 0:
                    del s2_dict[oldChar]
                left +=1
        #4. Have a condition to check if the window is the right size and compare dictionaries to see       if they are true  
            if right - left + 1 == len(s1):
                if s1_dict == s2_dict:
                    return True
    
        return False
            
