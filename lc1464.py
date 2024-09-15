#return (max-1)*(secondmax-1)
m1,m2=-1,-1
nums=[10,1,2,5]
for i in range(len(nums)):
    if(m1<nums[i]):
        m2=m1
        m1=nums[i]
    elif(m2<nums[i]):
        m2=nums[i]
res=(m1-1)*(m2-1)
print(res)