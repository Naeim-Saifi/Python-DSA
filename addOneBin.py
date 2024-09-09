# n = 7
# m=10

# while (n > 0 & m>0):
#     last_bit = n & 1
#     n >>= 1
#     next_bit = n & 1
#     if last_bit == next_bit:
#         print(False)
#         break
# else:
#     print(True)

#2220. Minimum Bit Flips to Convert Number
m=4
n = 3 #goal
count=0
while (n > 0 or m>0):
    if(m & 1) != (n & 1):
        count+=1
    n>>=1
    m>>=1
print(count)