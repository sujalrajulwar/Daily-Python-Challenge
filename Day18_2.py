# Given a string s. Your task is to remove spaces from it.

# Examples:

# Input: s = "geeks  for geeks"
# Output: "geeksforgeeks"
# Explanation: All the spaces have been removed.
# Input: s = "    g f g"
# Output: "gfg"
# Explanation: All the spaces including the leading ones have been removed.
# Constraints:
# 1<=|s|<=105

s = "    g f g"
new_s = ""

for char in s:
    if char == " ":
        continue
    else:
        new_s += char
print(new_s)
