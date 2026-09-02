class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output_array =  [1] * n
        left_product = 1 
        for i in range (n):
            output_array[i] = left_product
            left_product = left_product * nums[i]
        right_product = 1
        for i in range(n -1, -1, -1):
            output_array[i] = right_product * output_array[i]
            right_product = right_product * nums[i]
            
        return output_array

