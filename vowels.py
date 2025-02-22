dict={}
s="naeimsaifi"
vowels='aeiouAEIOU'
for i in s:
    if i in vowels:
        dict[i]=dict.get(i,0)+1
print(dict)