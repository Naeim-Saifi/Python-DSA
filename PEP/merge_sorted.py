num1 = [1, 2, 3]
num2 = [2, 5, 6]
l1 = []
i, j = 0, 0

while i < len(num1) or j < len(num2):
    if i == len(num1):  # If we've exhausted num1
        l1.extend(num2[j:])
        break
    elif j == len(num2):  # If we've exhausted num2
        l1.extend(num1[i:])
        break
    elif num1[i] > num2[j]:
        l1.append(num2[j])
        j += 1
    elif num1[i] < num2[j]:
        l1.append(num1[i])
        i += 1
    else:  # If num1[i] == num2[j]
        l1.append(num1[i])
        i += 1

print(l1)
