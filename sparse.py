numbers = [0, 3, 0, 0, 7, 0, 0, 0, 2, 0, 5]
sm={}
for i in range(len(numbers)):
    if numbers[i]!=0:
        sm[i]=numbers[i]
print(sm)