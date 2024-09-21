nums = [3, 0, 1]  

n = len(nums)
total_sum = n * (n + 1) // 2 
actual_sum = sum(nums)  
missing_number = total_sum - actual_sum  # The missing number

print(missing_number)
