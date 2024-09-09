arr=[11,34,4,2,6,4,7,1,86,5,100]
# min=arr[0]
# max=arr[0]
# for i in range(1,len(arr)):
#     if(min>arr[i]):
#         min=arr[i]
#     if(max<arr[i]):
#         max=arr[i]
# print("Minimum Number is : ",min,"\n Maximum : ",max)
#sort array

# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if(arr[i]<arr[j]):
#             swap=arr[j]
#             arr[j]=arr[i]
#             arr[i]=swap
# print(arr)
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return self._is_palindrome(s)

    def _is_palindrome(self, s):
        """
        Helper function to check if the string is a palindrome.
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
