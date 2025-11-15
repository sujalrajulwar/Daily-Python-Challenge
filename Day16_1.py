# Given two strings txt and pat,
# return the 0-based index of the first occurrence of the substring pat in txt.
# If pat is not found, return -1.
# Note: You are not allowed to use the inbuilt function.

# Examples :

# Input: txt = "GeeksForGeeks", pat = "Fr"
# Output: -1
# Explanation: "Fr" is not present in the string "GeeksForGeeks" as substring.
# Input: txt = "GeeksForGeeks", pat = "For"
# Output: 5
# Explanation: "For" is present as substring in "GeeksForGeeks" from index 5
# (0 based indexing).
# Input: txt = "GeeksForGeeks", pat = "gr"
# Output: -1
# Explanation: "gr" is not present in the string "GeeksForGeeks" as substring.

txt = "sujalsrajulwar"
pat = "war"

for i in range(len(txt)):
    val = txt[i]
    # val2 = pat[0]
    if val == pat[0]:
        search = txt[
            i : i + len(pat)
        ]  # It will start counts from 0 to 10 for "sujalsrajulwar" here search = "war"
        if search == pat:
            print(i)
        else:
            continue
    else:
        continue
