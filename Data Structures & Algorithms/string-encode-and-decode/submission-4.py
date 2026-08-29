class Solution:

    def encode(self, strs: List[str]) -> str:
        #to create the string, ensure that each of the strings within the list has the following
        #1. An integer which denotes the amount of characters wihtin the string
        #2. A delimiter which seperates the integer and the string itself
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        #while i is still within the string length, continue to perform the functions within the loop
        while i < len(s):
            #create another pointer 'j' which serves as an index to help find the first delimiter
            j = i
            while s[j] != '#':
                j += 1
        #this now allows for the length to be easily determined by the specific integer that is between the two pointers
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
        
            


