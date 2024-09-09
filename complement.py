# n=7
# b=0
# c=''
# while(n!=0):
#     a=n & 1
#     b=b*10+a
#     if(a==1):
#         c+='0'
#     else:
#         c+='1'
#     n=n>>1
# print(b)
# print(c)

# class Solution {
#     public int bitwiseComplement(int n) {
#       int m=n;
#       int mask=0;
#       while(m!=0){
#         mask=(mask<<1)|1;
#         m=m>>1;
#       }
#       int ans=(~n) & mask;
#       return ans;
#     }

n=3
if(n==1):
    print("true")
elif(n & 1==0):
    print("true")
else:
    print("false")