# Given a string s, the task is to change the complete string to uppercase 
# or lowercase depending on the case of the first character.

# Examples:

# Input: s = "abCD"
# Output: "abcd"
# Explanation: The first letter (a) is lowercase. 
# Hence, the complete string is made lowercase.

# Input: s = "Abcd"
# Output: "ABCD"
# Explanation: The first letter (A) is uppercase. 
# Hence, the complete string is made uppercase.

#link ="https://www.geeksforgeeks.org/problems/change-the-string3541/0"

s = "AbCD"
res = ""
if s[0].isupper():
    res = s.upper()

else:
    res = s.lower()
print(res)