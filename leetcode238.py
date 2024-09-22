#Given an integer array nums, return an array answer such 
# that answer[i] is equal to the product of all the elements of nums except nums[i].

# Example 1:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

nums = [1,2,3,4]

n = len(nums)
result = [1] * n  # Initialize the result array with 1s

# Calculate the prefix product
prefix = 1
for i in range(n):
    result[i] = prefix
    prefix *= nums[i]

# Calculate the suffix product
suffix = 1
for i in range(n - 1, -1, -1):
    result[i] *= suffix
    suffix *= nums[i]

print(result)
