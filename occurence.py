letter_Count={}
letter="mississippi"
for i in letter:
    #if letter not exist in letter_Count dict it will return 0 else count of that word
    letter_Count[i]=letter_Count.get(i,0)+1 
print(letter_Count)