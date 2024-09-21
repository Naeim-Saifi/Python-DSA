numbers = [2, 7, 11, 15]  
target = 9  

i = 0
j = len(numbers) - 1 

while i < j:
    current_sum = numbers[i] + numbers[j]
    if current_sum == target:
        result = [i + 1, j + 1]
        print(result)
        break
    elif current_sum < target:
        i += 1  
    else:
        j -= 1  
else:
    print(-1)  # If no solution is found
