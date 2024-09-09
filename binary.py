#Binary to Decimal Technique1
# n = 5
# rem = 0
# while n != 0:
#     q = n // 2
#     a = n % 2
#     rem = (rem * 10) + a
#     n = q
# print(rem)

#Technique 2
# n=5
# rem=0
# i=0
# while(n!=0):
#     bit=n & 1
#     rem=(bit*pow(10,i))+rem
#     n=n>>1
#     i=i+1
# print(rem)

# n = -5  # Example with a negative number
# rem = 0
# i = 0
# if n < 0:
#     n = (1 << 8) + n  # Convert n to a 32-bit two's complement binary

# while n != 0:
#     bit = n & 1
#     rem = (bit * pow(10, i)) + rem
#     n = n >> 1
#     i += 1

# print(rem)


#Binary to decimal value will be in form of binary
# n=0b10101
# d=0
# i=0
# while(n!=0):
#     bit=n & 1
#     if(bit!=0):
#         d=d+pow(2,i)
#     n=n >> 1
#     i=i+1
# print(d)

#User can enter value in decimal form 10101 it will be treated as binary
# n=1010
# d=0
# i=0
# while(n!=0):
#     bit=n%10
#     if(bit!=0):
#         d=d+pow(2,i)
#     n=n//10
#     i=i+1
# print(d)

# x=1534236469
# s=1
# if(x<0):
#     x=-x
#     s=-1
# rev = 0
# while x != 0:
#     a = x % 10
#     x = x // 10
#     rev = rev * 10 + a
# print(rev*s)
        