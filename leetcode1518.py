numBottles,numExchange=9,3
count=numBottles
a=1
while(a!=0):
    a=numBottles//numExchange
    b=numBottles%numExchange
    numBottles=a+b
    count+=a
print(count)