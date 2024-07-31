# 2.Given a string, write a python function to check if it is palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as the string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

# Examples: 

# Input : malayalam
# Output : Yes
# Input : geeks
# Output : No

def is_para(s):
    return s == s[::-1]
a = input("Enter string: ")
if is_para(a):
    print("yes")
else:
    print("no")
    
#  def is_para(s):
#     return s == s[::-1]   
# print("yes" if is_para("malayalam") else "no")
# print("yes" if is_para("geeks") else "no")