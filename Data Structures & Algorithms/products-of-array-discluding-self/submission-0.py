from typing import List   # Concept: Import type hints for clarity

# OOP structure: class with a method
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # VARIABLES
        n = len(nums)             # variable 'n' stores length of array
        output = [1] * n          # array 'output' initialized with 1s
        
        # LOOP 1: Prefix pass (left to right)
        prefix = 1                # variable 'prefix' starts as 1
        for i in range(n):        # loop through each index
            output[i] = prefix    # store product of all elements before i
            prefix *= nums[i]     # update prefix by multiplying current element
        
        # LOOP 2: Suffix pass (right to left)
        suffix = 1                # variable 'suffix' starts as 1
        for i in range(n-1, -1, -1):  # loop backwards
            output[i] *= suffix   # multiply stored prefix with suffix
            suffix *= nums[i]     # update suffix by multiplying current element
        
        # RETURN final array
        return output


# DRIVER CODE (testing)
solution = Solution()              # OOP: create object of class
nums1 = [1, 2, 4, 6]
nums2 = [-1, 0, 1, 2, 3]

print("Input:", nums1)
print("Output:", solution.productExceptSelf(nums1))  # Expected [48, 24, 12, 8]

print("Input:", nums2)
print("Output:", solution.productExceptSelf(nums2))  # Expected [0, -6, 0, 0, 0]
