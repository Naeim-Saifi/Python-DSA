#counting of 1 on even occurence and odd occurence in binary 
n=2
o=0
e=0
i=0
while(n>0):
    a=n&1
    if(i%2==0 and a==1):
        e+=1
    elif(i%2!=0 and a==1):
        o+=1
    n>>=1
    i=i+1
print("Even ",e," odd",o)