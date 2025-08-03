# Given a string s, convert the first letter of each word in the string to uppercase.

# Examples:

# Input: s = "gEEKs"
# Output: "GEEKs"
# Input: s = "i love programming"
# Output: "I Love Programming"
# Link : "https://www.geeksforgeeks.org/problems/upper-case-conversion5419/0"

s = "i love programming"

new_s = s.split(" ")
for i in range(len(new_s)):
    word = new_s[i]
    word_up = word[0].upper()
    new_word = word_up + word[1:]
    new_s[i] = new_word

final_s = " ".join(new_s)
