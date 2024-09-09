# s='abcdaabcdebb'
# str=ord(s[0])
# count=1
# max=0
# for i in range(1,len(s)):
#   if(count>max):
#     max=count
#   if(str+1==ord(s[i])):
#     count+=1
#   else:
#     count=1
#   str=ord(s[i])
# print(max)

s='abcabcbb'
l1=[]
for i in range(len(s)):

  if(s[i] in l1):
    continue
  else:
    l1.append(s[i])
print(len(l1))
