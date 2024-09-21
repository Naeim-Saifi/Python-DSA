l1=[1,2,0,0]
sum=0
rev=0
k=34
for i in range(0,len(l1)):
  sum=sum*10+l1[i]
sum=sum+k
while(sum!=0):
  a=sum%10
  rev=rev*10+a
  sum=sum//10
j=0
while(rev!=0):
  a=rev%10
  rev=rev//10
  l1[j]=a
  j=j+1
print(l1)
