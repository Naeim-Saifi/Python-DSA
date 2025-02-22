n=4
d=333
letter_Count={}
s=""
s+=str(n/d)
for i in s:
    #if letter not exist in letter_Count dict it will return 0 else count of that word
    
    letter_Count[i]=letter_Count.get(i,0)+1 

print(s)