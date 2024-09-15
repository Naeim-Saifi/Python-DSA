n="CMXC"
total=0
prev=0
roman_map = {
    "M": 1000, "D": 500, 
    "C": 100,"L": 50,
    "X": 10,  "V": 5,  "I": 1
}
for i in reversed(n):
    curr=roman_map[i]
    if(curr>prev):
        total+=curr
    else:
        total-=curr
    prev=curr
print(total)