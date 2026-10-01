class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_index = 0
        right_index = len(s) - 1
        string_lower = s.lower()
        while left_index < right_index:
            while left_index < right_index and not string_lower[left_index].isalnum():
                left_index +=1
            while left_index < right_index and not string_lower[right_index].isalnum():
                right_index -=1
            if string_lower[left_index] != string_lower[right_index]:
                return False
            
            left_index +=1
            right_index -=1
            
        return True