# Given two strings A and B, find if A is a subsequence of B.

# Example 1:

# Input:
# A = AXY
# B = YADXCP
# Output: 0
# Explanation: A is not a subsequence of B
# as 'Y' appears before 'A'.


# Example 2:

# Input:
# A = gksrek
# B = geeksforgeeks
# Output: 1
# Explanation: A is a subsequence of B.


# Your Task:
# You dont need to read input or print anything. Complete the function isSubSequence() which takes A and B as input parameters and returns a boolean value denoting if A is a subsequence of B or not.

A = "gksrek"
B = "geeksforgeeks"

count = 0
start = 0

for char in A:
    for j in range(start, len(B)):
        if char == B[j]:
            count += 1
            start = j + 1
            break
        else:
            continue

if count == len(A):
    print(True)
else:
    print(False)
