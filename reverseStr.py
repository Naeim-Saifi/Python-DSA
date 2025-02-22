def reverse_string(s):
    # Base case
    if len(s) == 0:
        return s
    return s[-1] + reverse_string(s[:-1])

print(reverse_string("abcd"))