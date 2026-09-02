class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        start_num = 0
        sequence_count = 1
        highest_count = 0
        #adding all the elements of the array in the set
        for i in range(len(nums)):
            seen.add(nums[i])
        #checking each of the elements to see if its value - 1 is in the set
        for i in range(len(nums)):
            if (nums[i] - 1) not in seen:
                start_num = nums[i]
                current_num = start_num

                #edge case to check if the current number isnt in the hash set
                if current_num + 1 not in seen:
                    if highest_count == 0:
                        highest_count = 1

                #while loop to continue checking if the current_number + 1 is still in the set
                while current_num + 1 in seen:
                    sequence_count +=1
                    current_num +=1
                    if sequence_count > highest_count:
                        highest_count = sequence_count

                sequence_count = 1

              

        return highest_count