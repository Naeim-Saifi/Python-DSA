nums = [-1,1,0,-3,3]

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
