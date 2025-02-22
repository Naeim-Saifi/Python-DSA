letter_Count={}
letter="naeimsaifi"
for i in letter:
    #if letter not exist in letter_Count dict it will return 0 else count of that word
    letter_Count[i]=letter_Count.get(i,0)+1 


# for i in range(len(letter)):
#     count=0
#     for j in range(len(letter)):
#         if letter[i]==letter[j]:
#             count+=1
#     letter_Count.update({letter[i]:count})
# print(letter_Count)





# user_dict = {}

# # Number of entries you want to take from the user
# n = int(input("Enter the number of entries you want to add: "))

# for i in range(n):
#     key = input("Enter the key: ")
#     value = input("Enter the value: ")
#     user_dict[key] = value  # Add key-value pair to the dictionary

# print("The resulting dictionary is:")
# print(user_dict)
