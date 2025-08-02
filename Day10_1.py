# Given a string consisting of lowercase english alphabets.
# Find the repeated character present first in the string.

# NOTE - If there are no repeating characters return '#'.

# Example 1:

# Input:
# S = "geeksforgeeks"
# Output: g
# Explanation: g, e, k and s are the repeating
# characters. Out of these, g occurs first.
# Example 2:

# Input:
# S = "abcde"
# Output: -1
# Explanation: No repeating character present. (You need to return '#')

# Your Task:
# You don't need to read input or print anything.
# Your task is to complete the function firstRep()
# which takes the string S as input and
# returns the the first repeating character in the string.
# In case there's no repeating character present, return '#'.


S = "geeksforgeeks"

out = {}
for char in S:
    if char not in out:
        out[char] = 1
    else:
        out[char] = out[char] + 1

for key, val in out.items():
    if val > 1:
        print(key)
        break
    else:
        print("#")
