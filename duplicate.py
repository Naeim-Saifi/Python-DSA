# nums=[4,3,2,7,8,2,3,1]
# l1 = []
# count = 1 # Define nums here
# # for i in range(len(nums)):
# #     for j in range(i+1, len(nums)):
# #         if(nums[i] == nums[j]):
# #             count = count + 1
# #             if(count > 1 and nums[i] not in l1):
# #                 l1.append(nums[i])
# #         if(count > 1):
# #             count = 1

# j=1
# for i in range(len(nums)):
#     if(nums[i]==)
# print(sorted(l1) )
nums = [1,2,4,1,2,5,4]
d = None # Initialize d to None for clarity
for i in range(len(nums)):
    count = 0 # Initialize count to 0 for counting occurrences
    for j in range(len(nums)): # Check all elements
        if nums[i] == nums[j]:
            count += 1 # Increment count for each occurrence
    if count == 1: # Check if the count is 1
        d = nums[i] # Assign the unique number to d
        break # Exit loop after finding the first unique number
print(d)