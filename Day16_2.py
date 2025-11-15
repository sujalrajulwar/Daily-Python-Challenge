# Given a string S,
# the task is to create a string with the first letter of every word in the string.


# Example 1:

# Input:
# S = "geeks for geeks"
# Output: gfg

# Example 2:

# Input:
# S = "bad is good"
# Output: big

S = "geeks for geeks"
res = ""

for i in range(len(S)):
    if S[i] != " " and (i == 0 or S[i - 1] == " "):
        res += S[i]

print(res)


# result = " "
# for char in range(len(S)):
#     if S[char] != " " and (S[char - 1] == " " or char == 0):
#         result += S[char]
#     print(S[char])
