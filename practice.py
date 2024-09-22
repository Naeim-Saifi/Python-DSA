num=[3,4,-2,5,8,20,-10,8]
sum=0
l1=[]
for i in range(len(num)):
    sum+=num[i]
sum_half=sum//2
for i in range(len(num)):
    if sum!=sum_half:
        sum-=num[i]
        l1.append(num[i])
    else:
        break
print(l1)