# Given a string s , return reverse of the string as output.

# Example 1:

# Input:
# s = "GeeksforGeeks"
# Output: "skeeGrofskeeG"
# Explanation: Reverse string of "GeeksforGeeks" will be "skeeGrofskeeG"
# Example 2:

# Input:
# s = "ReversE"
# Output: "EsreveR"
# Explanation: Reverse string of "ReversE" will be "EsreveR"

# Your Task:
# You dont need to read input or print anything.
# Complete the function revStr() which takes s as input parameter and
# returns the reversed string .

s = "GeeksforGeeks"
res = ""
start = len(s) - 1
end = -1
for i in range(start, end, -1):
    res += s[i]
print(res)
